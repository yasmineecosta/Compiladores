# Trabalho-Final/analisador_semantico.py (Versão 100% Completa)

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

    # --- Átomos (folhas da árvore de expressão) ---
    def visitIdAtom(self, ctx: JavythonParser.IdAtomContext):
        nome_var = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome_var)
        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Variável ou função '{nome_var}' não declarada.")
            return "indefinido"
        return simbolo.tipo

    def visitIntAtom(self, ctx: JavythonParser.IntAtomContext):
        return "int"

    def visitRealAtom(self, ctx: JavythonParser.RealAtomContext):
        return "real"

    def visitStringAtom(self, ctx: JavythonParser.StringAtomContext):
        return "str"

    def visitBoolAtom(self, ctx: JavythonParser.BoolAtomContext):
        return "bool"

    def visitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        nome_func = ctx.chamadaFuncao().ID().getText()
        simbolo = self.tabela.buscar(nome_func)
        if not simbolo or simbolo.categoria != 'metodo':
            self.reportar_erro(ctx.start.line, f"Função '{nome_func}' não declarada.")
            return "indefinido"
        return simbolo.tipo

    # --- Expressões Compostas ---
    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if tipo_esq != tipo_dir and not (tipo_esq in ["int", "real"] and tipo_dir in ["int", "real"]):
            self.reportar_erro(ctx.start.line, f"Comparação entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}'.")
        return "bool"

    def visitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if "indefinido" in [tipo_esq, tipo_dir]: return "indefinido"
        if tipo_esq not in ["int", "real"] or tipo_dir not in ["int", "real"]:
            self.reportar_erro(ctx.start.line,
                               f"Operação aritmética inválida para os tipos '{tipo_esq}' e '{tipo_dir}'.")
            return "indefinido"
        return "real" if tipo_esq == "real" or tipo_dir == "real" else "int"

    def visitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        return self.visitAddSubExpr(ctx)

    def visitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        return self.visit(ctx.expressao())

    def visitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        return self.visit(ctx.expressao())


# ===================================================================
# Listener principal para gerenciamento de escopo e regras semânticas
# ===================================================================
class AnalisadorSemantico(JavythonListener):
    def __init__(self):
        """
        Este é o construtor que estava em falta. Ele inicializa
        a tabela de símbolos e a lista de erros.
        """
        self.tabela = TabelaSimbolos()
        self.erros = []
        self.expression_visitor = ExpressionTypeVisitor(self.tabela, self.erros)

        # Adiciona funções nativas ao escopo global
        self.tabela.declarar(Simbolo(nome='input', tipo='void', categoria='metodo'))
        self.tabela.declarar(Simbolo(nome='print', tipo='void', categoria='metodo'))

    def reportar_erro(self, linha, mensagem):
        erro_msg = f"Linha {linha}: {mensagem}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)

    def enterMetodo(self, ctx: JavythonParser.MetodoContext):
        nome = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        linha = ctx.ID().getSymbol().line

        simbolo_metodo = Simbolo(nome=nome, tipo=tipo_retorno, categoria='metodo', linha=linha)
        if not self.tabela.declarar(simbolo_metodo):
            self.reportar_erro(linha, f"Identificador '{nome}' já declarado no escopo global.")

        self.tabela.entrar_escopo()

        if ctx.parametros():
            for param_ctx in ctx.parametros().parametro():
                nome_param = param_ctx.ID().getText()
                tipo_param = param_ctx.tipo().getText()
                linha_param = param_ctx.ID().getSymbol().line
                simbolo_param = Simbolo(nome=nome_param, tipo=tipo_param, categoria='parametro', linha=linha_param)
                if not self.tabela.declarar(simbolo_param):
                    self.reportar_erro(linha_param, f"Parâmetro '{nome_param}' já foi declarado neste escopo.")

    def exitMetodo(self, ctx: JavythonParser.MetodoContext):
        self.tabela.sair_escopo()

    def enterMain(self, ctx: JavythonParser.MainContext):
        self.tabela.entrar_escopo("main")

    def exitMain(self, ctx: JavythonParser.MainContext):
        self.tabela.sair_escopo()

    def exitDecl(self, ctx: JavythonParser.DeclContext):
        tipo = ctx.tipo().getText()
        for id_node in ctx.idList().ID():
            nome_var = id_node.getText()
            linha = id_node.getSymbol().line
            simbolo = Simbolo(nome=nome_var, tipo=tipo, categoria='variavel', linha=linha)
            if not self.tabela.declarar(simbolo):
                self.reportar_erro(linha, f"Variável '{nome_var}' já foi declarada.")

    def exitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        nome_var = ctx.ID().getText()
        linha = ctx.ID().getSymbol().line
        simbolo = self.tabela.buscar(nome_var)
        if not simbolo:
            self.reportar_erro(linha, f"Variável '{nome_var}' não declarada.")
            return

        tipo_expr = self.expression_visitor.visit(ctx.expressao())
        if tipo_expr == "indefinido": return

        tipos_compativeis = (simbolo.tipo == tipo_expr) or (simbolo.tipo == "real" and tipo_expr == "int")
        if not tipos_compativeis:
            self.reportar_erro(linha,
                               f"Atribuição de tipo incompatível para '{nome_var}'. Esperado '{simbolo.tipo}', mas recebeu '{tipo_expr}'.")

    def exitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        tipo_teste = self.expression_visitor.visit(ctx.expressao())
        if tipo_teste != "bool" and tipo_teste != "indefinido":
            self.reportar_erro(ctx.expressao().start.line,
                               f"A condição do 'if' deve ser booleana, mas é do tipo '{tipo_teste}'.")