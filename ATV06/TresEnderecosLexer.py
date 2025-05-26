# Generated from ./TresEnderecos.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,
        7,1,7,1,8,1,8,1,9,1,9,5,9,51,8,9,10,9,12,9,54,9,9,1,10,4,10,57,8,
        10,11,10,12,10,58,1,11,4,11,62,8,11,11,11,12,11,63,1,11,1,11,0,0,
        12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,
        4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,69,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,32,
        1,0,0,0,5,34,1,0,0,0,7,36,1,0,0,0,9,38,1,0,0,0,11,40,1,0,0,0,13,
        42,1,0,0,0,15,44,1,0,0,0,17,46,1,0,0,0,19,48,1,0,0,0,21,56,1,0,0,
        0,23,61,1,0,0,0,25,26,5,110,0,0,26,27,5,117,0,0,27,28,5,109,0,0,
        28,29,5,98,0,0,29,30,5,101,0,0,30,31,5,114,0,0,31,2,1,0,0,0,32,33,
        5,59,0,0,33,4,1,0,0,0,34,35,5,61,0,0,35,6,1,0,0,0,36,37,5,42,0,0,
        37,8,1,0,0,0,38,39,5,47,0,0,39,10,1,0,0,0,40,41,5,43,0,0,41,12,1,
        0,0,0,42,43,5,45,0,0,43,14,1,0,0,0,44,45,5,40,0,0,45,16,1,0,0,0,
        46,47,5,41,0,0,47,18,1,0,0,0,48,52,7,0,0,0,49,51,7,1,0,0,50,49,1,
        0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,20,1,0,0,0,54,
        52,1,0,0,0,55,57,7,2,0,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,
        0,58,59,1,0,0,0,59,22,1,0,0,0,60,62,7,3,0,0,61,60,1,0,0,0,62,63,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,6,11,0,0,
        66,24,1,0,0,0,4,0,52,58,63,1,6,0,0
    ]

class TresEnderecosLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    SEMI = 2
    EQUAL = 3
    MUL = 4
    DIV = 5
    ADD = 6
    SUB = 7
    LPAREN = 8
    RPAREN = 9
    ID = 10
    INT = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "';'", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
            "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "SEMI", "EQUAL", "MUL", "DIV", "ADD", "SUB", "LPAREN", 
            "RPAREN", "ID", "INT", "WS" ]

    ruleNames = [ "NUMBER", "SEMI", "EQUAL", "MUL", "DIV", "ADD", "SUB", 
                  "LPAREN", "RPAREN", "ID", "INT", "WS" ]

    grammarFileName = "TresEnderecos.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


