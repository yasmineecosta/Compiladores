# Trabalho-Final/analisador_semantico.py (Versão Corrigida com Verificação de Parâmetros e Escopo Completo nas Estruturas de Controle)

from JavythonParser import JavythonParser
from JavythonListener import JavythonListener
from JavythonVisitor import JavythonVisitor
from tabela_simbolos import TabelaSimbolos, Simbolo

# ===================================================================
# Visitor dedicado a determinar o tipo de qualquer nó de expressão.
# ===================================================================
class ExpressionTypeVisitor(JavythonVisitor):
    def __init__(self, tabela: TabelaSimbolos, erros: list):
        self.tabela = tabela
        self.erros = erros

    def reportar_erro(self, linha, mensagem):
        erro_msg = f"Linha {linha}: {mensagem}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)

    def visitIdAtom(self, ctx):
        nome_var = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome_var)
        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Variável ou função '{nome_var}' não declarada.")
            return "indefinido"
        return simbolo.tipo

    def visitIntAtom(self, ctx): return "int"
    def visitRealAtom(self, ctx): return "real"
    def visitStringAtom(self, ctx): return "str"
    def visitBoolAtom(self, ctx): return "bool"

    def visitFuncCallExpr(self, ctx):
        nome_func = ctx.chamadaFuncao().ID().getText()
        simbolo = self.tabela.buscar(nome_func)
        if not simbolo or simbolo.categoria != 'metodo':
            self.reportar_erro(ctx.start.line, f"Função '{nome_func}' não declarada.")
            return "indefinido"

        argumentos = ctx.chamadaFuncao().expressao()
        parametros_esperados = simbolo.parametros if hasattr(simbolo, 'parametros') else []

        if len(argumentos) != len(parametros_esperados):
            self.reportar_erro(ctx.start.line,
                f"Função '{nome_func}' chamada com {len(argumentos)} argumento(s), mas espera {len(parametros_esperados)}.")

        for expr in argumentos:
            self.visit(expr)

        return simbolo.tipo

    def visitCompExpr(self, ctx):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if "indefinido" in [tipo_esq, tipo_dir]: return "indefinido"
        if tipo_esq != tipo_dir and not (tipo_esq in ["int", "real"] and tipo_dir in ["int", "real"]):
            self.reportar_erro(ctx.start.line, f"Comparação entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}'.")
        return "bool"

    def visitAddSubExpr(self, ctx):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if "indefinido" in [tipo_esq, tipo_dir]: return "indefinido"
        if tipo_esq not in ["int", "real"] or tipo_dir not in ["int", "real"]:
            self.reportar_erro(ctx.start.line, f"Operação aritmética inválida para os tipos '{tipo_esq}' e '{tipo_dir}'.")
            return "indefinido"
        return "real" if tipo_esq == "real" or tipo_dir == "real" else "int"

    def visitMulDivExpr(self, ctx): return self.visitAddSubExpr(ctx)
    def visitUnaryExpr(self, ctx): return self.visit(ctx.expressao())
    def visitParensExpr(self, ctx): return self.visit(ctx.expressao())

# ===================================================================
class AnalisadorSemantico(JavythonListener):
    def __init__(self):
        self.tabela = TabelaSimbolos()
        self.erros = []
        self.expression_visitor = ExpressionTypeVisitor(self.tabela, self.erros)
        self.tabela.declarar(Simbolo('input', 'void', 'metodo'))
        self.tabela.declarar(Simbolo('print', 'void', 'metodo'))

    def reportar_erro(self, linha, mensagem):
        erro_msg = f"Linha {linha}: {mensagem}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)

    def enterMetodo(self, ctx):
        nome = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        linha = ctx.ID().getSymbol().line
        parametros = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                parametros.append((p.tipo().getText(), p.ID().getText()))
        simbolo = Simbolo(nome, tipo_retorno, 'metodo', linha, parametros)
        self.tabela.declarar(simbolo)
        self.tabela.entrar_escopo(nome)
        for tipo, nome in parametros:
            self.tabela.declarar(Simbolo(nome, tipo, 'parametro', linha))

    def exitMetodo(self, ctx):
        self.tabela.sair_escopo()

    def enterMain(self, ctx): self.tabela.entrar_escopo("main")
    def exitMain(self, ctx): self.tabela.sair_escopo()

    def enterDecl(self, ctx):
        tipo = ctx.tipo().getText()
        for id_tok in ctx.idList().ID():
            nome = id_tok.getText()
            linha = id_tok.getSymbol().line
            if not self.tabela.declarar(Simbolo(nome, tipo, 'variavel', linha)):
                self.reportar_erro(linha, f"Redeclaração da variável '{nome}'.")

    def exitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome)
        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Variável '{nome}' não declarada.")
            return
        tipo_expr = self.expression_visitor.visit(ctx.expressao())
        if tipo_expr == "indefinido": return
        if simbolo.tipo != tipo_expr and not (simbolo.tipo in ["int", "real"] and tipo_expr in ["int", "real"]):
            self.reportar_erro(ctx.start.line, f"Tipo incompatível: '{nome}' é '{simbolo.tipo}' mas recebeu '{tipo_expr}'.")

    def exitReturnCmd(self, ctx):
        self.expression_visitor.visit(ctx.expressao())

    def exitPrintCmd(self, ctx):
        for e in ctx.expressao(): self.expression_visitor.visit(e)

    def exitInputCmd(self, ctx):
        for id_tok in ctx.idList().ID():
            nome = id_tok.getText()
            if not self.tabela.buscar(nome):
                self.reportar_erro(id_tok.getSymbol().line, f"Variável '{nome}' não declarada.")

    def exitExpressao(self, ctx):
        # This method in the listener is triggered for every 'expressao' rule exit.
        # It's already calling the visitor, which should handle the ID lookup.
        # The issue is likely that control flow commands have their own 'exit' methods
        # and might not be triggering the `exitExpressao` for their conditions,
        # or the order of operations in the walker might be causing issues.
        pass # The visitor should handle the actual expression checking.

    # Updated methods for control flow structures to ensure expression validation
    def exitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        # Validate the condition expression
        self.expression_visitor.visit(ctx.expressao())
        # The commands within the if/else blocks will be visited by the walker naturally

    def exitForCmd(self, ctx: JavythonParser.ForCmdContext):
        # The 'atribuicaoFor' and 'incDecFor' contexts will already be handled by their respective exit methods
        # We need to explicitly visit the condition expression.
        if ctx.expressao(): # The condition can be empty
            self.expression_visitor.visit(ctx.expressao())

    def exitWhileCmd(self, ctx: JavythonParser.WhileCmdContext):
        # Validate the condition expression
        self.expression_visitor.visit(ctx.expressao())
        # The commands within the while block will be visited by the walker naturally