# Generated from ./TresEnderecos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TresEnderecosParser import TresEnderecosParser
else:
    from TresEnderecosParser import TresEnderecosParser

# This class defines a complete listener for a parse tree produced by TresEnderecosParser.
class TresEnderecosListener(ParseTreeListener):

    # Enter a parse tree produced by TresEnderecosParser#program.
    def enterProgram(self, ctx:TresEnderecosParser.ProgramContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#program.
    def exitProgram(self, ctx:TresEnderecosParser.ProgramContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#instrucoes.
    def enterInstrucoes(self, ctx:TresEnderecosParser.InstrucoesContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#instrucoes.
    def exitInstrucoes(self, ctx:TresEnderecosParser.InstrucoesContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#declaracaoVariavel.
    def enterDeclaracaoVariavel(self, ctx:TresEnderecosParser.DeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#declaracaoVariavel.
    def exitDeclaracaoVariavel(self, ctx:TresEnderecosParser.DeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#atribuicao.
    def enterAtribuicao(self, ctx:TresEnderecosParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#atribuicao.
    def exitAtribuicao(self, ctx:TresEnderecosParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#UnaryOp.
    def enterUnaryOp(self, ctx:TresEnderecosParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#UnaryOp.
    def exitUnaryOp(self, ctx:TresEnderecosParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#MulDiv.
    def enterMulDiv(self, ctx:TresEnderecosParser.MulDivContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#MulDiv.
    def exitMulDiv(self, ctx:TresEnderecosParser.MulDivContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#AddSub.
    def enterAddSub(self, ctx:TresEnderecosParser.AddSubContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#AddSub.
    def exitAddSub(self, ctx:TresEnderecosParser.AddSubContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#Parens.
    def enterParens(self, ctx:TresEnderecosParser.ParensContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#Parens.
    def exitParens(self, ctx:TresEnderecosParser.ParensContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#Id.
    def enterId(self, ctx:TresEnderecosParser.IdContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#Id.
    def exitId(self, ctx:TresEnderecosParser.IdContext):
        pass


    # Enter a parse tree produced by TresEnderecosParser#Int.
    def enterInt(self, ctx:TresEnderecosParser.IntContext):
        pass

    # Exit a parse tree produced by TresEnderecosParser#Int.
    def exitInt(self, ctx:TresEnderecosParser.IntContext):
        pass



del TresEnderecosParser