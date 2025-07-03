# tac_generator.py (Versão Corrigida e Mais Robusta)

from antlr4.tree.Tree import TerminalNode
from JavythonParser import JavythonParser
from JavythonVisitor import JavythonVisitor
from tabela_simbolos import TabelaSimbolos


class TACGenerator(JavythonVisitor):
    def __init__(self, tabela_simbolos: TabelaSimbolos):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.tabela_simbolos = tabela_simbolos

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, instruction):
        self.instructions.append(instruction)

    def visitProgram(self, ctx: JavythonParser.ProgramContext):
        if ctx.decIds(): self.visit(ctx.decIds())
        for metodo_ctx in ctx.metodo(): self.visit(metodo_ctx)
        self.visit(ctx.main())
        return self.instructions

    def visitMetodo(self, ctx: JavythonParser.MetodoContext):
        method_name = ctx.ID().getText()
        self.emit(f"label {method_name}_entry")
        if ctx.decIds(): self.visit(ctx.decIds())
        for comando_ctx in ctx.comando(): self.visit(comando_ctx)
        simbolo_metodo = self.tabela_simbolos.buscar(method_name)
        if simbolo_metodo and simbolo_metodo.tipo == "void":
            if not self.instructions or not self.instructions[-1].strip().startswith("return"):
                self.emit("return")

    def visitMain(self, ctx: JavythonParser.MainContext):
        self.emit("label main_entry")
        if ctx.decIds(): self.visit(ctx.decIds())
        for comando_ctx in ctx.comando(): self.visit(comando_ctx)
        self.emit("return")

    def visitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        expr_result = self.visit(ctx.expressao())
        self.emit(f"{var_name} = {expr_result}")

    def visitReturnCmd(self, ctx: JavythonParser.ReturnCmdContext):
        if ctx.expressao():
            expr_result = self.visit(ctx.expressao())
            self.emit(f"return {expr_result}")
        else:
            self.emit("return")

    def visitInputCmd(self, ctx: JavythonParser.InputCmdContext):
        for id_node in ctx.idList().ID():
            self.emit(f"read {id_node.getText()}")

    def visitPrintCmd(self, ctx: JavythonParser.PrintCmdContext):
        # Itera sobre cada expressão dentro do print
        for i, expr_ctx in enumerate(ctx.expressao()):
            expr_result = self.visit(expr_ctx)
            # Evita imprimir "None" para chamadas de função void
            if expr_result is not None:
                self.emit(f"print {expr_result}")

        # Emite um comando para pular a linha ao final do comando print
        self.emit("println")

    # CORREÇÃO PRINCIPAL: Lógica robusta para IF/ELSE
    def visitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        cond_result = self.visit(ctx.expressao())

        # Procura pelo token 'else' para saber se é um if-then ou if-then-else
        else_node = None
        for child in ctx.children:
            if isinstance(child, TerminalNode) and child.getSymbol().text == 'else':
                else_node = child
                break

        if else_node:  # Estrutura IF-THEN-ELSE
            label_else = self.new_label()
            label_end = self.new_label()

            self.emit(f"if_false {cond_result} goto {label_else}")

            # Bloco THEN: comandos antes do 'else'
            for cmd in ctx.comando():
                if cmd.start.tokenIndex < else_node.getSymbol().tokenIndex:
                    self.visit(cmd)
            self.emit(f"goto {label_end}")

            # Bloco ELSE
            self.emit(f"label {label_else}")
            for cmd in ctx.comando():
                if cmd.start.tokenIndex > else_node.getSymbol().tokenIndex:
                    self.visit(cmd)
            self.emit(f"label {label_end}")

        else:  # Estrutura IF-THEN (sem else)
            label_end = self.new_label()
            self.emit(f"if_false {cond_result} goto {label_end}")

            # Bloco THEN
            for cmd in ctx.comando():
                self.visit(cmd)
            self.emit(f"label {label_end}")

    def visitForCmd(self, ctx: JavythonParser.ForCmdContext):
        label_cond = self.new_label()
        label_end = self.new_label()
        if ctx.atribuicaoFor(0): self.visit(ctx.atribuicaoFor(0))
        self.emit(f"label {label_cond}")
        if ctx.expressao():
            cond_result = self.visit(ctx.expressao())
            self.emit(f"if_false {cond_result} goto {label_end}")
        for comando_ctx in ctx.comando(): self.visit(comando_ctx)
        if len(ctx.atribuicaoFor()) > 1:
            self.visit(ctx.atribuicaoFor(1))
        elif ctx.incDecFor():
            self.visit(ctx.incDecFor())
        self.emit(f"goto {label_cond}")
        self.emit(f"label {label_end}")

    def visitAtribuicaoFor(self, ctx: JavythonParser.AtribuicaoForContext):
        # A regra de atribuição do For é semanticamente igual à atribuição normal
        self.visitAtribuicao(ctx)

    def visitIncDecFor(self, ctx: JavythonParser.IncDecForContext):
        var_name = ctx.ID().getText()
        op_symbol = '+' if ctx.getChild(1).getText() == '++' else '-'
        temp = self.new_temp()
        self.emit(f"{temp} = {var_name} {op_symbol} 1")
        self.emit(f"{var_name} = {temp}")

    def visitBinaryExpr(self, ctx):
        left = self.visit(ctx.expressao(0))
        right = self.visit(ctx.expressao(1))
        op = ctx.op.text
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        return self.visitBinaryExpr(ctx)

    def visitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        return self.visitBinaryExpr(ctx)

    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        return self.visitBinaryExpr(ctx)

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
        args = [self.visit(arg) for arg in ctx.expressao()]
        for arg_result in args:
            self.emit(f"param {arg_result}")
        simbolo = self.tabela_simbolos.buscar(func_name)
        if simbolo and simbolo.tipo != "void":
            result_temp = self.new_temp()
            self.emit(f"{result_temp} = call {func_name}, {len(args)}")
            return result_temp
        else:
            self.emit(f"call {func_name}, {len(args)}")
            return None

    def visitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        return self.visit(ctx.chamadaFuncao())

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