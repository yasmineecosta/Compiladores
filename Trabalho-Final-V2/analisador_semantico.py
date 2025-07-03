# analisador_semantico.py

from JavythonParser import JavythonParser
from JavythonListener import JavythonListener
from JavythonVisitor import JavythonVisitor
from tabela_simbolos import TabelaDeSimbolos, Simbolo


# ==============================================================================
# Visitor dedicado a determinar o tipo de qualquer nó de expressão.
# Esta é a abordagem correta, pois a análise de tipo de expressão é recursiva.
# ==============================================================================
class ExpressionTypeVisitor(JavythonVisitor):
    def __init__(self, tabela: TabelaDeSimbolos, erros: list):
        self.tabela = tabela
        self.erros = erros

    def reportar_erro(self, linha, mensagem):
        erro_msg = f"Linha {linha}: {mensagem}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)

    # Átomos: retornam seu tipo literal.
    def visitIntAtom(self, ctx):
        return "int"

    def visitRealAtom(self, ctx):
        return "real"

    def visitStringAtom(self, ctx):
        return "str"

    def visitBoolAtom(self, ctx):
        return "bool"

    # ID: busca na tabela de símbolos para encontrar o tipo.
    def visitIdAtom(self, ctx):
        nome = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome)
        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Identificador '{nome}' não declarado.")
            return "erro"
        return simbolo.tipo

    # Expressões com parênteses: o tipo é o tipo da expressão interna.
    def visitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        return self.visit(ctx.expressao())

    # Operador unário: verifica o tipo e retorna o tipo resultante.
    def visitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        tipo_expr = self.visit(ctx.expressao())
        op = ctx.op.text
        if op == '!':
            if tipo_expr != 'bool':
                self.reportar_erro(ctx.start.line,
                                   f"Operador '!' só pode ser aplicado a booleanos, não a '{tipo_expr}'.")
            return 'bool'
        if op == '-':
            if tipo_expr not in ['int', 'real']:
                self.reportar_erro(ctx.start.line,
                                   f"Operador unário '-' só pode ser aplicado a tipos numéricos, não a '{tipo_expr}'.")
            return tipo_expr
        return 'erro'

    # Operadores binários: verificam a compatibilidade e retornam o tipo resultante.
    def _verificar_operacao_numerica(self, ctx):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if 'erro' in [tipo_esq, tipo_dir]: return 'erro'

        if not (tipo_esq in ['int', 'real'] and tipo_dir in ['int', 'real']):
            self.reportar_erro(ctx.start.line,
                               f"Operador '{ctx.op.text}' só pode ser aplicado a tipos numéricos, não a '{tipo_esq}' e '{tipo_dir}'.")
            return 'erro'
        # Promove para real se um dos operandos for real
        return 'real' if 'real' in [tipo_esq, tipo_dir] else 'int'

    def visitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        return self._verificar_operacao_numerica(ctx)

    def visitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))

        # Se for concatenação de string
        if ctx.op.text == '+' and ('str' in [tipo_esq, tipo_dir]):
            return 'str'

        # Senão, trata como operação numérica
        return self._verificar_operacao_numerica(ctx)

    def visitCompExpr(self, ctx: JavythonParser.CompExprContext):
        tipo_esq = self.visit(ctx.expressao(0))
        tipo_dir = self.visit(ctx.expressao(1))
        if 'erro' in [tipo_esq, tipo_dir]: return 'erro'

        # Permite comparação entre tipos numéricos
        numericos_compativeis = tipo_esq in ['int', 'real'] and tipo_dir in ['int', 'real']
        # Permite comparação apenas entre tipos iguais (ex: bool com bool, str com str)
        tipos_iguais_compativeis = tipo_esq == tipo_dir

        if not (numericos_compativeis or tipos_iguais_compativeis):
            self.reportar_erro(ctx.start.line, f"Comparação entre tipos incompatíveis: '{tipo_esq}' e '{tipo_dir}'.")
        return 'bool'

    # Chamada de função: verifica a existência, o número e tipo dos parâmetros.
    def visitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        return self.visit(ctx.chamadaFuncao())  # Delega para a regra de chamada de função

    def visitChamadaFuncao(self, ctx: JavythonParser.ChamadaFuncaoContext):
        nome_func = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome_func)

        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Função '{nome_func}' não declarada.")
            return 'erro'
        if simbolo.categoria != 'metodo':
            self.reportar_erro(ctx.start.line,
                               f"'{nome_func}' é um(a) '{simbolo.categoria}' e não pode ser chamado como uma função.")
            return 'erro'

        # Validação de argumentos para funções que não sejam 'print' ou 'input'
        if nome_func not in ['print', 'input']:
            args_passados = ctx.expressao()
            params_esperados = simbolo.parametros
            if len(args_passados) != len(params_esperados):
                self.reportar_erro(ctx.start.line,
                                   f"Função '{nome_func}' espera {len(params_esperados)} argumento(s), mas recebeu {len(args_passados)}.")
                return simbolo.tipo  # Retorna o tipo esperado para evitar erros em cascata

            for i, arg_ctx in enumerate(args_passados):
                tipo_arg = self.visit(arg_ctx)
                tipo_param_esperado = params_esperados[i][1]
                if tipo_arg != 'erro' and tipo_arg != tipo_param_esperado and not (
                        tipo_param_esperado == 'real' and tipo_arg == 'int'):
                    self.reportar_erro(arg_ctx.start.line,
                                       f"Argumento {i + 1} da função '{nome_func}' é do tipo '{tipo_arg}', mas o esperado era '{tipo_param_esperado}'.")

        return simbolo.tipo


