from antlr4 import *
from TresEnderecosLexer import TresEnderecosLexer
from TresEnderecosParser import TresEnderecosParser
from TresEnderecosSemantico import TresEnderecosSemantico, ErroSemantico
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lança exceção na primeira ocorrência de erro sintático
        raise Exception(f"Erro sintático na linha {line}, coluna {column}: {msg}")



def main(file_path):
    input_stream = FileStream(file_path)
    lexer = TresEnderecosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TresEnderecosParser(stream)


    # Adiciona o listener de erros sintáticos
    parser.removeErrorListeners()  # Remove os listeners padrão
    parser.addErrorListener(MyErrorListener()) # Adiciona o listener personalizado


    listener = TresEnderecosSemantico()
    walker = ParseTreeWalker()

    try:
        tree = parser.program()

        listener = TresEnderecosSemantico()
        walker = ParseTreeWalker()

        # Tenta caminhar a árvore e capturar erros semânticos
        walker.walk(listener, tree)

    except ErroSemantico as e:
        # Se ocorrer erro semântico, imprime a mensagem de erro
        print(f" {e.message} (linha {e.line}, coluna {e.column})")
        return

    except Exception as e:
        # Captura outros erros e imprime uma mensagem genérica
        print(f"Erro inesperado: {str(e)}")
        return

        # Se não ocorreu erro, imprime o código gerado
    print("\nPrograma compilado com sucesso.")

if __name__ == "__main__":
    import sys
    main(sys.argv[1])  # python main.py .\teste1.txt -> Terminal
    print("\n")
