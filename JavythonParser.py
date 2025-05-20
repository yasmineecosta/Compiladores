# Generated from ./Javython.g4 by ANTLR 4.13.2
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
        4,1,44,286,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,0,1,0,1,0,5,0,51,8,0,10,0,12,0,54,9,
        0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,62,8,1,1,1,5,1,65,8,1,10,1,12,1,68,
        9,1,1,2,1,2,1,2,1,2,1,2,4,2,75,8,2,11,2,12,2,76,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,5,4,86,8,4,10,4,12,4,89,9,4,1,5,1,5,1,6,1,6,1,6,1,6,
        3,6,97,8,6,1,6,1,6,1,6,3,6,102,8,6,1,6,5,6,105,8,6,10,6,12,6,108,
        9,6,1,6,3,6,111,8,6,1,6,1,6,1,7,1,7,1,7,5,7,118,8,7,10,7,12,7,121,
        9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,140,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,5,13,158,8,13,10,
        13,12,13,161,9,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,175,8,15,10,15,12,15,178,9,15,1,15,1,15,1,15,1,
        15,5,15,184,8,15,10,15,12,15,187,9,15,1,15,3,15,190,8,15,1,16,1,
        16,1,16,1,16,1,16,1,16,5,16,198,8,16,10,16,12,16,201,9,16,1,16,1,
        16,1,17,1,17,1,17,3,17,208,8,17,1,17,3,17,211,8,17,1,17,1,17,1,17,
        1,17,3,17,217,8,17,1,17,1,17,1,17,5,17,222,8,17,10,17,12,17,225,
        9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,245,8,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,259,8,18,10,18,12,18,
        262,9,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,5,21,277,8,21,10,21,12,21,280,9,21,3,21,282,8,21,1,21,
        1,21,1,21,0,1,36,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,0,5,1,0,8,12,1,0,28,29,2,0,27,27,30,30,1,0,31,32,
        1,0,33,34,308,0,44,1,0,0,0,2,58,1,0,0,0,4,69,1,0,0,0,6,78,1,0,0,
        0,8,82,1,0,0,0,10,90,1,0,0,0,12,92,1,0,0,0,14,114,1,0,0,0,16,122,
        1,0,0,0,18,125,1,0,0,0,20,139,1,0,0,0,22,141,1,0,0,0,24,146,1,0,
        0,0,26,152,1,0,0,0,28,165,1,0,0,0,30,168,1,0,0,0,32,191,1,0,0,0,
        34,204,1,0,0,0,36,244,1,0,0,0,38,263,1,0,0,0,40,267,1,0,0,0,42,271,
        1,0,0,0,44,45,5,1,0,0,45,46,5,2,0,0,46,47,5,39,0,0,47,48,5,3,0,0,
        48,52,3,4,2,0,49,51,3,12,6,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,
        0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,3,2,1,0,56,
        57,5,4,0,0,57,1,1,0,0,0,58,59,5,5,0,0,59,61,5,2,0,0,60,62,3,4,2,
        0,61,60,1,0,0,0,61,62,1,0,0,0,62,66,1,0,0,0,63,65,3,20,10,0,64,63,
        1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,3,1,0,0,0,68,
        66,1,0,0,0,69,70,5,6,0,0,70,74,5,2,0,0,71,72,3,6,3,0,72,73,5,3,0,
        0,73,75,1,0,0,0,74,71,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,5,1,0,0,0,78,79,3,8,4,0,79,80,5,2,0,0,80,81,3,10,5,0,
        81,7,1,0,0,0,82,87,5,39,0,0,83,84,5,7,0,0,84,86,5,39,0,0,85,83,1,
        0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,9,1,0,0,0,89,
        87,1,0,0,0,90,91,7,0,0,0,91,11,1,0,0,0,92,93,3,10,5,0,93,94,5,39,
        0,0,94,96,5,13,0,0,95,97,3,14,7,0,96,95,1,0,0,0,96,97,1,0,0,0,97,
        98,1,0,0,0,98,99,5,14,0,0,99,101,5,15,0,0,100,102,3,4,2,0,101,100,
        1,0,0,0,101,102,1,0,0,0,102,106,1,0,0,0,103,105,3,20,10,0,104,103,
        1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,110,
        1,0,0,0,108,106,1,0,0,0,109,111,3,18,9,0,110,109,1,0,0,0,110,111,
        1,0,0,0,111,112,1,0,0,0,112,113,5,16,0,0,113,13,1,0,0,0,114,119,
        3,16,8,0,115,116,5,7,0,0,116,118,3,16,8,0,117,115,1,0,0,0,118,121,
        1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,15,1,0,0,0,121,119,1,
        0,0,0,122,123,3,10,5,0,123,124,5,39,0,0,124,17,1,0,0,0,125,126,5,
        17,0,0,126,127,3,36,18,0,127,128,5,3,0,0,128,19,1,0,0,0,129,140,
        3,22,11,0,130,140,3,24,12,0,131,140,3,26,13,0,132,140,3,30,15,0,
        133,140,3,32,16,0,134,140,3,34,17,0,135,140,3,28,14,0,136,140,3,
        38,19,0,137,140,3,40,20,0,138,140,3,18,9,0,139,129,1,0,0,0,139,130,
        1,0,0,0,139,131,1,0,0,0,139,132,1,0,0,0,139,133,1,0,0,0,139,134,
        1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,0,0,139,138,
        1,0,0,0,140,21,1,0,0,0,141,142,5,39,0,0,142,143,5,18,0,0,143,144,
        3,36,18,0,144,145,5,3,0,0,145,23,1,0,0,0,146,147,5,19,0,0,147,148,
        5,13,0,0,148,149,3,8,4,0,149,150,5,14,0,0,150,151,5,3,0,0,151,25,
        1,0,0,0,152,153,5,20,0,0,153,154,5,13,0,0,154,159,3,36,18,0,155,
        156,5,7,0,0,156,158,3,36,18,0,157,155,1,0,0,0,158,161,1,0,0,0,159,
        157,1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,
        163,5,14,0,0,163,164,5,3,0,0,164,27,1,0,0,0,165,166,5,21,0,0,166,
        167,5,3,0,0,167,29,1,0,0,0,168,169,5,22,0,0,169,170,5,13,0,0,170,
        171,3,36,18,0,171,172,5,14,0,0,172,176,5,15,0,0,173,175,3,20,10,
        0,174,173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,
        0,177,179,1,0,0,0,178,176,1,0,0,0,179,189,5,16,0,0,180,181,5,23,
        0,0,181,185,5,15,0,0,182,184,3,20,10,0,183,182,1,0,0,0,184,187,1,
        0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,
        0,0,0,188,190,5,16,0,0,189,180,1,0,0,0,189,190,1,0,0,0,190,31,1,
        0,0,0,191,192,5,24,0,0,192,193,5,13,0,0,193,194,3,36,18,0,194,195,
        5,14,0,0,195,199,5,15,0,0,196,198,3,20,10,0,197,196,1,0,0,0,198,
        201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,
        199,1,0,0,0,202,203,5,16,0,0,203,33,1,0,0,0,204,205,5,25,0,0,205,
        207,5,13,0,0,206,208,3,22,11,0,207,206,1,0,0,0,207,208,1,0,0,0,208,
        210,1,0,0,0,209,211,3,36,18,0,210,209,1,0,0,0,210,211,1,0,0,0,211,
        212,1,0,0,0,212,216,5,3,0,0,213,217,3,22,11,0,214,217,3,38,19,0,
        215,217,3,40,20,0,216,213,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,
        0,216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,14,0,0,219,223,5,15,
        0,0,220,222,3,20,10,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,
        0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,223,1,0,0,0,226,227,5,
        16,0,0,227,35,1,0,0,0,228,229,6,18,-1,0,229,230,5,13,0,0,230,231,
        3,36,18,0,231,232,5,14,0,0,232,245,1,0,0,0,233,234,5,26,0,0,234,
        245,3,36,18,13,235,236,5,27,0,0,236,245,3,36,18,12,237,245,3,42,
        21,0,238,245,5,39,0,0,239,245,5,40,0,0,240,245,5,41,0,0,241,245,
        5,42,0,0,242,245,5,35,0,0,243,245,5,36,0,0,244,228,1,0,0,0,244,233,
        1,0,0,0,244,235,1,0,0,0,244,237,1,0,0,0,244,238,1,0,0,0,244,239,
        1,0,0,0,244,240,1,0,0,0,244,241,1,0,0,0,244,242,1,0,0,0,244,243,
        1,0,0,0,245,260,1,0,0,0,246,247,10,11,0,0,247,248,7,1,0,0,248,259,
        3,36,18,12,249,250,10,10,0,0,250,251,7,2,0,0,251,259,3,36,18,11,
        252,253,10,9,0,0,253,254,7,3,0,0,254,259,3,36,18,10,255,256,10,8,
        0,0,256,257,7,4,0,0,257,259,3,36,18,9,258,246,1,0,0,0,258,249,1,
        0,0,0,258,252,1,0,0,0,258,255,1,0,0,0,259,262,1,0,0,0,260,258,1,
        0,0,0,260,261,1,0,0,0,261,37,1,0,0,0,262,260,1,0,0,0,263,264,5,39,
        0,0,264,265,5,37,0,0,265,266,5,3,0,0,266,39,1,0,0,0,267,268,5,39,
        0,0,268,269,5,38,0,0,269,270,5,3,0,0,270,41,1,0,0,0,271,272,5,39,
        0,0,272,281,5,13,0,0,273,278,3,36,18,0,274,275,5,7,0,0,275,277,3,
        36,18,0,276,274,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,
        1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,281,273,1,0,0,0,281,282,
        1,0,0,0,282,283,1,0,0,0,283,284,5,14,0,0,284,43,1,0,0,0,25,52,61,
        66,76,87,96,101,106,110,119,139,159,176,185,189,199,207,210,216,
        223,244,258,260,278,281
    ]

