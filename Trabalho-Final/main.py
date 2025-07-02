# Trabalho-Final/main.py (Versão Final com Impressão da Tabela de Símbolos)

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from ast_listener import ASTListener
from analisador_semantico import AnalisadorSemantico
from tac_generator import TACGenerator # Novo import

def print_section_header(title):
    """ Imprime um cabeçalho padronizado para a apresentação. """
    print(f"\n{'=' * 25} {title.upper()} {'=' * 25}")


class MyErrorListener(ErrorListener):
    """ Captura erros de sintaxe para um relatório mais limpo. """

    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro_msg = f"Linha {line}:{column}: {msg}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_o_arquivo.jy>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"Iniciando compilação do arquivo: {input_file}")

    try:
        input_stream = FileStream(input_file, encoding="utf-8")

        # --- a) Análise Léxica ---
        print_section_header("a) Regras de Análise Léxica (Tokens)")
        lexer = JavythonLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        # Acessa os nomes simbólicos e literais diretamente do Parser.
        symbolic_names = JavythonParser.symbolicNames
        literal_names = JavythonParser.literalNames

        for token in token_stream.tokens:
            if token.type == Token.EOF:
                break

            token_name = symbolic_names[token.type]
            if token_name == "<INVALID>":
                token_name = literal_names[token.type]

            print(f"  - Tipo: {token_name:<15} | Texto: '{token.text}'")

        token_stream.seek(0)

        # --- b) Análise Sintática ---
        print_section_header("b) Regras de Análise Sintática")
        error_listener = MyErrorListener()
        parser = JavythonParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        tree = parser.program()

        if error_listener.erros:
            print("❌ Erros de sintaxe encontrados:")
            for erro in error_listener.erros:
                print(f"  -> {erro}")
            sys.exit(1)
        else:
            print("✔️ Análise sintática concluída com sucesso.")

        # --- c) Análise Semântica ---
        print_section_header("c) Regras de Semântica")
        walker = ParseTreeWalker()
        analisador_semantico = AnalisadorSemantico()
        walker.walk(analisador_semantico, tree)

        if analisador_semantico.erros:
            print("❌ Foram encontrados erros semânticos.")
        else:
            print("✔️ Análise semântica concluída sem erros.")

        # --- d) Geração da Saída ---
        print_section_header("d) Geração da Saída")
        if analisador_semantico.erros:
            print("Compilação falhou. Relatório de erros:")
            for erro in analisador_semantico.erros:
                print(f"  -> {erro}")
        else:
            print("Compilação bem-sucedida!")

            # --- IMPRESSÃO DA TABELA DE SÍMBOLOS ---
            print("\n--- Tabela de Símbolos Final ---")
            print(analisador_semantico.tabela)
            # ----------------------------------------

            print("\n--- Árvore Sintática Abstrata (AST) ---")
            ast_builder = ASTListener()
            walker.walk(ast_builder, tree)
            ast_string = ast_builder.get_ast_string(tree)
            # Limpa múltiplos espaços para uma melhor visualização
            print(' '.join(ast_string.split()))

            # --- Geração do Código de Três Endereços (TAC) ---
            print("\n--- Código de Três Endereços (TAC) ---")
            tac_generator = TACGenerator(analisador_semantico.tabela)
            tac_instructions = tac_generator.visit(tree)
            for instr in tac_instructions:
                print(instr)

    except FileNotFoundError:
        print(f"\nERRO: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == '__main__':
    main()