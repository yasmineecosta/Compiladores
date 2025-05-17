from gen.JavythonListener import JavythonListener
from gen.JavythonParser import JavythonParser

class AcoesSemanticas(JavythonListener):
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
