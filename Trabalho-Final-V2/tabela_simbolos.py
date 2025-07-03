# tabela_simbolos.py

class Simbolo:
    """ Representa uma entrada na tabela de símbolos (variável, constante, método, etc.). """
    def __init__(self, nome, tipo, categoria='variavel', linha=0, parametros=None, e_constante=False):
        self.nome = nome.lower()
        self.tipo = tipo
        self.categoria = categoria  # 'variavel', 'constante', 'metodo'
        self.linha = linha
        self.parametros = parametros if parametros is not None else []
        self.e_constante = e_constante

    def __str__(self):
        # Cria uma representação em string mais detalhada para a impressão da tabela.
        const_str = "[CONST] " if self.e_constante else ""
        cat_str = f"Categoria: {self.categoria}, Tipo: {self.tipo}"
        if self.categoria == 'metodo':
            params_str = ', '.join([f"{p_tipo} {p_nome}" for p_nome, p_tipo in self.parametros])
            return f"{const_str}{self.nome} -> ({cat_str}, Parâmetros: [{params_str}])"
        return f"{const_str}{self.nome} -> ({cat_str})"

class TabelaDeSimbolos:
    """ Gerencia a hierarquia de escopos para o analisador semântico. """
    def __init__(self):
        # O escopo raiz representa o escopo global.
        self.escopo_raiz = {"simbolos": {}, "pai": None, "filhos": []}
        self.escopo_atual = self.escopo_raiz

    def entrar_escopo(self):
        """ Cria um novo escopo filho do escopo atual e passa a ser o atual. """
        novo_escopo = {"simbolos": {}, "pai": self.escopo_atual, "filhos": []}
        self.escopo_atual["filhos"].append(novo_escopo)
        self.escopo_atual = novo_escopo

    def sair_escopo(self):
        """ Retorna ao escopo pai. """
        if self.escopo_atual["pai"] is not None:
            self.escopo_atual = self.escopo_atual["pai"]

    def declarar(self, simbolo: Simbolo):
        """ Declara um símbolo no escopo atual. Retorna False se já existir. """
        nome_simbolo = simbolo.nome
        if nome_simbolo in self.escopo_atual["simbolos"]:
            return False
        self.escopo_atual["simbolos"][nome_simbolo] = simbolo
        return True

    def buscar(self, nome):
        """ Busca um símbolo no escopo atual e nos escopos pais recursivamente. """
        nome_lower = nome.lower()
        escopo = self.escopo_atual
        while escopo is not None:
            if nome_lower in escopo["simbolos"]:
                return escopo["simbolos"][nome_lower]
            escopo = escopo["pai"]
        return None

    def _imprimir_recursivo(self, escopo, nivel=0):
        """ Função auxiliar para imprimir a tabela de forma aninhada. """
        indentacao = "  " * nivel
        saida = f"{indentacao}--- Escopo (Nível {nivel}) ---\n"
        if not escopo["simbolos"]:
            saida += f"{indentacao}  (vazio)\n"
        else:
            for simbolo in escopo["simbolos"].values():
                saida += f"{indentacao}  {simbolo}\n"
        for filho in escopo["filhos"]:
            saida += self._imprimir_recursivo(filho, nivel + 1)
        return saida

    def __str__(self):
        return self._imprimir_recursivo(self.escopo_raiz)