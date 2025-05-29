from antlr4 import *

from TresEnderecosParser import TresEnderecosParser
from TresEnderecosListener import TresEnderecosListener


class ErroSemantico(Exception):
    """
    Exceção lançada na primeira ocorrência de erro semântico,
    contendo mensagem e localização (linha e coluna).
    """
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.__str__())

    def __str__(self):
        loc = f" (linha {self.line}, coluna {self.column})" if self.line and self.column else ""
        return f"{self.message}{loc}"


class TresEnderecosSemantico(TresEnderecosListener):
    """
    Classe que estende TresEnderecosListener para realizar verificações semânticas
    e gerar código intermediário.
    """
    def __init__(self):
        super().__init__()
        self.temp_count = 0       # Contador de temporários
        self.code = []            # Armazena as instruções geradas
        self.values = {}          # mapeia nós da árvore para valores temporários
        self.tabela_simbolos = {} # Tabela de símbolos para variáveis

    # Função auxiliar para criar variáveis temporárias
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    # ================
    # Métodos do programa
    # ================

    def enterProgram(self, ctx: TresEnderecosParser.ProgramContext):
        """
        Inicializa estruturas de dados ao entrar no programa.
        """
        self.code.clear()
        self.temp_count = -1
        self.values.clear()
        self.tabela_simbolos.clear()

    def exitProgram(self, ctx: TresEnderecosParser.ProgramContext):
        """
        Imprime o código gerado ao sair do programa.
        """
        print("\nCódigo intermediário gerado:")
        print("\n".join(self.code))

    # ================
    # Declarações
    # ================
    def exitDeclaracaoVariavel(self, ctx: TresEnderecosParser.DeclaracaoVariavelContext):
        """
        Trata declarações de variáveis, adicionando-as à tabela de símbolos.
        """
        var_name = ctx.ID().getText()
        if var_name in self.tabela_simbolos:
            token = ctx.ID().getSymbol()
            raise ErroSemantico(f"Erro: Variável '{var_name}' já declarada.", token.line, token.column)
        else:
            self.tabela_simbolos[var_name] = None

    # ===========
    # Atribuição
    # ===========
    def exitAtribuicao(self, ctx: TresEnderecosParser.AtribuicaoContext):
        """
        Trata atribuições, gerando código intermediário e verificando se a variável foi declarada.
        """
        var_name = ctx.ID().getText()
        if var_name not in self.tabela_simbolos:
            token = ctx.ID().getSymbol()
            raise ErroSemantico(f"Erro: Variável '{var_name}' não declarada.", token.line, token.column)

        expr_node = ctx.expr()
        expr_val = self.values.get(expr_node)

        if expr_val is None:
            token = ctx.start
            raise ErroSemantico(f"Erro: Expressão inválida na atribuição de '{var_name}'.", token.line, token.column)

        self.code.append(f"{var_name} = {expr_val}")

    # ================
    # Expressões
    # ================
    def exitUnaryOp(self, ctx: TresEnderecosParser.UnaryOpContext):
        """
        Gera código para operações unárias (plus e minus).
        """
        expr_val = self.values.get(ctx.expr())
        if expr_val is None:
            token = ctx.start
            raise ErroSemantico("Erro: Expressão inválida em operação unária.", token.line, token.column)

        op = ctx.op.text
        temp = self.new_temp()

        if op == '+':
            self.code.append(f"{temp} = plus {expr_val}")
        else:
            self.code.append(f"{temp} = minus {expr_val}")

        self.values[ctx] = temp

    def exitMulDiv(self, ctx: TresEnderecosParser.MulDivContext):
        """
        Gera código para multiplicação e divisão.
        """
        left_val = self.values.get(ctx.expr(0))
        right_val = self.values.get(ctx.expr(1))

        if left_val is None or right_val is None:
            token = ctx.start
            raise ErroSemantico("Erro: Expressão inválida em multiplicação/divisão.", token.line, token.column)

        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    def exitAddSub(self, ctx: TresEnderecosParser.AddSubContext):
        """
        Gera código para adição e subtração.
        """
        left_val = self.values.get(ctx.expr(0))
        right_val = self.values.get(ctx.expr(1))

        if left_val is None or right_val is None:
            token = ctx.start
            raise ErroSemantico("Erro: Expressão inválida em adição/subtração.", token.line, token.column)

        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    def exitParens(self, ctx: TresEnderecosParser.ParensContext):
        """
        Propaga o valor de expressões entre parênteses.
        """
        expr_val = self.values.get(ctx.expr())
        if expr_val is None:
            token = ctx.start
            raise ErroSemantico("Erro: Expressão inválida entre parênteses.", token.line, token.column)
        self.values[ctx] = expr_val

    def exitId(self, ctx: TresEnderecosParser.IdContext):
        """
        Registra identificadores, armazenando seu nome.
        """
        var_name = ctx.ID().getText()
        if var_name not in self.tabela_simbolos:
            token = ctx.ID().getSymbol()
            raise ErroSemantico(f"Erro: Variável '{var_name}' não declarada.", token.line, token.column)
        self.values[ctx] = var_name

    def exitInt(self, ctx: TresEnderecosParser.IntContext):
        """
        Registra valores inteiros, armazenando o próprio número.
        """
        int_value = ctx.INT().getText()
        self.values[ctx] = int_value