# ==============================================================================
# Listener principal para caminhar na árvore, gerenciar escopos e validar
# declarações e comandos.
# ==============================================================================
class AnalisadorSemantico(JavythonListener):
    def __init__(self):
        self.tabela = TabelaDeSimbolos()
        self.erros = []
        self.expression_visitor = ExpressionTypeVisitor(self.tabela, self.erros)

    def reportar_erro(self, linha, mensagem):
        erro_msg = f"Linha {linha}: {mensagem}"
        if erro_msg not in self.erros:
            self.erros.append(erro_msg)

    # --- Gerenciamento de Escopo e Declarações ---

    def enterProgram(self, ctx: JavythonParser.ProgramContext):
        # Declara funções nativas no escopo global
        self.tabela.declarar(Simbolo('print', 'void', 'metodo'))
        self.tabela.declarar(Simbolo('input', 'void', 'metodo'))

    def enterMetodo(self, ctx: JavythonParser.MetodoContext):
        nome = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        linha = ctx.start.line

        parametros = []
        if ctx.parametros():
            for p_ctx in ctx.parametros().parametro():
                parametros.append((p_ctx.ID().getText(), p_ctx.tipo().getText()))

        simbolo_metodo = Simbolo(nome, tipo_retorno, 'metodo', linha, parametros)
        if not self.tabela.declarar(simbolo_metodo):
            self.reportar_erro(linha, f"Símbolo '{nome}' já foi declarado neste escopo.")

        self.tabela.entrar_escopo()
        for p_nome, p_tipo in parametros:
            self.tabela.declarar(Simbolo(p_nome, p_tipo, 'parametro', linha))

    def exitMetodo(self, ctx: JavythonParser.MetodoContext):
        self.tabela.sair_escopo()

    def enterMain(self, ctx: JavythonParser.MainContext):
        self.tabela.entrar_escopo()

    def exitMain(self, ctx: JavythonParser.MainContext):
        self.tabela.sair_escopo()

    def exitDeclVar(self, ctx: JavythonParser.DeclVarContext):
        tipo = ctx.tipo().getText()
        for id_node in ctx.idList().ID():
            nome = id_node.getText()
            linha = id_node.getSymbol().line
            if not self.tabela.declarar(Simbolo(nome, tipo, 'variavel', linha)):
                self.reportar_erro(linha, f"Símbolo '{nome}' já foi declarado neste escopo.")

    def exitDeclConst(self, ctx: JavythonParser.DeclConstContext):
        nome = ctx.ID().getText()
        linha = ctx.start.line
        tipo_expr = self.expression_visitor.visit(ctx.expressao())

        if tipo_expr != 'erro':
            simbolo = Simbolo(nome, tipo_expr, 'constante', linha, e_constante=True)
            if not self.tabela.declarar(simbolo):
                self.reportar_erro(linha, f"Símbolo '{nome}' já foi declarado neste escopo.")

    # --- Validação de Comandos ---

    def exitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        nome = ctx.ID().getText()
        simbolo = self.tabela.buscar(nome)

        if not simbolo:
            self.reportar_erro(ctx.start.line, f"Atribuição a uma variável não declarada '{nome}'.")
            return
        if simbolo.e_constante:
            self.reportar_erro(ctx.start.line, f"Não é possível fazer uma atribuição a uma constante '{nome}'.")
            return

        tipo_expr = self.expression_visitor.visit(ctx.expressao())
        tipo_var = simbolo.tipo

        if tipo_expr != 'erro' and tipo_var != tipo_expr and not (tipo_var == 'real' and tipo_expr == 'int'):
            self.reportar_erro(ctx.start.line,
                               f"Tipo incompatível para atribuição. Variável '{nome}' é do tipo '{tipo_var}', mas recebeu '{tipo_expr}'.")

    def exitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        tipo_cond = self.expression_visitor.visit(ctx.expressao())
        if tipo_cond != 'bool' and tipo_cond != 'erro':
            self.reportar_erro(ctx.expressao().start.line,
                               f"Condição do 'if' deve ser booleana, mas é do tipo '{tipo_cond}'.")

    def exitWhileCmd(self, ctx: JavythonParser.WhileCmdContext):
        tipo_cond = self.expression_visitor.visit(ctx.expressao())
        if tipo_cond != 'bool' and tipo_cond != 'erro':
            self.reportar_erro(ctx.expressao().start.line,
                               f"Condição do 'while' deve ser booleana, mas é do tipo '{tipo_cond}'.")

    def exitForCmd(self, ctx: JavythonParser.ForCmdContext):
        if ctx.expressao():  # Condição de parada é opcional
            tipo_cond = self.expression_visitor.visit(ctx.expressao())
            if tipo_cond != 'bool' and tipo_cond != 'erro':
                self.reportar_erro(ctx.expressao().start.line,
                                   f"Condição do 'for' deve ser booleana, mas é do tipo '{tipo_cond}'.")