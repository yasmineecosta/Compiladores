# jasmin_generator.py (Versão Final Corrigida e Completa)

from JavythonParser import JavythonParser
from JavythonVisitor import JavythonVisitor
from analisador_semantico import AnalisadorSemantico
from tabela_simbolos import TabelaSimbolos, Simbolo


class JasminGenerator(JavythonVisitor):
    """
    Este visitor percorre a AST e gera o código de montagem Jasmin para a JVM.
    """

    def __init__(self, analisador: AnalisadorSemantico):
        self.code = []
        self.analisador = analisador
        self.tabela = analisador.tabela
        self.expression_visitor = analisador.expression_visitor
        self.label_count = 0

        self.class_name = ""
        self.current_method_return_type = ""
        self.var_map = {}
        self.var_count = 0

    def new_label(self, hint=""):
        self.label_count += 1
        return f"L{self.label_count}_{hint}"

    def new_var(self, var_name, is_param=False):
        if var_name not in self.var_map:
            if self.current_method_return_type == "" and self.var_count == 0:  # Metodo Main
                self.var_count = 1
            self.var_map[var_name] = self.var_count
            self.var_count += 1
        return self.var_map[var_name]

    def _get_type_descriptor(self, type_name):
        type_map = {"int": "I", "real": "F", "bool": "Z", "str": "Ljava/lang/String;", "void": "V"}
        return type_map.get(type_name, "Ljava/lang/Object;")

    def _get_method_descriptor(self, metodo_simbolo):
        param_types = "".join([self._get_type_descriptor(p[0]) for p in metodo_simbolo.parametros])
        return_type = self._get_type_descriptor(metodo_simbolo.tipo)
        return f"({param_types}){return_type}"

    # --- Estrutura Principal do Programa ---

    def visitProgram(self, ctx: JavythonParser.ProgramContext):
        self.class_name = ctx.ID().getText()
        self.code.append(f".class public {self.class_name}")
        self.code.append(".super java/lang/Object")

        if ctx.decIds():
            for decl in ctx.decIds().decl():
                tipo = self._get_type_descriptor(decl.tipo().getText())
                for var in decl.idList().ID():
                    self.code.append(f".field public static {var.getText()} {tipo}")

        self.code.append("\n; Construtor padrao (obrigatorio)")
        self.code.append(".method public <init>()V")
        self.code.append("   aload_0")
        self.code.append("   invokespecial java/lang/Object/<init>()V")
        self.code.append("   return")
        self.code.append(".end method\n")

        for metodo_ctx in ctx.metodo(): self.visit(metodo_ctx)
        self.visit(ctx.main())

        return "\n".join(self.code)

    def visitMain(self, ctx: JavythonParser.MainContext):
        self.tabela.entrar_escopo("main")
        self.var_map, self.var_count = {}, 0
        self.current_method_return_type = "void"

        self.code.append("; Metodo principal")
        self.code.append(".method public static main([Ljava/lang/String;)V")

        stack_limit_pos = len(self.code)
        self.code.append("   .limit stack 99")
        locals_limit_pos = len(self.code)
        self.code.append("   .limit locals 99")

        if ctx.decIds(): self.visit(ctx.decIds())
        for cmd in ctx.comando(): self.visit(cmd)

        self.code.append("   return")
        self.code.append(".end method")
        self.code[locals_limit_pos] = f"   .limit locals {self.var_count if self.var_count > 0 else 1}"
        self.tabela.sair_escopo()

    def visitMetodo(self, ctx: JavythonParser.MetodoContext):
        nome = ctx.ID().getText()
        self.tabela.entrar_escopo(nome)
        self.var_map, self.var_count = {}, 0

        simbolo = self.tabela.buscar(nome)
        if not simbolo: return

        self.current_method_return_type = simbolo.tipo
        descritor = self._get_method_descriptor(simbolo)

        self.code.append(f"\n.method public static {nome}{descritor}")
        stack_pos, locals_pos = len(self.code), len(self.code) + 1
        self.code.extend(["   .limit stack 99", "   .limit locals 99"])

        if ctx.parametros(): self.visit(ctx.parametros())
        if ctx.decIds(): self.visit(ctx.decIds())
        for cmd in ctx.comando(): self.visit(cmd)

        if simbolo.tipo == 'void': self.code.append("   return")

        self.code.append(".end method")
        self.code[locals_pos] = f"   .limit locals {self.var_count if self.var_count > 0 else 1}"
        self.tabela.sair_escopo()

    def visitParametros(self, ctx: JavythonParser.ParametrosContext):
        for param in ctx.parametro(): self.new_var(param.ID().getText(), is_param=True)

    def visitDecl(self, ctx: JavythonParser.DeclContext):
        for id_node in ctx.idList().ID(): self.new_var(id_node.getText())

    # --- Comandos ---

    def visitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        var_name, simbolo = ctx.ID().getText(), self.tabela.buscar(ctx.ID().getText())
        if not simbolo: return

        self.visit(ctx.expressao())

        if simbolo.categoria in ['variavel', 'parametro']:
            var_index = self.var_map.get(var_name)
            if simbolo.tipo in ['int', 'bool']:
                self.code.append(f"   istore {var_index}")
            elif simbolo.tipo == 'real':
                self.code.append(f"   fstore {var_index}")
            else:
                self.code.append(f"   astore {var_index}")
        else:
            tipo_desc = self._get_type_descriptor(simbolo.tipo)
            self.code.append(f"   putstatic {self.class_name}/{var_name} {tipo_desc}")

    def visitPrintCmd(self, ctx: JavythonParser.PrintCmdContext):
        for expr in ctx.expressao():
            self.code.append("   getstatic java/lang/System/out Ljava/io/PrintStream;")
            tipo_expr = self.expression_visitor.visit(expr)
            descritor = self._get_type_descriptor(tipo_expr)
            self.visit(expr)
            self.code.append(f"   invokevirtual java/io/PrintStream/println({descritor})V")

        # jasmin_generator.py

        # ... (resto do seu código)

    def visitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        label_else = self.new_label("else")
        label_endif = self.new_label("endif")
        expr_ctx = ctx.expressao()

        # Otimização: Gera saltos condicionais diretamente, evitando booleanos intermediários.
        if isinstance(expr_ctx, JavythonParser.CompExprContext):
            self.visit(expr_ctx.expressao(0))  # Empilha o valor da esquerda
            self.visit(expr_ctx.expressao(1))  # Empilha o valor da direita

            # Mapa de operadores para a instrução de salto OPOSTA
            # (Ex: para '>', saltamos se for '<=')
            op_map_inverso = {
                '==': 'if_icmpne',  # Salta se não for igual
                '!=': 'if_icmpeq',  # Salta se for igual
                '>': 'if_icmple',  # Salta se for menor ou igual
                '<': 'if_icmpge'  # Salta se for maior ou igual
                # Adicione 'if_icmplt' para '>=' e 'if_icmpgt' para '<=' se os tiver na sua linguagem
            }

            op = expr_ctx.op.text
            if op in op_map_inverso:
                self.code.append(f"   {op_map_inverso[op]} {label_else}")
            else:
                # Fallback para outros operadores ou erro
                self.reportar_erro(ctx.start.line, f"Operador de comparação '{op}' não suportado.")
                return
        else:
            # Fallback para expressões que já resultam em um booleano (0 ou 1)
            self.visit(expr_ctx)
            self.code.append(f"   ifeq {label_else}")

        # --- Geração dos blocos THEN e ELSE (seu código para isso parece correto) ---

        # Lógica para separar os comandos dos blocos then/else
        all_commands = ctx.comando()
        then_commands = []
        else_commands = []
        else_node = next((child for child in ctx.children if child.getText() == 'else'), None)

        if else_node:
            for cmd in all_commands:
                if cmd.getSourceInterval()[0] < else_node.getSourceInterval()[0]:
                    then_commands.append(cmd)
                else:
                    else_commands.append(cmd)
        else:
            then_commands = all_commands

        # Gera o código para o bloco THEN
        for cmd in then_commands:
            self.visit(cmd)

        # Se houver um bloco ELSE, pule por cima dele
        if else_commands:
            self.code.append(f"   goto {label_endif}")

        # Gera o label do ELSE (é o destino do ifeq ou if_icmpX)
        self.code.append(f"{label_else}:")

        # Gera o código para o bloco ELSE
        if else_commands:
            for cmd in else_commands:
                self.visit(cmd)
            # Marca o fim do if-else
            self.code.append(f"{label_endif}:")

    def visitWhileCmd(self, ctx: JavythonParser.WhileCmdContext):
        label_start, label_end = self.new_label("while_start"), self.new_label("while_end")
        self.code.append(f"{label_start}:")
        self.visit(ctx.expressao())
        self.code.append(f"   ifeq {label_end}")
        for cmd in ctx.comando(): self.visit(cmd)
        self.code.append(f"   goto {label_start}")
        self.code.append(f"{label_end}:")

    def visitForCmd(self, ctx: JavythonParser.ForCmdContext):
        label_start, label_end = self.new_label("for_start"), self.new_label("for_end")
        if ctx.atribuicaoFor(0): self.visit(ctx.atribuicaoFor(0))

        self.code.append(f"{label_start}:")
        if ctx.expressao():
            self.visit(ctx.expressao())
            self.code.append(f"   ifeq {label_end}")

        for cmd in ctx.comando(): self.visit(cmd)
        if len(ctx.atribuicaoFor()) > 1:
            self.visit(ctx.atribuicaoFor(1))
        elif ctx.incDecFor():
            self.visit(ctx.incDecFor())
        self.code.append(f"   goto {label_start}")
        self.code.append(f"{label_end}:")

    def visitReturnCmd(self, ctx: JavythonParser.ReturnCmdContext):
        if ctx.expressao():
            self.visit(ctx.expressao())
            rt = self.current_method_return_type
            if rt in ['int', 'bool']:
                self.code.append("   ireturn")
            elif rt == 'real':
                self.code.append("   freturn")
            else:
                self.code.append("   areturn")
        else:
            self.code.append("   return")

    def visitAtribuicaoFor(self, ctx: JavythonParser.AtribuicaoForContext):
        self.visitAtribuicao(ctx)

    def visitIncremento(self, ctx: JavythonParser.IncrementoContext):
        var_index = self.var_map.get(ctx.ID().getText())
        self.code.append(f"   iinc {var_index} 1")

    def visitDecremento(self, ctx: JavythonParser.DecrementoContext):
        var_index = self.var_map.get(ctx.ID().getText())
        self.code.append(f"   iinc {var_index} -1")

    # --- Expressoes e Atomos ---

    def visitIdAtom(self, ctx: JavythonParser.IdAtomContext):
        var_name, simbolo = ctx.getText(), self.tabela.buscar(ctx.getText())
        if not simbolo: return

        if simbolo.categoria in ['variavel', 'parametro']:
            var_index = self.var_map.get(var_name)
            if simbolo.tipo in ['int', 'bool']:
                self.code.append(f"   iload {var_index}")
            elif simbolo.tipo == 'real':
                self.code.append(f"   fload {var_index}")
            else:
                self.code.append(f"   aload {var_index}")
        else:
            tipo_desc = self._get_type_descriptor(simbolo.tipo)
            self.code.append(f"   getstatic {self.class_name}/{var_name} {tipo_desc}")

    def visitIntAtom(self, ctx: JavythonParser.IntAtomContext):
        valor = int(ctx.getText())
        if -1 <= valor <= 5:
            self.code.append(f"   iconst_{'m1' if valor == -1 else valor}")
        elif -128 <= valor <= 127:
            self.code.append(f"   bipush {valor}")
        else:
            self.code.append(f"   ldc {valor}")

    def visitRealAtom(self, ctx: JavythonParser.RealAtomContext):
        self.code.append(f"   ldc {float(ctx.getText())}")

    def visitStringAtom(self, ctx: JavythonParser.StringAtomContext):
        self.code.append(f"   ldc {ctx.getText()}")

    def visitBoolAtom(self, ctx: JavythonParser.BoolAtomContext):
        self.code.append("   iconst_1" if ctx.getText() == 'true' else "   iconst_0")

    def visitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        return self.visit(ctx.expressao())

    def visitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        self.visit(ctx.expressao(0));
        self.visit(ctx.expressao(1))
        self.code.append("   iadd" if ctx.op.text == '+' else "   isub")

    def visitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        self.visit(ctx.expressao(0));
        self.visit(ctx.expressao(1))
        self.code.append("   imul" if ctx.op.text == '*' else "   idiv")

    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        label_true, label_end = self.new_label("comp_true"), self.new_label("comp_end")
        self.visit(ctx.expressao(0));
        self.visit(ctx.expressao(1))
        op_map = {'==': 'if_icmpeq', '!=': 'if_icmpne', '>': 'if_icmpgt', '<': 'if_icmplt'}
        self.code.append(f"   {op_map.get(ctx.op.text)} {label_true}")
        self.code.extend([f"   iconst_0", f"   goto {label_end}", f"{label_true}:", "   iconst_1", f"{label_end}:"])

    def visitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        self.visit(ctx.expressao())
        if ctx.op.text == '-':
            self.code.append("   ineg")
        elif ctx.op.text == '!':
            self.code.extend(["   iconst_1", "   ixor"])

    def visitChamadaFuncao(self, ctx: JavythonParser.ChamadaFuncaoContext):
        nome_funcao = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome_funcao)
        if not simbolo: return

        descritor = self._get_method_descriptor(simbolo)
        for arg in ctx.expressao(): self.visit(arg)
        self.code.append(f"   invokestatic {self.class_name}/{nome_funcao}{descritor}")

    def visitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        return self.visit(ctx.chamadaFuncao())