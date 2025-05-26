# Generated from ./TresEnderecos.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,41,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,49,8,4,10,4,12,4,52,9,4,1,4,0,1,8,5,0,
        2,4,6,8,0,2,1,0,6,7,1,0,4,5,55,0,13,1,0,0,0,2,20,1,0,0,0,4,22,1,
        0,0,0,6,26,1,0,0,0,8,40,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,
        1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,
        16,17,5,0,0,1,17,1,1,0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,0,
        0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,10,0,0,24,25,
        5,2,0,0,25,5,1,0,0,0,26,27,5,10,0,0,27,28,5,3,0,0,28,29,3,8,4,0,
        29,30,5,2,0,0,30,7,1,0,0,0,31,32,6,4,-1,0,32,33,7,0,0,0,33,41,3,
        8,4,4,34,41,5,10,0,0,35,41,5,11,0,0,36,37,5,8,0,0,37,38,3,8,4,0,
        38,39,5,9,0,0,39,41,1,0,0,0,40,31,1,0,0,0,40,34,1,0,0,0,40,35,1,
        0,0,0,40,36,1,0,0,0,41,50,1,0,0,0,42,43,10,6,0,0,43,44,7,1,0,0,44,
        49,3,8,4,7,45,46,10,5,0,0,46,47,7,0,0,0,47,49,3,8,4,6,48,42,1,0,
        0,0,48,45,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,9,
        1,0,0,0,52,50,1,0,0,0,5,13,20,40,48,50
    ]

class TresEnderecosParser ( Parser ):

    grammarFileName = "TresEnderecos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "';'", "'='", "'*'", "'/'", 
                     "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "SEMI", "EQUAL", "MUL", "DIV", 
                      "ADD", "SUB", "LPAREN", "RPAREN", "ID", "INT", "WS" ]

    RULE_program = 0
    RULE_instrucoes = 1
    RULE_declaracaoVariavel = 2
    RULE_atribuicao = 3
    RULE_expr = 4

    ruleNames =  [ "program", "instrucoes", "declaracaoVariavel", "atribuicao", 
                   "expr" ]

    EOF = Token.EOF
    NUMBER=1
    SEMI=2
    EQUAL=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    LPAREN=8
    RPAREN=9
    ID=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TresEnderecosParser.EOF, 0)

        def instrucoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TresEnderecosParser.InstrucoesContext)
            else:
                return self.getTypedRuleContext(TresEnderecosParser.InstrucoesContext,i)


        def getRuleIndex(self):
            return TresEnderecosParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = TresEnderecosParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==10:
                self.state = 10
                self.instrucoes()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(TresEnderecosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoVariavel(self):
            return self.getTypedRuleContext(TresEnderecosParser.DeclaracaoVariavelContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(TresEnderecosParser.AtribuicaoContext,0)


        def getRuleIndex(self):
            return TresEnderecosParser.RULE_instrucoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucoes" ):
                listener.enterInstrucoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucoes" ):
                listener.exitInstrucoes(self)




    def instrucoes(self):

        localctx = TresEnderecosParser.InstrucoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucoes)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.declaracaoVariavel()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.atribuicao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoVariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(TresEnderecosParser.NUMBER, 0)

        def ID(self):
            return self.getToken(TresEnderecosParser.ID, 0)

        def SEMI(self):
            return self.getToken(TresEnderecosParser.SEMI, 0)

        def getRuleIndex(self):
            return TresEnderecosParser.RULE_declaracaoVariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoVariavel" ):
                listener.enterDeclaracaoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoVariavel" ):
                listener.exitDeclaracaoVariavel(self)




    def declaracaoVariavel(self):

        localctx = TresEnderecosParser.DeclaracaoVariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracaoVariavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(TresEnderecosParser.NUMBER)
            self.state = 23
            self.match(TresEnderecosParser.ID)
            self.state = 24
            self.match(TresEnderecosParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TresEnderecosParser.ID, 0)

        def EQUAL(self):
            return self.getToken(TresEnderecosParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(TresEnderecosParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TresEnderecosParser.SEMI, 0)

        def getRuleIndex(self):
            return TresEnderecosParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = TresEnderecosParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(TresEnderecosParser.ID)
            self.state = 27
            self.match(TresEnderecosParser.EQUAL)
            self.state = 28
            self.expr(0)
            self.state = 29
            self.match(TresEnderecosParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TresEnderecosParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TresEnderecosParser.ExprContext,0)

        def ADD(self):
            return self.getToken(TresEnderecosParser.ADD, 0)
        def SUB(self):
            return self.getToken(TresEnderecosParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TresEnderecosParser.ExprContext)
            else:
                return self.getTypedRuleContext(TresEnderecosParser.ExprContext,i)

        def MUL(self):
            return self.getToken(TresEnderecosParser.MUL, 0)
        def DIV(self):
            return self.getToken(TresEnderecosParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TresEnderecosParser.ExprContext)
            else:
                return self.getTypedRuleContext(TresEnderecosParser.ExprContext,i)

        def ADD(self):
            return self.getToken(TresEnderecosParser.ADD, 0)
        def SUB(self):
            return self.getToken(TresEnderecosParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(TresEnderecosParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(TresEnderecosParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(TresEnderecosParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TresEnderecosParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TresEnderecosParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TresEnderecosParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TresEnderecosParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                localctx = TresEnderecosParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.expr(4)
                pass
            elif token in [10]:
                localctx = TresEnderecosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(TresEnderecosParser.ID)
                pass
            elif token in [11]:
                localctx = TresEnderecosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(TresEnderecosParser.INT)
                pass
            elif token in [8]:
                localctx = TresEnderecosParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(TresEnderecosParser.LPAREN)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(TresEnderecosParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = TresEnderecosParser.MulDivContext(self, TresEnderecosParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 43
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = TresEnderecosParser.AddSubContext(self, TresEnderecosParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(6)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




