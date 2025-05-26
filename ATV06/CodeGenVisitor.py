from TresEnderecosParser import TresEnderecosParser
from TresEnderecosParserVisitor import TresEnderecosParserVisitor

class CodeGenVisitor(TresEnderecosParserVisitor):
    def __init__(self):
        self.temp_count = 0
        self.variables = set()

    def new_temp(self):
        t = f"t{self.temp_count}"
        self.temp_count += 1
        return t

    def visitDeclaracaoVariavel(self, ctx:TresEnderecosParser.DeclaracaoVariavelContext):
        var_name = ctx.ID().getText()
        self.variables.add(var_name)
        # Não gera código para declaração aqui
        return None

    def visitAtribuicao(self, ctx:TresEnderecosParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        expr_result = self.visit(ctx.expr())
        print(f"{var_name} = {expr_result};")
        return var_name

    def visitId(self, ctx:TresEnderecosParser.IdContext):
        return ctx.ID().getText()

    def visitInt(self, ctx:TresEnderecosParser.IntContext):
        return ctx.INT().getText()

    def visitParens(self, ctx:TresEnderecosParser.ParensContext):
        return self.visit(ctx.expr())

    def visitUnaryOp(self, ctx:TresEnderecosParser.UnaryOpContext):
        operand = self.visit(ctx.expr())
        temp = self.new_temp()
        op = ctx.op.text
        print(f"{temp} = {op}{operand};")
        return temp

    def visitMulDiv(self, ctx:TresEnderecosParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.op.text
        print(f"{temp} = {left} {op} {right};")
        return temp

    def visitAddSub(self, ctx:TresEnderecosParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        temp = self.new_temp()
        op = ctx.op.text
        print(f"{temp} = {left} {op} {right};")
        return temp

    def visitPrograma(self, ctx:TresEnderecosParser.ProgramaContext):
        for instr in ctx.instrucoes():
            self.visit(instr)
        return None
