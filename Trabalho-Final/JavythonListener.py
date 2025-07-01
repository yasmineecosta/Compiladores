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


    # Enter a parse tree produced by JavythonParser#atribuicaoFor.
    def enterAtribuicaoFor(self, ctx:JavythonParser.AtribuicaoForContext):
        pass

    # Exit a parse tree produced by JavythonParser#atribuicaoFor.
    def exitAtribuicaoFor(self, ctx:JavythonParser.AtribuicaoForContext):
        pass


    # Enter a parse tree produced by JavythonParser#incDecFor.
    def enterIncDecFor(self, ctx:JavythonParser.IncDecForContext):
        pass

    # Exit a parse tree produced by JavythonParser#incDecFor.
    def exitIncDecFor(self, ctx:JavythonParser.IncDecForContext):
        pass


    # Enter a parse tree produced by JavythonParser#RealAtom.
    def enterRealAtom(self, ctx:JavythonParser.RealAtomContext):
        pass

    # Exit a parse tree produced by JavythonParser#RealAtom.
    def exitRealAtom(self, ctx:JavythonParser.RealAtomContext):
        pass


    # Enter a parse tree produced by JavythonParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:JavythonParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:JavythonParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#StringAtom.
    def enterStringAtom(self, ctx:JavythonParser.StringAtomContext):
        pass

    # Exit a parse tree produced by JavythonParser#StringAtom.
    def exitStringAtom(self, ctx:JavythonParser.StringAtomContext):
        pass


    # Enter a parse tree produced by JavythonParser#BoolAtom.
    def enterBoolAtom(self, ctx:JavythonParser.BoolAtomContext):
        pass

    # Exit a parse tree produced by JavythonParser#BoolAtom.
    def exitBoolAtom(self, ctx:JavythonParser.BoolAtomContext):
        pass


    # Enter a parse tree produced by JavythonParser#ParensExpr.
    def enterParensExpr(self, ctx:JavythonParser.ParensExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#ParensExpr.
    def exitParensExpr(self, ctx:JavythonParser.ParensExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#CompExpr.
    def enterCompExpr(self, ctx:JavythonParser.CompExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#CompExpr.
    def exitCompExpr(self, ctx:JavythonParser.CompExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:JavythonParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:JavythonParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#IntAtom.
    def enterIntAtom(self, ctx:JavythonParser.IntAtomContext):
        pass

    # Exit a parse tree produced by JavythonParser#IntAtom.
    def exitIntAtom(self, ctx:JavythonParser.IntAtomContext):
        pass


    # Enter a parse tree produced by JavythonParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:JavythonParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:JavythonParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by JavythonParser#IdAtom.
    def enterIdAtom(self, ctx:JavythonParser.IdAtomContext):
        pass

    # Exit a parse tree produced by JavythonParser#IdAtom.
    def exitIdAtom(self, ctx:JavythonParser.IdAtomContext):
        pass


    # Enter a parse tree produced by JavythonParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:JavythonParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by JavythonParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:JavythonParser.FuncCallExprContext):
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