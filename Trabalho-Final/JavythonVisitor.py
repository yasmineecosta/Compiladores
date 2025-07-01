# Generated from Javython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JavythonParser import JavythonParser
else:
    from JavythonParser import JavythonParser

# This class defines a complete generic visitor for a parse tree produced by JavythonParser.

class JavythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavythonParser#program.
    def visitProgram(self, ctx:JavythonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#main.
    def visitMain(self, ctx:JavythonParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#decIds.
    def visitDecIds(self, ctx:JavythonParser.DecIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#decl.
    def visitDecl(self, ctx:JavythonParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#idList.
    def visitIdList(self, ctx:JavythonParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#tipo.
    def visitTipo(self, ctx:JavythonParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#metodo.
    def visitMetodo(self, ctx:JavythonParser.MetodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#parametros.
    def visitParametros(self, ctx:JavythonParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#parametro.
    def visitParametro(self, ctx:JavythonParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#returnCmd.
    def visitReturnCmd(self, ctx:JavythonParser.ReturnCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#comando.
    def visitComando(self, ctx:JavythonParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#atribuicao.
    def visitAtribuicao(self, ctx:JavythonParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#inputCmd.
    def visitInputCmd(self, ctx:JavythonParser.InputCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#printCmd.
    def visitPrintCmd(self, ctx:JavythonParser.PrintCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#breakCmd.
    def visitBreakCmd(self, ctx:JavythonParser.BreakCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#ifCmd.
    def visitIfCmd(self, ctx:JavythonParser.IfCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#whileCmd.
    def visitWhileCmd(self, ctx:JavythonParser.WhileCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#forCmd.
    def visitForCmd(self, ctx:JavythonParser.ForCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#atribuicaoFor.
    def visitAtribuicaoFor(self, ctx:JavythonParser.AtribuicaoForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#incDecFor.
    def visitIncDecFor(self, ctx:JavythonParser.IncDecForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#RealAtom.
    def visitRealAtom(self, ctx:JavythonParser.RealAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:JavythonParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#StringAtom.
    def visitStringAtom(self, ctx:JavythonParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#BoolAtom.
    def visitBoolAtom(self, ctx:JavythonParser.BoolAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#ParensExpr.
    def visitParensExpr(self, ctx:JavythonParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#CompExpr.
    def visitCompExpr(self, ctx:JavythonParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:JavythonParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#IntAtom.
    def visitIntAtom(self, ctx:JavythonParser.IntAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:JavythonParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#IdAtom.
    def visitIdAtom(self, ctx:JavythonParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:JavythonParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#incremento.
    def visitIncremento(self, ctx:JavythonParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#decremento.
    def visitDecremento(self, ctx:JavythonParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavythonParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:JavythonParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)



del JavythonParser