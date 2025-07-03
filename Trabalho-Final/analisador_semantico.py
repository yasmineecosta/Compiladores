# Trabalho-Final/analisador_semantico.py (Versão com validação de retorno)

from JavythonParser import JavythonParser
from JavythonListener import JavythonListener
from JavythonVisitor import JavythonVisitor
from tabela_simbolos import TabelaSimbolos, Simbolo


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

    def visitIntAtom(self, ctx):
        return "int"

    def visitRealAtom(self, ctx):
        return "real"

    def visitStringAtom(self, ctx):
        return "str"

    def visitBoolAtom(self, ctx):
        return "bool"

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

        for i, (arg_expr, param_info) in enumerate(zip(argumentos, parametros_esperados)):
            tipo_argumento = self.visit(arg_expr)
            tipo_parametro_esperado = param_info[0]
            nome_parametro = param_info[1]

            if tipo_argumento == "indefinido":
                continue

            is_compatible = (tipo_parametro_esperado == tipo_argumento) or \
                            (tipo_parametro_esperado == 'real' and tipo_argumento == 'int')

            if not is_compatible:
                self.reportar_erro(
                    arg_expr.start.line,
                    f"Tipo incompatível para o parâmetro '{nome_parametro}' na chamada da função '{nome_func}'. "
                    f"Esperado: '{tipo_parametro_esperado}', Recebido: '{tipo_argumento}'."
                )

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
            self.reportar_erro(ctx.start.line,
                               f"Operação aritmética inválida para os tipos '{tipo_esq}' e '{tipo_dir}'.")
            return "indefinido"
        return "real" if tipo_esq == "real" or tipo_dir == "real" else "int"

    def visitMulDivExpr(self, ctx):
        return self.visitAddSubExpr(ctx)

    def visitUnaryExpr(self, ctx):
        return self.visit(ctx.expressao())

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expressao())


# ===================================================================
class AnalisadorSemantico(JavythonListener):
    def __init__(self):
        self.tabela = TabelaSimbolos()
        self.erros = []
        self.expression_visitor = ExpressionTypeVisitor(self.tabela, self.erros)

        self.metodo_atual = None  # Controla o simbolo do metodo que estamos visitando
        self.simbolo_main = Simbolo('main', 'void', 'metodo')  # Cria um simbolo para o main

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
        if not self.tabela.declarar(simbolo):
            self.reportar_erro(linha, f"Redeclaração do método '{nome}'.")

        self.metodo_atual = simbolo  # Armazena o simbolo do metodo atual

        self.tabela.entrar_escopo(nome)
        for tipo, nome_param in parametros:
            self.tabela.declarar(Simbolo(nome_param, tipo, 'parametro', linha))

    def exitMetodo(self, ctx):
        self.metodo_atual = None  # Limpa a referencia ao sair do metodo
        self.tabela.sair_escopo()

    def enterMain(self, ctx):
        self.tabela.entrar_escopo("main")
        self.metodo_atual = self.simbolo_main  # Define o 'main' como metodo atual

    def exitMain(self, ctx):
        self.tabela.sair_escopo()
        self.metodo_atual = None  # Limpa a referencia ao sair do main

    def enterDecl(self, ctx):
        tipo = ctx.tipo().getText()
        for id_tok in ctx.idList().ID():
            nome = id_tok.getText()
            linha = id_tok.getSymbol().line
            if not self.tabela.declarar(Simbolo(nome, tipo, 'variavel', linha)):
                self.reportar_erro(linha, f"Redeclaração da variável '{nome}'.")

    def exitAtribuicao(self, ctx):
        nome_var = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome_var)
        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Variável '{nome_var}' não declarada.")
            return

        tipo_variavel = simbolo.tipo
        tipo_expressao = self.expression_visitor.visit(ctx.expressao())

        if tipo_expressao == "indefinido": return

        is_compatible = (tipo_variavel == tipo_expressao) or \
                        (tipo_variavel == 'real' and tipo_expressao == 'int')

        if not is_compatible:
            self.reportar_erro(ctx.start.line,
                               f"Atribuição incompatível. Não é possível converter de '{tipo_expressao}' para '{tipo_variavel}'.")

    def exitReturnCmd(self, ctx):
        if self.metodo_atual is None:
            self.reportar_erro(ctx.start.line, "Comando 'return' encontrado fora de um método ou do bloco main.")
            return

        tipo_retorno_esperado = self.metodo_atual.tipo

        # Caso 1: O método é 'void', mas o return possui um valor.
        if tipo_retorno_esperado == 'void':
            if ctx.expressao():  # Verifica se há uma expressão no retorno
                self.reportar_erro(ctx.start.line,
                                   f"Método '{self.metodo_atual.nome}' é 'void' e não pode retornar um valor.")
            return  # Se for void, não há mais nada a checar.

        # Caso 2: O método não é 'void', então o tipo do valor retornado deve ser compatível.
        tipo_valor_retornado = self.expression_visitor.visit(ctx.expressao())

        if tipo_valor_retornado == "indefinido":
            return  # Erro na expressão já foi reportado

        # Verifica a compatibilidade (permite int -> real)
        is_compatible = (tipo_retorno_esperado == tipo_valor_retornado) or \
                        (tipo_retorno_esperado == 'real' and tipo_valor_retornado == 'int')

        if not is_compatible:
            self.reportar_erro(
                ctx.start.line,
                f"Tipo de retorno incompatível para o método '{self.metodo_atual.nome}'. "
                f"Esperado: '{tipo_retorno_esperado}', mas o valor retornado é do tipo '{tipo_valor_retornado}'."
            )

    def exitPrintCmd(self, ctx):
        for e in ctx.expressao(): self.expression_visitor.visit(e)

    def exitInputCmd(self, ctx):
        for id_tok in ctx.idList().ID():
            nome = id_tok.getText()
            if not self.tabela.buscar(nome):
                self.reportar_erro(id_tok.getSymbol().line, f"Variável '{nome}' não declarada.")

    def exitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        self.expression_visitor.visit(ctx.expressao())

    def exitForCmd(self, ctx: JavythonParser.ForCmdContext):
        if ctx.atribuicaoFor(0): self.expression_visitor.visit(ctx.atribuicaoFor(0).expressao())
        if ctx.expressao(): self.expression_visitor.visit(ctx.expressao())
        if ctx.atribuicaoFor(1): self.expression_visitor.visit(ctx.atribuicaoFor(1).expressao())
        if ctx.incDecFor(): self.expression_visitor.visit(ctx.incDecFor())

    def exitWhileCmd(self, ctx: JavythonParser.WhileCmdContext):
        self.expression_visitor.visit(ctx.expressao())