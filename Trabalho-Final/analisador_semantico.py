from antlr4 import *
from JavythonListener import JavythonListener
from tabela_simbolos import TabelaSimbolos

PALAVRAS_RESERVADAS = {
            'if', 'else', 'while', 'for', 'break', 'input', 'print', 'program', 'main', 'end', 'return',
            'int', 'real', 'str', 'bool', 'void', 'decIds'
        }  
class AnalisadorSemantico(JavythonListener):
    def __init__(self, debug=False):
        self.debug = debug
        self.tabela_global = {}  # usa classe modular
        self.erros = []
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

    def reportaErro(self, msg):
        # print("[Erro semântico] " + msg)
        # self.erros.append(msg)
        self.erros.append(f"[Erro semântico] {msg}")
        if self.debug:
            print("[Erro semântico] " + msg)

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

    def nome_invalido(self, nome):
        return nome.lower() in PALAVRAS_RESERVADAS or nome.lower() in self.tabela_global
    
    def enterDecl(self, ctx):
        tipo = ctx.tipo().getText()
        if tipo == "void":
            self.reportaErro
            ("Variável não pode ser declarada com tipo 'void'.")
            return
        for id_ctx in ctx.idList().ID():
            nome = id_ctx.getText().lower()
            if self.nome_invalido(nome):
                self.reportaErro
                (f"Nome inválido ou já utilizado: '{nome}'")
            else:
                self.tabela_global[nome] = f"variável ({tipo})"

    def enterMetodo(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.ID().getText().lower()
        if self.nome_invalido(nome):
            self.reportaErro
            (f"Nome de método inválido ou já utilizado: '{nome}'")
        else:
            self.tabela_global[nome] = f"método ({tipo})"

        if ctx.parametros():
            for p in ctx.parametros().parametro():
                nome_param = p.ID().getText().lower()
                tipo_param = p.tipo().getText()
                if tipo_param == "void":
                    self.reportaErro
                    (f"Parâmetro '{nome_param}' não pode ser do tipo 'void'.")
                if self.nome_invalido(nome_param):
                    self.reportaErro
                    (f"Nome de parâmetro inválido ou já utilizado: '{nome_param}'")
                else:
                    self.tabela_global[nome_param] = f"parâmetro ({tipo_param})"

    

    # def __init__(self):
    #     self.tabela = TabelaSimbolos()  # usa classe modular
    #     self.metodos = {}
    #     self.escopo_atual = "global"
    #     self.erros = []
    #     self.declaracoes_encerradas = False

    # def reportaErro
    # (self, msg):
    #     self.erros.append("[Erro semântico] " + msg)

    # def enterMain(self, ctx):
    #     self.tabela.entrar_escopo()
    #     self.declaracoes_encerradas = False
    #     self.escopo_atual = "main"

    # def exitMain(self, ctx):
    #     self.tabela.sair_escopo()
    #     self.escopo_atual = "global"

    # def enterMetodo(self, ctx):
    #     nome = ctx.ID().getText()
    #     tipo = ctx.tipo().getText() if ctx.tipo() else "void"
    #     if nome in self.metodos or self.tabela.existe_em_escopo_atual(nome):
    #         self.reportaErro
    # (f"Método '{nome}' já declarado.")
    #     self.metodos[nome] = {
    #         "tipo": tipo,
    #         "params": [],
    #     }
    #     self.tabela.entrar_escopo()
    #     self.escopo_atual = nome
    #     if ctx.parametros():
    #         for p in ctx.parametros().parametro():
    #             tipo_param = p.tipo().getText()
    #             nome_param = p.ID().getText()
    #             if not self.tabela.declarar(nome_param, tipo_param):
    #                 self.reportaErro
    # (f"Parâmetro '{nome_param}' já declarado.")
    #             self.metodos[nome]["params"].append(tipo_param)

    # def exitMetodo(self, ctx):
    #     self.tabela.sair_escopo()
    #     self.escopo_atual = "global"

    # def enterDecl(self, ctx):
    #     if self.declaracoes_encerradas:
    #         self.reportaErro
    # ("Declaração após comandos não é permitida.")
    #     tipo = ctx.tipo().getText()
    #     for id_ctx in ctx.idList().ID():
    #         nome = id_ctx.getText()
    #         if not self.tabela.declarar(nome, tipo):
    #             self.reportaErro
    # (f"Variável '{nome}' já declarada no escopo atual.")
    #         elif nome in self.metodos:
    #             self.reportaErro
    # (f"Nome '{nome}' já utilizado por um método.")

    # # def enterComando(self, ctx):
    # #     self.declaracoes_encerradas = True
    # def enterComando(self, ctx):
    #     if self.escopo_atual in ["main"] or self.escopo_atual in self.metodos:
    #         self.declaracoes_encerradas = True

    # def enterChamadaFuncao(self, ctx):
    #     nome = ctx.ID().getText()
    #     if nome not in self.metodos:
    #         self.reportaErro
    # (f"Chamada a função '{nome}' não declarada.")
    #     else:
    #         esperado = len(self.metodos[nome]["params"])
    #         fornecido = len(ctx.expressao())
    #         if esperado != fornecido:
    #             self.reportaErro
    # (f"Função '{nome}' espera {esperado} argumento(s), mas recebeu {fornecido}.")







# class sintatic(JavythonListener):
#     def __init__(self):
#         # Simula tipos de variáveis (tudo lowercase por insensibilidade a maiúsculas)
#         self.tabela_simbolos = {
#             "a": "int",
#             "b": "real",
#             "c": "bool",
#             "d": "string",
#             "i": "int",
#             "r": "real",
#             "s": "string"
#         }
#         self.erros = []

#     def reportaErro(self, msg):
#         print("[Erro semântico] " + msg)
#         self.erros.append(msg)

#     # Expressões
#     def exitAddSub(self, ctx):
#         self.validaBinario(ctx, ["int", "real", "string"], "add/sub")

#     def exitMulDiv(self, ctx):
#         self.validaBinario(ctx, ["int", "real"], "mul/div")

#     def exitRelacional(self, ctx):
#         self.validaBinario(ctx, ["int", "real", "bool", "string"], "relacional")

#     def exitIgualdade(self, ctx):
#         self.validaBinario(ctx, ["int", "real", "bool", "string"], "igualdade")

#     def exitUnaryNot(self, ctx):
#         tipo = self.inferirTipo(ctx.expressao())
#         if tipo != "bool":
#             self.reportaErro(f"'!' requer tipo bool, mas foi usado '{tipo}'")

#     def exitUnaryMinus(self, ctx):
#         tipo = self.inferirTipo(ctx.expressao())
#         if tipo not in ["int", "real"]:
#             self.reportaErro(f"'-' requer tipo int ou real, mas foi usado '{tipo}'")

#     # ++ e --
#     def exitIncremento(self, ctx):
#         var = ctx.ID().getText().lower()
#         tipo = self.tabela_simbolos.get(var, "desconhecido")
#         if tipo != "int":
#             self.reportaErro(f"'++' requer tipo int, mas '{var}' é do tipo {tipo}")

#     def exitDecremento(self, ctx):
#         var = ctx.ID().getText().lower()
#         tipo = self.tabela_simbolos.get(var, "desconhecido")
#         if tipo != "int":
#             self.reportaErro(f"'--' requer tipo int, mas '{var}' é do tipo {tipo}")

#     # Auxiliares
#     def validaBinario(self, ctx, tiposAceitos, nomeOperador):
#         tipo_esq = self.inferirTipo(ctx.expressao(0))
#         tipo_dir = self.inferirTipo(ctx.expressao(1))
#         if tipo_esq != tipo_dir:
#             self.reportaErro(f"Tipos incompatíveis em '{nomeOperador}': {tipo_esq} e {tipo_dir}")
#         elif tipo_esq not in tiposAceitos:
#             self.reportaErro(f"Tipo inválido em '{nomeOperador}': {tipo_esq}")

#     def inferirTipo(self, ctx):
#         if ctx.ID():
#             nome = ctx.ID().getText().lower()
#             return self.tabela_simbolos.get(nome, "desconhecido")
#         elif ctx.NUM_INT():
#             return "int"
#         elif ctx.NUM_REAL():
#             return "real"
#         elif ctx.STRING():
#             return "string"
#         elif ctx.getText().lower() in ["true", "false"]:
#             return "bool"
#         elif ctx.expressao():
#             return self.inferirTipo(ctx.expressao(0))
#         return "desconhecido"

