# Gerado a partir de ./TresEnderecos.g4 pelo ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from TresEnderecosParser import TresEnderecosParser
else:
    from TresEnderecosParser import TresEnderecosParser

class TresEnderecosListener(ParseTreeListener):

    def __init__(self):
        self.temp_count = 0 #contador de temporários,
        self.code = []      # Armazena as instruções geradas
        self.values = {}    # Mapeia nós da AST para valores intermediários

    # Função auxiliar para criar novos variaveis temporários
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    # =====================
    # Métodos de Programa
    # =====================

    # Inicializa estruturas de dados ao entrar no programa
    def enterProgram(self, ctx: TresEnderecosParser.ProgramContext):
        self.code.clear()
        self.temp_count = -1
        self.values.clear()

    # Imprime o código gerado ao sair do programa
    def exitProgram(self, ctx: TresEnderecosParser.ProgramContext):
        print("\n".join(self.code))

    # =========================
    # Métodos 'exit'
    # =========================

    # Saindo da regra instrucoes // Declarações não geram código no destino
    def exitInstrucoes(self, ctx: TresEnderecosParser.InstrucoesContext):
        pass

    # Saindo da declaração de variável // Declarações não geram código no destino
    def exitDeclaracaoVariavel(self, ctx: TresEnderecosParser.DeclaracaoVariavelContext):
        pass

    # Atribuição: id = expr;
    def exitAtribuicao(self, ctx: TresEnderecosParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        expr_node = ctx.expr()
        expr_val = self.values[expr_node]
        self.code.append(f"{var_name} = {expr_val}")



    # Métodos de Expressões

    # Gera código para operações unárias:  "t = -expr"
    def exitUnaryOp(self, ctx: TresEnderecosParser.UnaryOpContext):
        # expr_node = ctx.expr()
        # expr_val = self.values[expr_node]
        # op = ctx.op.text
        # temp = self.new_temp()
        # self.code.append(f"{temp} = {op}{expr_val}")
        # self.values[ctx] = temp

        """Gera código para operações unárias (minus e plus)"""
        expr_val = self.values[ctx.expr()]  # Obtém o valor da expressão
        op = ctx.op.text                    # Obtém o operador ('+' ou '-')

        if op == '+':
            temp = self.new_temp()
            self.code.append(f"{temp} = plus {expr_val}")
            self.values[ctx] = temp
        else:
            temp = self.new_temp()
            self.code.append(f"{temp} = minus {expr_val}")
            self.values[ctx] = temp


    # Gera código para multiplicação/divisão: "t = left * right"
    def exitMulDiv(self, ctx: TresEnderecosParser.MulDivContext):
        left_val = self.values[ctx.expr(0)]
        right_val = self.values[ctx.expr(1)]
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    # Gera código para adição/subtração: "t = left + right"
    def exitAddSub(self, ctx: TresEnderecosParser.AddSubContext):
        left_val = self.values[ctx.expr(0)]
        right_val = self.values[ctx.expr(1)]
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    # Propaga valor de expressões entre parênteses
    def exitParens(self, ctx: TresEnderecosParser.ParensContext):
        self.values[ctx] = self.values[ctx.expr()]

    # Registra identificadores: valor é o próprio nome
    def exitId(self, ctx: TresEnderecosParser.IdContext):
        self.values[ctx] = ctx.ID().getText()

    # Registra valores inteiros:  valor é o próprio número
    def exitInt(self, ctx: TresEnderecosParser.IntContext):
        self.values[ctx] = ctx.INT().getText()

    # =========================
    # Métodos 'enter'
    # =========================
    # Métodos 'enter' são chamados ao ENTRAR em cada regra.
    # Como não precisamos fazer nada antes, deixamos 'pass'.

    # Entrando na regra instrucoes
    def enterInstrucoes(self, ctx: TresEnderecosParser.InstrucoesContext):
        pass

    # Entrando na declaração de variável
    def enterDeclaracaoVariavel(self, ctx: TresEnderecosParser.DeclaracaoVariavelContext):
        pass

    # Entrando na atribuição
    def enterAtribuicao(self, ctx: TresEnderecosParser.AtribuicaoContext):
        pass

    # Entrando na operação unária
    def enterUnaryOp(self, ctx: TresEnderecosParser.UnaryOpContext):
        pass

    # Entrando na multiplicação ou divisão
    def enterMulDiv(self, ctx: TresEnderecosParser.MulDivContext):
        pass

    # Entrando na adição ou subtração
    def enterAddSub(self, ctx: TresEnderecosParser.AddSubContext):
        pass

    # Entrando nos parênteses
    def enterParens(self, ctx: TresEnderecosParser.ParensContext):
        pass

    # Entrando no identificador
    def enterId(self, ctx: TresEnderecosParser.IdContext):
        pass

    # Entrando no número inteiro
    def enterInt(self, ctx: TresEnderecosParser.IntContext):
        pass

del TresEnderecosParser
