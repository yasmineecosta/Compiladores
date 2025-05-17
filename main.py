from antlr4 import *
from gen.JavythonLexer import JavythonLexer
from gen.JavythonParser import JavythonParser
from AcoesSemanticas import AcoesSemanticas

if __name__ == "__main__":
    input_stream = FileStream("exemplo.jy", encoding="utf-8")
    lexer = JavythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavythonParser(stream)

    tree = parser.program()
    walker = ParseTreeWalker()
    semantico = AcoesSemanticas()
    walker.walk(semantico, tree)

    if semantico.erros:
        print(f"\n{len(semantico.erros)} erro(s) semântico(s) encontrado(s).")
    else:
        print("\n✔️ Nenhum erro semântico encontrado.")
