# Trabalho-Final/tabela_simbolos.py (Refatorado com Suporte a Parâmetros de Métodos)

class Simbolo:
    """ Representa uma entrada na tabela de símbolos (variável, método, parâmetro). """
    def __init__(self, nome, tipo, categoria='variavel', linha=0, parametros=None):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria  # variavel, metodo ou parametro
        self.linha = linha
        self.parametros = parametros or []  # Somente para métodos

    def __str__(self):
        base = f"{self.nome} -> (Categoria: {self.categoria}, Tipo: {self.tipo}, Linha: {self.linha})"
        if self.parametros:
            params_str = ', '.join([f"{tipo} {nome}" for tipo, nome in self.parametros])
            base += f", Parâmetros: ({params_str})"
        return base


class Escopo:
    """ Representa um escopo com símbolos declarados e possíveis escopos filhos. """
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
    """ Gerencia a hierarquia de escopos para o analisador semântico. """
    def __init__(self):
        self.escopo_raiz = Escopo(nome="global")
        self.escopo_atual = self.escopo_raiz

    def entrar_escopo(self, nome_escopo="local"):
        self.escopo_atual = self.escopo_atual.adicionar_filho(nome_escopo)

    def sair_escopo(self):
        if self.escopo_atual.pai:
            self.escopo_atual = self.escopo_atual.pai

    def declarar(self, simbolo: Simbolo):
        return self.escopo_atual.declarar(simbolo)

    def buscar(self, nome):
        return self.escopo_atual.buscar(nome)

    def _imprimir_recursivo(self, escopo: Escopo, nivel=0):
        indentacao = "  " * nivel
        saida = f"{indentacao}--- Escopo: {escopo.nome} (Nível {nivel}) ---\n"

        if not escopo.simbolos:
            saida += f"{indentacao}  (vazio)\n"
        else:
            for simbolo in escopo.simbolos.values():
                saida += f"{indentacao}  {simbolo}\n"

        for filho in escopo.filhos:
            saida += self._imprimir_recursivo(filho, nivel + 1)

        return saida

    def __str__(self):
        return self._imprimir_recursivo(self.escopo_raiz)
