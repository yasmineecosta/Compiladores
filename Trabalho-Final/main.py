from antlr4 import *
from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from JavythonListener import JavythonListener
from antlr4.error.ErrorListener import ErrorListener
import sys
import json
import os
from analisador_semantico import AnalisadorSemantico


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")
        raise Exception(f"Erro de sintaxe: {msg}")


class ASTBuilder(JavythonListener):
    def __init__(self):
        self.ast = {"type": "Program", "children": []}
        self.stack = [self.ast]  # pilha para navegar entre nós

    def current_node(self):
        return self.stack[-1]

    def enterProgram(self, ctx):
        pass  # já criado no __init__

    def enterMain(self, ctx):
        main_node = {"type": "Main", "children": []}
        self.current_node()["children"].append(main_node)
        self.stack.append(main_node)

    def exitMain(self, ctx):
        self.stack.pop()

    def enterMetodo(self, ctx):
        tipo = ctx.tipo().getText() if ctx.tipo() else "void"
        nome = ctx.ID().getText()
        metodo_node = {"type": "Method", "name": nome, "returnType": tipo, "children": []}
        self.current_node()["children"].append(metodo_node)
        self.stack.append(metodo_node)

    def exitMetodo(self, ctx):
        self.stack.pop()

    def enterDecl(self, ctx):
        texto = ctx.getText()
        decl_node = {"type": "Declaration", "text": texto}
        self.current_node()["children"].append(decl_node)

    def enterComando(self, ctx):
        texto = ctx.getText().replace("\n", " ").replace(" ", "").strip()
        comando_node = {"type": "Command", "text": texto}
        self.current_node()["children"].append(comando_node)

    def exitProgram(self, ctx):
        while len(self.stack) > 1:
            self.stack.pop()

def print_ast(node, indent=0):
    spacing = "  " * indent
    if isinstance(node, dict):
        node_type = node.get("type", "<unknown>")
        print(f"{spacing}{node_type}:")
        for key, value in node.items():
            if key == "type":
                continue
            if isinstance(value, list):
                print(f"{spacing}  {key}:")
                for child in value:
                    print_ast(child, indent + 2)
            elif isinstance(value, dict):
                print(f"{spacing}  {key}:")
                print_ast(value, indent + 2)
            else:
                print(f"{spacing}  {key}: {value}")
    else:
        print(f"{spacing}{node}")


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
        print("\nÁrvore de análise sintática:")
        print(tree.toStringTree(recog=parser))

        # Construção da AST
        # ast_builder = ASTBuilder()
        # walker = ParseTreeWalker()
        # walker.walk(ast_builder, tree)
        # print("\n\u00c1rvore de Sintaxe Abstrata (AST):")
        # print_ast(ast_builder.ast)

        # print("\nÁrvore de Sintaxe Abstrata (AST):")
        # print(ast_builder.ast)
        # print("\n\u00c1rvore de Sintaxe Abstrata (AST):")
        # print(json.dumps(ast_builder.ast, indent=2, ensure_ascii=False))
        

        listener = AnalisadorSemantico(debug=True)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # if hasattr(listener, "erros") and listener.erros:
        #     print("\nErros semânticos encontrados:")
        #     for erro in listener.erros:
        #         print(erro)
        # else:
        #     print("\n✔️ Nenhum erro semântico encontrado.")
        print("\nTabela de símbolos:")
        for nome, tipo in listener.tabela_global.items():
            print(f"  {nome}: {tipo}")

        if listener.erros:
            print("\nErros semânticos encontrados:")
            for erro in listener.erros:
                print(erro)
        else:
            print("\n✔️ Nenhum erro semântico encontrado.")


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
