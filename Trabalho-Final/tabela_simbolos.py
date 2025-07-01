# Trabalho-Final/tabela_simbolos.py (Versão Corrigida com Escopos Aninhados)

class Simbolo:
    """ Representa uma entrada na tabela (variável, método, etc.). """

    def __init__(self, nome, tipo, categoria='variavel', linha=0):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.linha = linha

    def __str__(self):
        return f"{self.nome} -> (Categoria: {self.categoria}, Tipo: {self.tipo}, Linha: {self.linha})"


class Escopo:
    """ Representa um único escopo com seus símbolos e escopos filhos. """

    def __init__(self, pai=None, nome="global"):
        self.simbolos = {}
        self.pai = pai
        self.filhos = []
        self.nome = nome

    def declarar(self, simbolo: Simbolo):
        if simbolo.nome in self.simbolos:
            return False
        self.simbolos[simbolo.nome] = simbolo
        return True

    def buscar(self, nome):
        if nome in self.simbolos:
            return self.simbolos[nome]
        if self.pai:
            return self.pai.buscar(nome)
        return None

    def adicionar_filho(self, nome_escopo):
        filho = Escopo(pai=self, nome=nome_escopo)
        self.filhos.append(filho)
        return filho


class TabelaSimbolos:
    """ Gerencia a árvore de escopos para a análise semântica. """

    def __init__(self):
        self.escopo_raiz = Escopo(nome="global")
        self.escopo_atual = self.escopo_raiz

    def entrar_escopo(self, nome_escopo="local"):
        # Adiciona um novo escopo como filho do atual e move o ponteiro para ele
        self.escopo_atual = self.escopo_atual.adicionar_filho(nome_escopo)

    def sair_escopo(self):
        # Apenas move o ponteiro para o escopo pai, sem apagar nada
        if self.escopo_atual.pai:
            self.escopo_atual = self.escopo_atual.pai

    def declarar(self, simbolo: Simbolo):
        return self.escopo_atual.declarar(simbolo)

    def buscar(self, nome):
        return self.escopo_atual.buscar(nome)

    def _imprimir_recursivo(self, escopo: Escopo, nivel=0):
        """ Função auxiliar para imprimir a árvore de escopos. """
        indentacao = "  " * nivel
        saida = f"{indentacao}--- Escopo: {escopo.nome} (Nível {nivel}) ---\n"

        if not escopo.simbolos:
            saida += f"{indentacao}  (vazio)\n"
        else:
            for nome, simbolo in escopo.simbolos.items():
                saida += f"{indentacao}  {simbolo}\n"

        for filho in escopo.filhos:
            saida += self._imprimir_recursivo(filho, nivel + 1)

        return saida

    def __str__(self):
        # Inicia a impressão a partir do escopo raiz
        return self._imprimir_recursivo(self.escopo_raiz)