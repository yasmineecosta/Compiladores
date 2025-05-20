# Generated from Javython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JavythonParser import JavythonParser
else:
    from JavythonParser import JavythonParser

# This class defines a complete listener for a parse tree produced by JavythonParser.
class JavythonListener(ParseTreeListener):

    # Enter a parse tree produced by JavythonParser#program.
    def enterProgram(self, ctx:JavythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by JavythonParser#program.
    def exitProgram(self, ctx:JavythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by JavythonParser#main.
    def enterMain(self, ctx:JavythonParser.MainContext):
        pass

    # Exit a parse tree produced by JavythonParser#main.
    def exitMain(self, ctx:JavythonParser.MainContext):
        pass


    # Enter a parse tree produced by JavythonParser#decIds.
    def enterDecIds(self, ctx:JavythonParser.DecIdsContext):
        pass

    # Exit a parse tree produced by JavythonParser#decIds.
    def exitDecIds(self, ctx:JavythonParser.DecIdsContext):
        pass


    # Enter a parse tree produced by JavythonParser#decl.
    def enterDecl(self, ctx:JavythonParser.DeclContext):
        pass

    # Exit a parse tree produced by JavythonParser#decl.
    def exitDecl(self, ctx:JavythonParser.DeclContext):
        pass


    # Enter a parse tree produced by JavythonParser#idList.
    def enterIdList(self, ctx:JavythonParser.IdListContext):
        pass

    # Exit a parse tree produced by JavythonParser#idList.
    def exitIdList(self, ctx:JavythonParser.IdListContext):
        pass


    # Enter a parse tree produced by JavythonParser#tipo.
    def enterTipo(self, ctx:JavythonParser.TipoContext):
        pass

    # Exit a parse tree produced by JavythonParser#tipo.
    def exitTipo(self, ctx:JavythonParser.TipoContext):
        pass


    # Enter a parse tree produced by JavythonParser#metodo.
    def enterMetodo(self, ctx:JavythonParser.MetodoContext):
        pass

    # Exit a parse tree produced by JavythonParser#metodo.
    def exitMetodo(self, ctx:JavythonParser.MetodoContext):
        pass


    # Enter a parse tree produced by JavythonParser#parametros.
    def enterParametros(self, ctx:JavythonParser.ParametrosContext):
        pass

    # Exit a parse tree produced by JavythonParser#parametros.
    def exitParametros(self, ctx:JavythonParser.ParametrosContext):
        pass


    # Enter a parse tree produced by JavythonParser#parametro.
    def enterParametro(self, ctx:JavythonParser.ParametroContext):
        pass

    # Exit a parse tree produced by JavythonParser#parametro.
    def exitParametro(self, ctx:JavythonParser.ParametroContext):
        pass


    # Enter a parse tree produced by JavythonParser#returnCmd.
    def enterReturnCmd(self, ctx:JavythonParser.ReturnCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#returnCmd.
    def exitReturnCmd(self, ctx:JavythonParser.ReturnCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#comando.
    def enterComando(self, ctx:JavythonParser.ComandoContext):
        pass

    # Exit a parse tree produced by JavythonParser#comando.
    def exitComando(self, ctx:JavythonParser.ComandoContext):
        pass


    # Enter a parse tree produced by JavythonParser#atribuicao.
    def enterAtribuicao(self, ctx:JavythonParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by JavythonParser#atribuicao.
    def exitAtribuicao(self, ctx:JavythonParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by JavythonParser#inputCmd.
    def enterInputCmd(self, ctx:JavythonParser.InputCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#inputCmd.
    def exitInputCmd(self, ctx:JavythonParser.InputCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#printCmd.
    def enterPrintCmd(self, ctx:JavythonParser.PrintCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#printCmd.
    def exitPrintCmd(self, ctx:JavythonParser.PrintCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#breakCmd.
    def enterBreakCmd(self, ctx:JavythonParser.BreakCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#breakCmd.
    def exitBreakCmd(self, ctx:JavythonParser.BreakCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#ifCmd.
    def enterIfCmd(self, ctx:JavythonParser.IfCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#ifCmd.
    def exitIfCmd(self, ctx:JavythonParser.IfCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#whileCmd.
    def enterWhileCmd(self, ctx:JavythonParser.WhileCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#whileCmd.
    def exitWhileCmd(self, ctx:JavythonParser.WhileCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#forCmd.
    def enterForCmd(self, ctx:JavythonParser.ForCmdContext):
        pass

    # Exit a parse tree produced by JavythonParser#forCmd.
    def exitForCmd(self, ctx:JavythonParser.ForCmdContext):
        pass


    # Enter a parse tree produced by JavythonParser#strExpr.
    def enterStrExpr(self, ctx:JavythonParser.StrExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#strExpr.
    def exitStrExpr(self, ctx:JavythonParser.StrExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#intExpr.
    def enterIntExpr(self, ctx:JavythonParser.IntExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#intExpr.
    def exitIntExpr(self, ctx:JavythonParser.IntExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#relacional.
    def enterRelacional(self, ctx:JavythonParser.RelacionalContext):
        pass

    # Exit a parse tree produced by JavythonParser#relacional.
    def exitRelacional(self, ctx:JavythonParser.RelacionalContext):
        pass


    # Enter a parse tree produced by JavythonParser#boolFalse.
    def enterBoolFalse(self, ctx:JavythonParser.BoolFalseContext):
        pass

    # Exit a parse tree produced by JavythonParser#boolFalse.
    def exitBoolFalse(self, ctx:JavythonParser.BoolFalseContext):
        pass


    # Enter a parse tree produced by JavythonParser#chamada.
    def enterChamada(self, ctx:JavythonParser.ChamadaContext):
        pass

    # Exit a parse tree produced by JavythonParser#chamada.
    def exitChamada(self, ctx:JavythonParser.ChamadaContext):
        pass


    # Enter a parse tree produced by JavythonParser#realExpr.
    def enterRealExpr(self, ctx:JavythonParser.RealExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#realExpr.
    def exitRealExpr(self, ctx:JavythonParser.RealExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#grupo.
    def enterGrupo(self, ctx:JavythonParser.GrupoContext):
        pass

    # Exit a parse tree produced by JavythonParser#grupo.
    def exitGrupo(self, ctx:JavythonParser.GrupoContext):
        pass


    # Enter a parse tree produced by JavythonParser#addSub.
    def enterAddSub(self, ctx:JavythonParser.AddSubContext):
        pass

    # Exit a parse tree produced by JavythonParser#addSub.
    def exitAddSub(self, ctx:JavythonParser.AddSubContext):
        pass


    # Enter a parse tree produced by JavythonParser#igualdade.
    def enterIgualdade(self, ctx:JavythonParser.IgualdadeContext):
        pass

    # Exit a parse tree produced by JavythonParser#igualdade.
    def exitIgualdade(self, ctx:JavythonParser.IgualdadeContext):
        pass


    # Enter a parse tree produced by JavythonParser#mulDiv.
    def enterMulDiv(self, ctx:JavythonParser.MulDivContext):
        pass

    # Exit a parse tree produced by JavythonParser#mulDiv.
    def exitMulDiv(self, ctx:JavythonParser.MulDivContext):
        pass


    # Enter a parse tree produced by JavythonParser#boolTrue.
    def enterBoolTrue(self, ctx:JavythonParser.BoolTrueContext):
        pass

    # Exit a parse tree produced by JavythonParser#boolTrue.
    def exitBoolTrue(self, ctx:JavythonParser.BoolTrueContext):
        pass


    # Enter a parse tree produced by JavythonParser#unaryMinus.
    def enterUnaryMinus(self, ctx:JavythonParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by JavythonParser#unaryMinus.
    def exitUnaryMinus(self, ctx:JavythonParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by JavythonParser#unaryNot.
    def enterUnaryNot(self, ctx:JavythonParser.UnaryNotContext):
        pass

    # Exit a parse tree produced by JavythonParser#unaryNot.
    def exitUnaryNot(self, ctx:JavythonParser.UnaryNotContext):
        pass


    # Enter a parse tree produced by JavythonParser#idExpr.
    def enterIdExpr(self, ctx:JavythonParser.IdExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#idExpr.
    def exitIdExpr(self, ctx:JavythonParser.IdExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#incremento.
    def enterIncremento(self, ctx:JavythonParser.IncrementoContext):
        pass

    # Exit a parse tree produced by JavythonParser#incremento.
    def exitIncremento(self, ctx:JavythonParser.IncrementoContext):
        pass


    # Enter a parse tree produced by JavythonParser#decremento.
    def enterDecremento(self, ctx:JavythonParser.DecrementoContext):
        pass

    # Exit a parse tree produced by JavythonParser#decremento.
    def exitDecremento(self, ctx:JavythonParser.DecrementoContext):
        pass


    # Enter a parse tree produced by JavythonParser#chamadaFuncao.
    def enterChamadaFuncao(self, ctx:JavythonParser.ChamadaFuncaoContext):
        pass

    # Exit a parse tree produced by JavythonParser#chamadaFuncao.
    def exitChamadaFuncao(self, ctx:JavythonParser.ChamadaFuncaoContext):
        pass



del JavythonParser