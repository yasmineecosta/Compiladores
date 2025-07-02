# tac_generator.py

from JavythonParser import JavythonParser
from JavythonVisitor import JavythonVisitor
from tabela_simbolos import TabelaSimbolos # Você precisará da tabela de símbolos

class TACGenerator(JavythonVisitor):
    def __init__(self, tabela_simbolos: TabelaSimbolos):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.tabela_simbolos = tabela_simbolos # Acesso à tabela de símbolos

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, instruction):
        self.instructions.append(instruction)

    # Métodos de visita para cada regra da AST
    # Cada método visit* deve retornar o 'endereço' do resultado da sua subárvore,
    # que pode ser um nome de variável, um literal ou um temporário.

    def visitProgram(self, ctx: JavythonParser.ProgramContext):
        # Visitar declarações globais (se houver, embora seu exemplo não tenha)
        if ctx.decIds():
            self.visit(ctx.decIds())

        # Visitar métodos
        for metodo_ctx in ctx.metodo():
            self.visit(metodo_ctx)

        # Visitar main
        self.visit(ctx.main())
        return self.instructions

    def visitMetodo(self, ctx: JavythonParser.MetodoContext):
        method_name = ctx.ID().getText()
        # Emitir rótulo de entrada do método
        self.emit(f"label {method_name}_entry")

        # Entrar em novo escopo (já feito pelo analisador semântico, mas aqui é para contexto)
        # self.tabela_simbolos.entrar_escopo(method_name) # Se precisar gerenciar escopo aqui

        # Declarations within method
        if ctx.decIds():
            self.visit(ctx.decIds())

        # Commands within method body
        for comando_ctx in ctx.comando():
            self.visit(comando_ctx)

        # Retorno implícito para métodos void ou garantir um return para não-void
        simbolo_metodo = self.tabela_simbolos.buscar(method_name)
        if simbolo_metodo and simbolo_metodo.tipo == "void":
            self.emit("return")
        # else: for non-void methods, the `returnCmd` will handle the return

        # Sair do escopo (já feito pelo analisador semântico)
        # self.tabela_simbolos.sair_escopo()

    def visitMain(self, ctx: JavythonParser.MainContext):
        self.emit("label main_entry")
        # Similar ao método, mas sem retorno explícito
        if ctx.decIds():
            self.visit(ctx.decIds())
        for comando_ctx in ctx.comando():
            self.visit(comando_ctx)
        self.emit("return") # Ou exit, dependendo da convenção do seu TAC

    # Declarações não geram TAC, apenas marcam na tabela de símbolos
    def visitDecl(self, ctx: JavythonParser.DeclContext):
        pass # Already handled by symbol table

    def visitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        expr_result = self.visit(ctx.expressao()) # Obtém o temporário/valor da expressão
        self.emit(f"{var_name} = {expr_result}")
        return var_name # Retorna o nome da variável atribuída

    def visitReturnCmd(self, ctx: JavythonParser.ReturnCmdContext):
        expr_result = self.visit(ctx.expressao())
        self.emit(f"return {expr_result}")

    def visitInputCmd(self, ctx: JavythonParser.InputCmdContext):
        for id_node in ctx.idList().ID():
            self.emit(f"read {id_node.getText()}")

    def visitPrintCmd(self, ctx: JavythonParser.PrintCmdContext):
        for expr_ctx in ctx.expressao():
            expr_result = self.visit(expr_ctx)
            self.emit(f"print {expr_result}")

    def visitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        cond_temp = self.visit(ctx.expressao())
        label_else = self.new_label()
        label_end_if = self.new_label()

        self.emit(f"if_false {cond_temp} goto {label_else}")

        # Visit THEN block
        then_commands = [c for c in ctx.comando() if c.start.tokenIndex < (ctx.children[ctx.children.index(ctx.expressao()) + 2].getSymbol().tokenIndex if 'else' in [str(child) for child in ctx.children] else float('inf'))]
        for cmd_ctx in then_commands:
            self.visit(cmd_ctx)

        if len(ctx.comando()) > len(then_commands): # Check if there's an ELSE block
            self.emit(f"goto {label_end_if}")
            self.emit(f"label {label_else}")
            # Visit ELSE block
            else_commands = [c for c in ctx.comando() if c.start.tokenIndex >= (ctx.children[ctx.children.index(ctx.expressao()) + 2].getSymbol().tokenIndex + 1)] # Approximate index
            for cmd_ctx in else_commands:
                self.visit(cmd_ctx)
        else:
            self.emit(f"label {label_else}") # No else, so jump directly to end_if if false

        self.emit(f"label {label_end_if}")


    def visitForCmd(self, ctx: JavythonParser.ForCmdContext):
        label_loop_start = self.new_label()
        label_condition = self.new_label()
        label_end_for = self.new_label()

        # Initialization
        if ctx.atribuicaoFor():
            self.visit(ctx.atribuicaoFor(0))

        self.emit(f"label {label_condition}")

        # Condition
        cond_temp = self.visit(ctx.expressao())
        self.emit(f"if_false {cond_temp} goto {label_end_for}")

        # Body
        for comando_ctx in ctx.comando():
            self.visit(comando_ctx)

        # Increment/Decrement
        if ctx.incDecFor():
            self.visit(ctx.incDecFor())
        elif len(ctx.atribuicaoFor()) > 1: # Secondary assignment as increment
            self.visit(ctx.atribuicaoFor(1))

        self.emit(f"goto {label_condition}")
        self.emit(f"label {label_end_for}")

    def visitAtribuicaoFor(self, ctx: JavythonParser.AtribuicaoForContext):
        # Similar to visitAtribuicao, but for the FOR loop's assignment
        var_name = ctx.ID().getText()
        expr_result = self.visit(ctx.expressao())
        self.emit(f"{var_name} = {expr_result}")
        return var_name

    def visitIncDecFor(self, ctx: JavythonParser.IncDecForContext):
        var_name = ctx.ID().getText()
        op = '++' if ctx.getChild(1).getSymbol().type == JavythonParser.T__25 else '--' # Assuming T__25 is '++'
        temp = self.new_temp()
        if op == '++':
            self.emit(f"{temp} = {var_name} + 1")
        else:
            self.emit(f"{temp} = {var_name} - 1")
        self.emit(f"{var_name} = {temp}")
        return temp # Not strictly needed to return for increment, but consistent

    # --- Expressões ---
    def visitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        left = self.visit(ctx.expressao(0))
        right = self.visit(ctx.expressao(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        left = self.visit(ctx.expressao(0))
        right = self.visit(ctx.expressao(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        left = self.visit(ctx.expressao(0))
        right = self.visit(ctx.expressao(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        expr_result = self.visit(ctx.expressao())
        op = ctx.op.text
        temp = self.new_temp()
        self.emit(f"{temp} = {op}{expr_result}")
        return temp

    def visitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        return self.visit(ctx.expressao())

    def visitChamadaFuncao(self, ctx: JavythonParser.ChamadaFuncaoContext):
        func_name = ctx.ID().getText()
        args = []
        for expr_ctx in ctx.expressao():
            arg_temp = self.visit(expr_ctx)
            args.append(arg_temp)
            self.emit(f"param {arg_temp}")

        simbolo_metodo = self.tabela_simbolos.buscar(func_name)
        if simbolo_metodo and simbolo_metodo.tipo != "void":
            result_temp = self.new_temp()
            self.emit(f"{result_temp} = call {func_name}, {len(args)}")
            return result_temp
        else:
            self.emit(f"call {func_name}, {len(args)}")
            return "void_call" # Indicação de que não retorna valor

    # --- Átomos ---
    def visitIdAtom(self, ctx: JavythonParser.IdAtomContext):
        return ctx.getText()

    def visitIntAtom(self, ctx: JavythonParser.IntAtomContext):
        return ctx.getText()

    def visitRealAtom(self, ctx: JavythonParser.RealAtomContext):
        return ctx.getText()

    def visitStringAtom(self, ctx: JavythonParser.StringAtomContext):
        return ctx.getText()

    def visitBoolAtom(self, ctx: JavythonParser.BoolAtomContext):
        return ctx.getText()

    def visitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        return self.visit(ctx.chamadaFuncao())