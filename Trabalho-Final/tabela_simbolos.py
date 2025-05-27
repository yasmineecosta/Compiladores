class TabelaSimbolos:
    def __init__(self):
        self.escopos = [{}]  # pilha de dicionários

    def entrar_escopo(self):
        self.escopos.append({})

    def sair_escopo(self):
        if len(self.escopos) > 1:
            self.escopos.pop()

    def declarar(self, nome, tipo):
        escopo_atual = self.escopos[-1]
        if nome in escopo_atual:
            return False  # já declarado no escopo atual
        escopo_atual[nome] = tipo
        return True

    def existe_em_escopo_atual(self, nome):
        return nome in self.escopos[-1]

    def buscar(self, nome):
        for escopo in reversed(self.escopos):
            if nome in escopo:
                return escopo[nome]
        return None

    def escopo_global(self):
        return self.escopos[0]