class JavythonParser ( Parser ):

    grammarFileName = "Javython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "':'", "';'", "'end'", "'main'", 
                     "'decIds'", "','", "'int'", "'real'", "'str'", "'bool'", 
                     "'void'", "'('", "')'", "'{'", "'}'", "'return'", "'='", 
                     "'input'", "'print'", "'break'", "'if'", "'else'", 
                     "'while'", "'for'", "'!'", "'-'", "'*'", "'/'", "'+'", 
                     "'=='", "'!='", "'>'", "'<'", "'true'", "'false'", 
                     "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM_INT", 
                      "NUM_REAL", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_decIds = 2
    RULE_decl = 3
    RULE_idList = 4
    RULE_tipo = 5
    RULE_metodo = 6
    RULE_parametros = 7
    RULE_parametro = 8
    RULE_returnCmd = 9
    RULE_comando = 10
    RULE_atribuicao = 11
    RULE_inputCmd = 12
    RULE_printCmd = 13
    RULE_breakCmd = 14
    RULE_ifCmd = 15
    RULE_whileCmd = 16
    RULE_forCmd = 17
    RULE_expressao = 18
    RULE_incremento = 19
    RULE_decremento = 20
    RULE_chamadaFuncao = 21

    ruleNames =  [ "program", "main", "decIds", "decl", "idList", "tipo", 
                   "metodo", "parametros", "parametro", "returnCmd", "comando", 
                   "atribuicao", "inputCmd", "printCmd", "breakCmd", "ifCmd", 
                   "whileCmd", "forCmd", "expressao", "incremento", "decremento", 
                   "chamadaFuncao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    ID=39
    NUM_INT=40
    NUM_REAL=41
    STRING=42
    WS=43
    COMMENT=44

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

        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def decIds(self):
            return self.getTypedRuleContext(JavythonParser.DecIdsContext,0)


        def main(self):
            return self.getTypedRuleContext(JavythonParser.MainContext,0)


        def metodo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.MetodoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.MetodoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = JavythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(JavythonParser.T__0)
            self.state = 45
            self.match(JavythonParser.T__1)
            self.state = 46
            self.match(JavythonParser.ID)
            self.state = 47
            self.match(JavythonParser.T__2)
            self.state = 48
            self.decIds()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0):
                self.state = 49
                self.metodo()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.main()
            self.state = 56
            self.match(JavythonParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decIds(self):
            return self.getTypedRuleContext(JavythonParser.DecIdsContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ComandoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ComandoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = JavythonParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(JavythonParser.T__4)
            self.state = 59
            self.match(JavythonParser.T__1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 60
                self.decIds()


            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549814140928) != 0):
                self.state = 63
                self.comando()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecIdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.DeclContext)
            else:
                return self.getTypedRuleContext(JavythonParser.DeclContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_decIds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecIds" ):
                listener.enterDecIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecIds" ):
                listener.exitDecIds(self)




    def decIds(self):

        localctx = JavythonParser.DecIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decIds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(JavythonParser.T__5)
            self.state = 70
            self.match(JavythonParser.T__1)
            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 71
                    self.decl()
                    self.state = 72
                    self.match(JavythonParser.T__2)

                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(JavythonParser.IdListContext,0)


        def tipo(self):
            return self.getTypedRuleContext(JavythonParser.TipoContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = JavythonParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.idList()
            self.state = 79
            self.match(JavythonParser.T__1)
            self.state = 80
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(JavythonParser.ID)
            else:
                return self.getToken(JavythonParser.ID, i)

        def getRuleIndex(self):
            return JavythonParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)




    def idList(self):

        localctx = JavythonParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(JavythonParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 83
                self.match(JavythonParser.T__6)
                self.state = 84
                self.match(JavythonParser.ID)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavythonParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = JavythonParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetodoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(JavythonParser.TipoContext,0)


        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(JavythonParser.ParametrosContext,0)


        def decIds(self):
            return self.getTypedRuleContext(JavythonParser.DecIdsContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ComandoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ComandoContext,i)


        def returnCmd(self):
            return self.getTypedRuleContext(JavythonParser.ReturnCmdContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_metodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetodo" ):
                listener.enterMetodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetodo" ):
                listener.exitMetodo(self)




    def metodo(self):

        localctx = JavythonParser.MetodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_metodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.tipo()
            self.state = 93
            self.match(JavythonParser.ID)
            self.state = 94
            self.match(JavythonParser.T__12)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0):
                self.state = 95
                self.parametros()


            self.state = 98
            self.match(JavythonParser.T__13)
            self.state = 99
            self.match(JavythonParser.T__14)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 100
                self.decIds()


            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 103
                    self.comando() 
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 109
                self.returnCmd()


            self.state = 112
            self.match(JavythonParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ParametroContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ParametroContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = JavythonParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.parametro()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 115
                self.match(JavythonParser.T__6)
                self.state = 116
                self.parametro()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(JavythonParser.TipoContext,0)


        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def getRuleIndex(self):
            return JavythonParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = JavythonParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.tipo()
            self.state = 123
            self.match(JavythonParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(JavythonParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_returnCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnCmd" ):
                listener.enterReturnCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnCmd" ):
                listener.exitReturnCmd(self)




    def returnCmd(self):

        localctx = JavythonParser.ReturnCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(JavythonParser.T__16)
            self.state = 126
            self.expressao(0)
            self.state = 127
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(JavythonParser.AtribuicaoContext,0)


        def inputCmd(self):
            return self.getTypedRuleContext(JavythonParser.InputCmdContext,0)


        def printCmd(self):
            return self.getTypedRuleContext(JavythonParser.PrintCmdContext,0)


        def ifCmd(self):
            return self.getTypedRuleContext(JavythonParser.IfCmdContext,0)


        def whileCmd(self):
            return self.getTypedRuleContext(JavythonParser.WhileCmdContext,0)


        def forCmd(self):
            return self.getTypedRuleContext(JavythonParser.ForCmdContext,0)


        def breakCmd(self):
            return self.getTypedRuleContext(JavythonParser.BreakCmdContext,0)


        def incremento(self):
            return self.getTypedRuleContext(JavythonParser.IncrementoContext,0)


        def decremento(self):
            return self.getTypedRuleContext(JavythonParser.DecrementoContext,0)


        def returnCmd(self):
            return self.getTypedRuleContext(JavythonParser.ReturnCmdContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = JavythonParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comando)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.atribuicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.inputCmd()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.printCmd()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.ifCmd()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.whileCmd()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.forCmd()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self.breakCmd()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 136
                self.incremento()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.decremento()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 138
                self.returnCmd()
                pass


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
            return self.getToken(JavythonParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(JavythonParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = JavythonParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(JavythonParser.ID)
            self.state = 142
            self.match(JavythonParser.T__17)
            self.state = 143
            self.expressao(0)
            self.state = 144
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(JavythonParser.IdListContext,0)


        def getRuleIndex(self):
            return JavythonParser.RULE_inputCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputCmd" ):
                listener.enterInputCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputCmd" ):
                listener.exitInputCmd(self)




    def inputCmd(self):

        localctx = JavythonParser.InputCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inputCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(JavythonParser.T__18)
            self.state = 147
            self.match(JavythonParser.T__12)
            self.state = 148
            self.idList()
            self.state = 149
            self.match(JavythonParser.T__13)
            self.state = 150
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_printCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCmd" ):
                listener.enterPrintCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCmd" ):
                listener.exitPrintCmd(self)




    def printCmd(self):

        localctx = JavythonParser.PrintCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_printCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(JavythonParser.T__19)
            self.state = 153
            self.match(JavythonParser.T__12)
            self.state = 154
            self.expressao(0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 155
                self.match(JavythonParser.T__6)
                self.state = 156
                self.expressao(0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(JavythonParser.T__13)
            self.state = 163
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JavythonParser.RULE_breakCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakCmd" ):
                listener.enterBreakCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakCmd" ):
                listener.exitBreakCmd(self)




    def breakCmd(self):

        localctx = JavythonParser.BreakCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(JavythonParser.T__20)
            self.state = 166
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(JavythonParser.ExpressaoContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ComandoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ComandoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_ifCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCmd" ):
                listener.enterIfCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCmd" ):
                listener.exitIfCmd(self)




    def ifCmd(self):

        localctx = JavythonParser.IfCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(JavythonParser.T__21)
            self.state = 169
            self.match(JavythonParser.T__12)
            self.state = 170
            self.expressao(0)
            self.state = 171
            self.match(JavythonParser.T__13)
            self.state = 172
            self.match(JavythonParser.T__14)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549814140928) != 0):
                self.state = 173
                self.comando()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(JavythonParser.T__15)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 180
                self.match(JavythonParser.T__22)
                self.state = 181
                self.match(JavythonParser.T__14)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549814140928) != 0):
                    self.state = 182
                    self.comando()
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 188
                self.match(JavythonParser.T__15)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(JavythonParser.ExpressaoContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ComandoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ComandoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_whileCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCmd" ):
                listener.enterWhileCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCmd" ):
                listener.exitWhileCmd(self)




    def whileCmd(self):

        localctx = JavythonParser.WhileCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(JavythonParser.T__23)
            self.state = 192
            self.match(JavythonParser.T__12)
            self.state = 193
            self.expressao(0)
            self.state = 194
            self.match(JavythonParser.T__13)
            self.state = 195
            self.match(JavythonParser.T__14)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549814140928) != 0):
                self.state = 196
                self.comando()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(JavythonParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.AtribuicaoContext,i)


        def expressao(self):
            return self.getTypedRuleContext(JavythonParser.ExpressaoContext,0)


        def incremento(self):
            return self.getTypedRuleContext(JavythonParser.IncrementoContext,0)


        def decremento(self):
            return self.getTypedRuleContext(JavythonParser.DecrementoContext,0)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ComandoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ComandoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_forCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCmd" ):
                listener.enterForCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCmd" ):
                listener.exitForCmd(self)




    def forCmd(self):

        localctx = JavythonParser.ForCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(JavythonParser.T__24)
            self.state = 205
            self.match(JavythonParser.T__12)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 206
                self.atribuicao()


            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8349617758208) != 0):
                self.state = 209
                self.expressao(0)


            self.state = 212
            self.match(JavythonParser.T__2)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 213
                self.atribuicao()

            elif la_ == 2:
                self.state = 214
                self.incremento()

            elif la_ == 3:
                self.state = 215
                self.decremento()


            self.state = 218
            self.match(JavythonParser.T__13)
            self.state = 219
            self.match(JavythonParser.T__14)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549814140928) != 0):
                self.state = 220
                self.comando()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(JavythonParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ExpressaoContext,i)


        def chamadaFuncao(self):
            return self.getTypedRuleContext(JavythonParser.ChamadaFuncaoContext,0)


        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def NUM_INT(self):
            return self.getToken(JavythonParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(JavythonParser.NUM_REAL, 0)

        def STRING(self):
            return self.getToken(JavythonParser.STRING, 0)

        def getRuleIndex(self):
            return JavythonParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JavythonParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(JavythonParser.T__12)
                self.state = 230
                self.expressao(0)
                self.state = 231
                self.match(JavythonParser.T__13)
                pass

            elif la_ == 2:
                self.state = 233
                localctx.op = self.match(JavythonParser.T__25)
                self.state = 234
                self.expressao(13)
                pass

            elif la_ == 3:
                self.state = 235
                localctx.op = self.match(JavythonParser.T__26)
                self.state = 236
                self.expressao(12)
                pass

            elif la_ == 4:
                self.state = 237
                self.chamadaFuncao()
                pass

            elif la_ == 5:
                self.state = 238
                self.match(JavythonParser.ID)
                pass

            elif la_ == 6:
                self.state = 239
                self.match(JavythonParser.NUM_INT)
                pass

            elif la_ == 7:
                self.state = 240
                self.match(JavythonParser.NUM_REAL)
                pass

            elif la_ == 8:
                self.state = 241
                self.match(JavythonParser.STRING)
                pass

            elif la_ == 9:
                self.state = 242
                self.match(JavythonParser.T__34)
                pass

            elif la_ == 10:
                self.state = 243
                self.match(JavythonParser.T__35)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = JavythonParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 246
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 247
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 248
                        self.expressao(12)
                        pass

                    elif la_ == 2:
                        localctx = JavythonParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 249
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 250
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 251
                        self.expressao(11)
                        pass

                    elif la_ == 3:
                        localctx = JavythonParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 252
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 253
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 254
                        self.expressao(10)
                        pass

                    elif la_ == 4:
                        localctx = JavythonParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 255
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 256
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expressao(9)
                        pass

             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IncrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def getRuleIndex(self):
            return JavythonParser.RULE_incremento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)




    def incremento(self):

        localctx = JavythonParser.IncrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_incremento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(JavythonParser.ID)
            self.state = 264
            self.match(JavythonParser.T__36)
            self.state = 265
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def getRuleIndex(self):
            return JavythonParser.RULE_decremento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecremento" ):
                listener.enterDecremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecremento" ):
                listener.exitDecremento(self)




    def decremento(self):

        localctx = JavythonParser.DecrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_decremento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(JavythonParser.ID)
            self.state = 268
            self.match(JavythonParser.T__37)
            self.state = 269
            self.match(JavythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChamadaFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JavythonParser.ID, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavythonParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(JavythonParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return JavythonParser.RULE_chamadaFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaFuncao" ):
                listener.enterChamadaFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaFuncao" ):
                listener.exitChamadaFuncao(self)




    def chamadaFuncao(self):

        localctx = JavythonParser.ChamadaFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_chamadaFuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(JavythonParser.ID)
            self.state = 272
            self.match(JavythonParser.T__12)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8349617758208) != 0):
                self.state = 273
                self.expressao(0)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 274
                    self.match(JavythonParser.T__6)
                    self.state = 275
                    self.expressao(0)
                    self.state = 280
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 283
            self.match(JavythonParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




