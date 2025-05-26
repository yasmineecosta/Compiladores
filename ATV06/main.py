from antlr4 import *
from TresEnderecosLexer import TresEnderecosLexer
from TresEnderecosParser import TresEnderecosParser
from TresEnderecosListener import TresEnderecosListener

def main(file_path):
    input_stream = FileStream(file_path)
    lexer = TresEnderecosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TresEnderecosParser(stream)
    tree = parser.program()

    listener = TresEnderecosListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])  # python main.py .\teste.txt -> Terminal
    print("\n")
