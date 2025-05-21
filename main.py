from antlr4 import *
from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from antlr4.error.ErrorListener import ErrorListener
import sys


# from AcoesSemanticas import AcoesSemanticas


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")
        raise Exception(f"Erro de sintaxe: {msg}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.jy>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
        lexer = JavythonLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener())

        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        print("Tokens detalhados:")
        for token in token_stream.tokens:
            print(f"Tipo: {token.type}, Texto: '{token.text}'")

        parser = JavythonParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        print("Árvore de análise sintática:")
        print(tree.toStringTree(recog=parser))
    
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# walker = ParseTreeWalker()
# semantico = AcoesSemanticas()
# walker.walk(semantico, tree)

# if semantico.erros:
#    print(f"\n{len(semantico.erros)} erro(s) semântico(s) encontrado(s).")
# else:
#    print("\n✔️ Nenhum erro semântico encontrado.")
