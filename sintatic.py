from antlr4 import *
from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from JavythonListener import JavythonListener
from antlr4.tree.Tree import ParseTreeWalker
import sys
from anytree import Node, RenderTree
from antlr4.error.ErrorListener import ErrorListener

class errorLexerListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")
        raise Exception(f"Erro de sintaxe: {msg}")
    


class sintatic(JavythonListener):
    def __init__(self):
        # Simula tipos de variáveis (tudo lowercase por insensibilidade a maiúsculas)
        self.tabela_simbolos = {
            "a": "int",
            "b": "real",
            "c": "bool",
            "d": "string",
            "i": "int",
            "r": "real",
            "s": "string"
        }
        self.erros = []

    def reportaErro(self, msg):
        print("[Erro semântico] " + msg)
        self.erros.append(msg)

    # Expressões
    def exitAddSub(self, ctx):
        self.validaBinario(ctx, ["int", "real", "string"], "add/sub")

    def exitMulDiv(self, ctx):
        self.validaBinario(ctx, ["int", "real"], "mul/div")

    def exitRelacional(self, ctx):
        self.validaBinario(ctx, ["int", "real", "bool", "string"], "relacional")

    def exitIgualdade(self, ctx):
        self.validaBinario(ctx, ["int", "real", "bool", "string"], "igualdade")

    def exitUnaryNot(self, ctx):
        tipo = self.inferirTipo(ctx.expressao())
        if tipo != "bool":
            self.reportaErro(f"'!' requer tipo bool, mas foi usado '{tipo}'")

    def exitUnaryMinus(self, ctx):
        tipo = self.inferirTipo(ctx.expressao())
        if tipo not in ["int", "real"]:
            self.reportaErro(f"'-' requer tipo int ou real, mas foi usado '{tipo}'")

    # ++ e --
    def exitIncremento(self, ctx):
        var = ctx.ID().getText().lower()
        tipo = self.tabela_simbolos.get(var, "desconhecido")
        if tipo != "int":
            self.reportaErro(f"'++' requer tipo int, mas '{var}' é do tipo {tipo}")

    def exitDecremento(self, ctx):
        var = ctx.ID().getText().lower()
        tipo = self.tabela_simbolos.get(var, "desconhecido")
        if tipo != "int":
            self.reportaErro(f"'--' requer tipo int, mas '{var}' é do tipo {tipo}")

    # Auxiliares
    def validaBinario(self, ctx, tiposAceitos, nomeOperador):
        tipo_esq = self.inferirTipo(ctx.expressao(0))
        tipo_dir = self.inferirTipo(ctx.expressao(1))
        if tipo_esq != tipo_dir:
            self.reportaErro(f"Tipos incompatíveis em '{nomeOperador}': {tipo_esq} e {tipo_dir}")
        elif tipo_esq not in tiposAceitos:
            self.reportaErro(f"Tipo inválido em '{nomeOperador}': {tipo_esq}")

    def inferirTipo(self, ctx):
        if ctx.ID():
            nome = ctx.ID().getText().lower()
            return self.tabela_simbolos.get(nome, "desconhecido")
        elif ctx.NUM_INT():
            return "int"
        elif ctx.NUM_REAL():
            return "real"
        elif ctx.STRING():
            return "string"
        elif ctx.getText().lower() in ["true", "false"]:
            return "bool"
        elif ctx.expressao():
            return self.inferirTipo(ctx.expressao(0))
        return "desconhecido"


# Adiciona uma implementação simples de TreeBuilder para evitar erro de definição
class TreeBuilder(JavythonListener):
    def __init__(self, parser):
        self.parser = parser
        self.root = Node("root", tipo="root")

    # Exemplo de método enter para construir a árvore (adapte conforme necessário)
    def enterEveryRule(self, ctx):
        pass

    def exitEveryRule(self, ctx):
        pass

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = JavythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavythonParser(stream)

    error_lexer = errorLexerListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_lexer)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = JavythonParser(token_stream)
    # parser.removeErrorListeners()
    tree = parser.file_()
    # tree = parser.programa()

    # Cria o listener e o walker
    # listener = sintatic()
    
    # Adiciona um listener de erro
    # parser.removeErrorListeners()
    # parser.addErrorListener(ErrorListener())

    # Faz a caminhada na árvore
    # walker.walk(listener, tree)

    tree_builder = TreeBuilder(parser)
    walker = ParseTreeWalker()
    walker.walk(tree_builder, tree)

    if parser.getNumberOfSyntaxErrors() <=0 and error_lexer.error_count <= 0:
        print("Análise sintática concluída sem erros.")
        for pre, fill, node in RenderTree(tree_builder.root):
            print(f"{pre}{node.name} (tipo: {node.tipo})")
    # Exibe os erros encontrados
    # if listener.erros:
    #     print("Erros encontrados:")
    #     for erro in listener.erros:
    #         print(erro)
    # else:
    #     print("Sem erros.")

if __name__ == '__main__':
    main()