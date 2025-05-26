from antlr4 import *
if "." in __name__:
    from .TresEnderecosParser import TresEnderecosParser
else:
    from TresEnderecosParser import TresEnderecosParser

class TresEnderecosListener(ParseTreeListener):
    def __init__(self):
        self.temp_count = 0
        self.code = []
        self.values = {}

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    # Programa
    def enterProgram(self, ctx:TresEnderecosParser.ProgramContext):
        self.code.clear()
        self.temp_count = -1
        self.values.clear()

    def exitProgram(self, ctx:TresEnderecosParser.ProgramContext):
        print("\n".join(self.code))


    def enterDeclaracaoVariavel(self, ctx:TresEnderecosParser.DeclaracaoVariavelContext):
        pass

    def exitDeclaracaoVariavel(self, ctx:TresEnderecosParser.DeclaracaoVariavelContext):
        pass

    # Atribuição: id = expr;
    def exitAtribuicao(self, ctx:TresEnderecosParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        expr_node = ctx.expr()
        expr_val = self.values[expr_node]
        self.code.append(f"{var_name} = {expr_val}")

    # Expressões:
    def exitAddSub(self, ctx:TresEnderecosParser.AddSubContext):
        left = ctx.expr(0)
        right = ctx.expr(1)
        left_val = self.values[left]
        right_val = self.values[right]
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    def exitMulDiv(self, ctx:TresEnderecosParser.MulDivContext):
        left = ctx.expr(0)
        right = ctx.expr(1)
        left_val = self.values[left]
        right_val = self.values[right]
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {left_val} {op} {right_val}")
        self.values[ctx] = temp

    def exitUnaryOp(self, ctx:TresEnderecosParser.UnaryOpContext):
        expr_node = ctx.expr()
        expr_val = self.values[expr_node]
        op = ctx.op.text
        temp = self.new_temp()
        self.code.append(f"{temp} = {op}{expr_val}")
        self.values[ctx] = temp

    def exitId(self, ctx:TresEnderecosParser.IdContext):
        self.values[ctx] = ctx.ID().getText()

    def exitInt(self, ctx:TresEnderecosParser.IntContext):
        self.values[ctx] = ctx.INT().getText()

    def exitParens(self, ctx:TresEnderecosParser.ParensContext):
        self.values[ctx] = self.values[ctx.expr()]


del TresEnderecosParser