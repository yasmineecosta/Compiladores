from antlr4 import *
from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from antlr4.error.ErrorListener import ErrorListener


# from AcoesSemanticas import AcoesSemanticas


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")


def main():
    input_stream = FileStream("exemplo.jy", encoding="utf-8")
    lexer = JavythonLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())

    stream = CommonTokenStream(lexer)
    parser = JavythonParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()

# walker = ParseTreeWalker()
# semantico = AcoesSemanticas()
# walker.walk(semantico, tree)

# if semantico.erros:
#    print(f"\n{len(semantico.erros)} erro(s) semântico(s) encontrado(s).")
# else:
#    print("\n✔️ Nenhum erro semântico encontrado.")
