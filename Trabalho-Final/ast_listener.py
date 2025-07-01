# Trabalho-Final/ast_listener.py (Versão FINAL E CORRIGIDA)

from antlr4.tree.Tree import TerminalNode
from JavythonParser import JavythonParser
from JavythonListener import JavythonListener


class ASTListener(JavythonListener):
    def __init__(self):
        self.ast_strings = {}

    def get_ast_string(self, ctx):
        return self.ast_strings.get(id(ctx), "")

    def set_ast_string(self, ctx, text):
        self.ast_strings[id(ctx)] = text

    # --- Métodos Principais ---
    def exitProgram(self, ctx: JavythonParser.ProgramContext):
        nome_programa = ctx.ID().getText()
        declaracoes_str = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        metodos_str = ' '.join(filter(None, [self.get_ast_string(m) for m in ctx.metodo()]))
        main_str = self.get_ast_string(ctx.main())
        ast_final = f"(Program (Name {nome_programa}) {declaracoes_str} {metodos_str} {main_str})"
        self.set_ast_string(ctx, ' '.join(ast_final.split()))

    def exitMetodo(self, ctx: JavythonParser.MetodoContext):
        nome = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        params = self.get_ast_string(ctx.parametros()) if ctx.parametros() else "(Params)"
        declaracoes_str = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        comandos_str = ' '.join(filter(None, [self.get_ast_string(c) for c in ctx.comando()]))
        corpo = f"{declaracoes_str} {comandos_str}".strip()
        self.set_ast_string(ctx, f"(Method (Name {nome}) (Returns {tipo_retorno}) {params} (Body {corpo}))")

    def exitMain(self, ctx: JavythonParser.MainContext):
        declaracoes_str = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        comandos_str = ' '.join(filter(None, [self.get_ast_string(cmd) for cmd in ctx.comando()]))
        self.set_ast_string(ctx, f"(Main {declaracoes_str} {comandos_str})".strip())

    # --- Declarações e Parâmetros ---
    def exitDecIds(self, ctx: JavythonParser.DecIdsContext):
        decls = ' '.join(self.get_ast_string(d) for d in ctx.decl())
        self.set_ast_string(ctx, f"(Declarations {decls})")

    def exitDecl(self, ctx: JavythonParser.DeclContext):
        tipo = ctx.tipo().getText()
        variaveis = ' '.join([var.getText() for var in ctx.idList().ID()])
        self.set_ast_string(ctx, f"(Declare (Type {tipo}) (Vars {variaveis}))")

    def exitParametros(self, ctx: JavythonParser.ParametrosContext):
        params = ' '.join(self.get_ast_string(p) for p in ctx.parametro())
        self.set_ast_string(ctx, f"(Params {params})")

    def exitParametro(self, ctx: JavythonParser.ParametroContext):
        self.set_ast_string(ctx, f"(Param (Type {ctx.tipo().getText()}) (Name {ctx.ID().getText()}))")

    # --- Comandos ---
    def exitComando(self, ctx: JavythonParser.ComandoContext):
        if ctx.getChildCount() > 0:
            child_str = self.get_ast_string(ctx.getChild(0))
            if child_str:  # Propaga apenas se não for vazio
                self.set_ast_string(ctx, child_str)

    def exitReturnCmd(self, ctx: JavythonParser.ReturnCmdContext):
        expr = self.get_ast_string(ctx.expressao())
        self.set_ast_string(ctx, f"(Return {expr})")

    def exitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        var = ctx.ID().getText()
        expr = self.get_ast_string(ctx.expressao())
        self.set_ast_string(ctx, f"(Assign (Var {var}) {expr})")

    def exitInputCmd(self, ctx: JavythonParser.InputCmdContext):
        ids = ' '.join([node.getText() for node in ctx.idList().ID()])
        self.set_ast_string(ctx, f"(Input (Vars {ids}))")

    def exitPrintCmd(self, ctx: JavythonParser.PrintCmdContext):
        args = ' '.join([self.get_ast_string(e) for e in ctx.expressao()])
        self.set_ast_string(ctx, f"(Print {args})")

    # <<<<<<<<<<<<<<<<<<<< FUNÇÃO CORRIGIDA >>>>>>>>>>>>>>>>>>>>
    def exitIfCmd(self, ctx: JavythonParser.IfCmdContext):
        cond = self.get_ast_string(ctx.expressao())

        all_commands_ctx = ctx.comando()
        if_commands = []
        else_commands = []

        # Encontra o token 'else' para saber onde dividir os comandos
        else_token = None
        for child in ctx.children:
            if isinstance(child, TerminalNode) and child.getSymbol().text == 'else':
                else_token = child
                break

        if else_token:
            else_token_index = else_token.getSymbol().tokenIndex
            for cmd_ctx in all_commands_ctx:
                if cmd_ctx.start.tokenIndex < else_token_index:
                    if_commands.append(self.get_ast_string(cmd_ctx))
                else:
                    else_commands.append(self.get_ast_string(cmd_ctx))
        else:
            # Se não há 'else', todos os comandos pertencem ao 'if'
            if_commands = [self.get_ast_string(cmd_ctx) for cmd_ctx in all_commands_ctx]

        if_body = ' '.join(filter(None, if_commands))
        ast_str = f"(If (Cond {cond}) (Then {if_body})"

        if else_commands:
            else_body = ' '.join(filter(None, else_commands))
            ast_str += f" (Else {else_body})"

        ast_str += ")"
        self.set_ast_string(ctx, ast_str)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def exitForCmd(self, ctx: JavythonParser.ForCmdContext):
        init = self.get_ast_string(ctx.atribuicaoFor(0)) if ctx.atribuicaoFor() else "()"
        cond = self.get_ast_string(ctx.expressao()) if ctx.expressao() else "()"

        # Lógica para o incremento
        incr = "()"
        if ctx.incDecFor():
            incr = self.get_ast_string(ctx.incDecFor())
        elif len(ctx.atribuicaoFor()) > 1:  # Se a atribuição inicial existir
            incr = self.get_ast_string(ctx.atribuicaoFor(1))

        corpo = ' '.join(self.get_ast_string(c) for c in ctx.comando())
        self.set_ast_string(ctx, f"(For (Init {init}) (Cond {cond}) (Incr {incr}) (Body {corpo}))")

    def exitAtribuicaoFor(self, ctx: JavythonParser.AtribuicaoForContext):
        self.set_ast_string(ctx, f"(Assign (Var {ctx.ID().getText()}) {self.get_ast_string(ctx.expressao())})")

    def exitIncDecFor(self, ctx: JavythonParser.IncDecForContext):
        op = '++' if ctx.getChild(1).getSymbol().type == JavythonParser.T__25 else '--'
        self.set_ast_string(ctx, f"({op} (ID {ctx.ID().getText()}))")

    # --- Expressões ---
    def exitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext):
        self.set_ast_string(ctx,
                            f"({ctx.op.text} {self.get_ast_string(ctx.expressao(0))} {self.get_ast_string(ctx.expressao(1))})")

    def exitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext):
        self.set_ast_string(ctx,
                            f"({ctx.op.text} {self.get_ast_string(ctx.expressao(0))} {self.get_ast_string(ctx.expressao(1))})")

    def exitCompExpr(self, ctx: JavythonParser.CompExprContext):
        self.set_ast_string(ctx,
                            f"({ctx.op.text} {self.get_ast_string(ctx.expressao(0))} {self.get_ast_string(ctx.expressao(1))})")

    def exitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        self.set_ast_string(ctx, f"({ctx.op.text} {self.get_ast_string(ctx.expressao())})")

    def exitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        self.set_ast_string(ctx, self.get_ast_string(ctx.expressao()))

    def exitChamadaFuncao(self, ctx: JavythonParser.ChamadaFuncaoContext):
        nome = ctx.ID().getText()
        args_str = ' '.join(self.get_ast_string(arg) for arg in ctx.expressao())
        self.set_ast_string(ctx, f"(Call (Name {nome}) (Args {args_str}))")

    # --- Átomos ---
    def exitIdAtom(self, ctx: JavythonParser.IdAtomContext):
        self.set_ast_string(ctx, f"(ID {ctx.getText()})")

    def exitIntAtom(self, ctx: JavythonParser.IntAtomContext):
        self.set_ast_string(ctx, f"(Int {ctx.getText()})")

    def exitRealAtom(self, ctx: JavythonParser.RealAtomContext):
        self.set_ast_string(ctx, f"(Real {ctx.getText()})")

    def exitStringAtom(self, ctx: JavythonParser.StringAtomContext):
        self.set_ast_string(ctx, f"(String {ctx.getText()})")

    def exitBoolAtom(self, ctx: JavythonParser.BoolAtomContext):
        self.set_ast_string(ctx, f"(Bool {ctx.getText()})")

    def exitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        self.set_ast_string(ctx, self.get_ast_string(ctx.chamadaFuncao()))