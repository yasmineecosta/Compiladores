# jasmin_generator.py (Versão Final Refatorada e Completa)
# jasmin_generator.py (Versão Corrigida e Funcional)

from JavythonParser import JavythonParser
from JavythonVisitor import JavythonVisitor
from analisador_semantico import AnalisadorSemantico, ExpressionTypeVisitor


class JasminGenerator(JavythonVisitor):
    def __init__(self, analisador: AnalisadorSemantico):
        self.code = []
        self.analisador = analisador
        self.tabela = analisador.tabela
        self.expression_visitor = ExpressionTypeVisitor(self.tabela, [])
        self.label_count = 0
        self.class_name = ""
        self.current_method = None
        self.var_map = {}
        self.var_count = 0

    def new_label(self, hint=""):
        self.label_count += 1
        return f"L{self.label_count}_{hint}"

    def get_var_index(self, var_name):
        if var_name not in self.var_map:
            if self.current_method and self.current_method.nome == 'main' and not self.var_map:
                self.var_count = 1
            self.var_map[var_name] = self.var_count
            self.var_count += 1
        return self.var_map[var_name]

    def get_type_descriptor(self, type_name):
        type_map = {"int": "I", "real": "F", "bool": "Z", "str": "Ljava/lang/String;", "void": "V"}
        return type_map.get(type_name, f"L{type_name};")

    def visitProgram(self, ctx: JavythonParser.ProgramContext):
        self.class_name = ctx.ID().getText()
        self.code.append(f".class public {self.class_name}")
        self.code.append(".super java/lang/Object\n")
        self.code.append(".method public <init>()V")
        self.code.append("   aload_0")
        self.code.append("   invokespecial java/lang/Object/<init>()V")
        self.code.append("   return")
        self.code.append(".end method\n")

        self.visit(ctx.main())
        return "\n".join(self.code)

    def visitMain(self, ctx: JavythonParser.MainContext):
        self.tabela.entrar_escopo("main")
        self.current_method = self.analisador.simbolo_main
        self.var_map, self.var_count = {}, 0

        self.code.append(".method public static main([Ljava/lang/String;)V")
        stack_limit_pos = len(self.code)
        self.code.append("   .limit stack 99")
        locals_limit_pos = len(self.code)
        self.code.append("   .limit locals 99")

        if ctx.decIds(): self.visit(ctx.decIds())
        for cmd in ctx.comando(): self.visit(cmd)  # <-- Esta linha processa todos os comandos

        self.code.append("   return")
        self.code.append(".end method")
        self.code[locals_limit_pos] = f"   .limit locals {max(1, self.var_count)}"
        self.tabela.sair_escopo()

    def visitDecl(self, ctx: JavythonParser.DeclContext):
        for id_node in ctx.idList().ID(): self.get_var_index(id_node.getText())

    def visitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        var_name, simbolo = ctx.ID().getText(), self.tabela.buscar(ctx.ID().getText())
        if not simbolo: return

        self.visit(ctx.expressao())
        var_index = self.get_var_index(var_name)
        store_map = {"int": "istore", "bool": "istore", "real": "fstore", "str": "astore"}
        self.code.append(f"   {store_map.get(simbolo.tipo, 'astore')} {var_index}")

    def visitPrintCmd(self, ctx: JavythonParser.PrintCmdContext):
        for expr in ctx.expressao():
            self.code.append("   getstatic java/lang/System/out Ljava/io/PrintStream;")
            tipo_expr = self.expression_visitor.visit(expr)
            descritor = self.get_type_descriptor(tipo_expr)
            self.visit(expr)
            self.code.append(f"   invokevirtual java/io/PrintStream/println({descritor})V")

    def visitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        label_else, label_endif = self.new_label("else"), self.new_label("endif")

        # Gera o código para a condição do IF
        self.visit(ctx.expressao())
        # se o valor na pilha for 0 (false), salta para o bloco else
        self.code.append(f"   ifeq {label_else}")

        # Bloco THEN: identifica os comandos que pertencem ao 'if'
        then_commands = [cmd for cmd in ctx.comando() if cmd.getRuleIndex() != JavythonParser.RULE_ifCmd or (
            cmd.start.tokenIndex < ctx.getChild(4).start.tokenIndex if 'else' in [c.getText() for c in
                                                                                  ctx.children] else True)]
        # Itera pelos nós filhos para executar o bloco 'then'
        for i in range(ctx.children.index(ctx.getChild(4)) + 1, len(ctx.children)):
            child = ctx.children[i]
            if child.getText() == 'else':
                break
            if isinstance(child, JavythonParser.ComandoContext):
                self.visit(child)

        # Se existe um bloco 'else', adiciona um salto para pular o código do else
        else_node = next((child for child in ctx.children if child.getText() == 'else'), None)
        if else_node:
            self.code.append(f"   goto {label_endif}")

        self.code.append(f"{label_else}:")

        # Bloco ELSE: Se houver um 'else', visita os comandos dele
        if else_node:
            else_start_index = ctx.children.index(else_node)
            for i in range(else_start_index + 1, len(ctx.children)):
                child = ctx.children[i]
                if isinstance(child, JavythonParser.ComandoContext):
                    self.visit(child)
            self.code.append(f"{label_endif}:")

    def visitIdAtom(self, ctx: JavythonParser.IdAtomContext):
        simbolo = self.tabela.buscar(ctx.getText())
        if not simbolo: return
        var_index = self.get_var_index(simbolo.nome)
        load_map = {"int": "iload", "bool": "iload", "real": "fload", "str": "aload"}
        self.code.append(f"   {load_map.get(simbolo.tipo, 'aload')} {var_index}")

    def visitIntAtom(self, ctx: JavythonParser.IntAtomContext):
        valor = int(ctx.getText())
        if -1 <= valor <= 5:
            self.code.append(f"   iconst_{'m1' if valor == -1 else valor}")
        else:
            self.code.append(f"   ldc {valor}")

    def visitStringAtom(self, ctx: JavythonParser.StringAtomContext):
        self.code.append(f"   ldc {ctx.getText()}")

    def visitBoolAtom(self, ctx: JavythonParser.BoolAtomContext):
        self.code.append("   iconst_1" if ctx.getText().lower() == 'true' else "   iconst_0")

    def visitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        return self.visit(ctx.expressao())

    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        label_true, label_end = self.new_label("comp_true"), self.new_label("comp_end")
        
        tipo_esq = self.expression_visitor.visit(ctx.expressao(0))
        tipo_dir = self.expression_visitor.visit(ctx.expressao(1))

        self.visit(ctx.expressao(0))
        if tipo_esq == 'int' and tipo_dir == 'real': self.code.append("   i2f")
            
        self.visit(ctx.expressao(1))
        if tipo_dir == 'int' and tipo_esq == 'real': self.code.append("   i2f")

        op_map_int = {'==': 'if_icmpeq', '!=': 'if_icmpne', '>': 'if_icmpgt', '<': 'if_icmplt'}
        op_map_float = {'==': 'fcmpl\n   ifne', '!=': 'fcmpl\n   ifeq', '>': 'fcmpl\n   iflt', '<': 'fcmpg\n   ifgt'}
        op_map_ref = {'==': 'if_acmpeq', '!=': 'if_acmpne'}

        jump_instruction = ""
        if tipo_esq in ['int', 'bool']:
            jump_instruction = op_map_int.get(ctx.op.text)
        elif tipo_esq == 'real' or tipo_dir == 'real':
            jump_instruction = op_map_float.get(ctx.op.text)
        else: # str
            jump_instruction = op_map_ref.get(ctx.op.text)
            
        if jump_instruction:
            self.code.append(f"   {jump_instruction} {label_true}")

        self.code.append("   iconst_0")
        self.code.append(f"   goto {label_end}")
        self.code.append(f"{label_true}:")
        self.code.append("   iconst_1")
        self.code.append(f"{label_end}:")