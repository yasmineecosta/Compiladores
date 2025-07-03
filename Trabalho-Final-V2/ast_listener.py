# ast_listener.py

from JavythonParser import JavythonParser
from JavythonListener import JavythonListener


class ASTListener(JavythonListener):
    def __init__(self):
        # Dicionário para mapear o ID de um nó da árvore à sua representação em string.
        self.ast_strings = {}

    def get_ast_string(self, ctx):
        return self.ast_strings.get(id(ctx), "")

    def set_ast_string(self, ctx, text):
        self.ast_strings[id(ctx)] = text

    # --- Regras de Saída (Construção Bottom-Up) ---

    def exitProgram(self, ctx: JavythonParser.ProgramContext):
        nome_programa = ctx.ID().getText()
        decls = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        metodos = ' '.join(self.get_ast_string(m) for m in ctx.metodo())
        main = self.get_ast_string(ctx.main())
        ast = f"(program {nome_programa} {decls} {metodos} {main})"
        self.set_ast_string(ctx, ' '.join(ast.split()))

    def exitMain(self, ctx: JavythonParser.MainContext):
        decls = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        comandos = ' '.join(self.get_ast_string(c) for c in ctx.comando())
        self.set_ast_string(ctx, f"(main {decls} (body {comandos}))")

    def exitMetodo(self, ctx: JavythonParser.MetodoContext):
        tipo = ctx.tipo().getText()
        nome = ctx.ID().getText()
        params = self.get_ast_string(ctx.parametros()) if ctx.parametros() else "(params)"
        decls = self.get_ast_string(ctx.decIds()) if ctx.decIds() else ""
        comandos = ' '.join(self.get_ast_string(c) for c in ctx.comando())
        self.set_ast_string(ctx, f"(method {tipo} {nome} {params} {decls} (body {comandos}))")

    def exitParametros(self, ctx: JavythonParser.ParametrosContext):
        params = ' '.join(self.get_ast_string(p) for p in ctx.parametro())
        self.set_ast_string(ctx, f"(params {params})")

    def exitParametro(self, ctx: JavythonParser.ParametroContext):
        self.set_ast_string(ctx, f"({ctx.tipo().getText()} {ctx.ID().getText()})")

    def exitDecIds(self, ctx: JavythonParser.DecIdsContext):
        decls = ' '.join(
            self.get_ast_string(d) for d in ctx.getChildren() if not isinstance(d, (JavythonParser.TerminalNode)))
        self.set_ast_string(ctx, f"(declarations {decls})")

    def exitDeclVar(self, ctx: JavythonParser.DeclVarContext):
        tipo = ctx.tipo().getText()
        ids = ' '.join(i.getText() for i in ctx.idList().ID())
        self.set_ast_string(ctx, f"(var {tipo} {ids})")

    def exitDeclConst(self, ctx: JavythonParser.DeclConstContext):
        expr = self.get_ast_string(ctx.expressao())
        self.set_ast_string(ctx, f"(const {ctx.ID().getText()} = {expr})")

    def exitComando(self, ctx: JavythonParser.ComandoContext):
        # Propaga a string do filho (atribuicao, ifCmd, etc.) para o nó 'comando'
        if ctx.getChildCount() > 0:
            self.set_ast_string(ctx, self.get_ast_string(ctx.getChild(0)))

    def exitAtribuicao(self, ctx: JavythonParser.AtribuicaoContext):
        expr = self.get_ast_string(ctx.expressao())
        self.set_ast_string(ctx, f"(assign {ctx.ID().getText()} {expr})")

    # --- Expressões ---
    def exitParensExpr(self, ctx: JavythonParser.ParensExprContext):
        self.set_ast_string(ctx, self.get_ast_string(ctx.expressao()))

    def exitUnaryExpr(self, ctx: JavythonParser.UnaryExprContext):
        self.set_ast_string(ctx, f"({ctx.op.text} {self.get_ast_string(ctx.expressao())})")

    def _exitBinaryExpr(self, ctx):
        esq = self.get_ast_string(ctx.expressao(0))
        dir = self.get_ast_string(ctx.expressao(1))
        self.set_ast_string(ctx, f"({ctx.op.text} {esq} {dir})")

    def exitMulDivExpr(self, ctx: JavythonParser.MulDivExprContext): self._exitBinaryExpr(ctx)

    def exitAddSubExpr(self, ctx: JavythonParser.AddSubExprContext): self._exitBinaryExpr(ctx)

    def exitCompExpr(self, ctx: JavythonParser.CompExprContext): self._exitBinaryExpr(ctx)

    def exitChamadaFuncao(self, ctx: JavythonParser.ChamadaFuncaoContext):
        args = ' '.join(self.get_ast_string(a) for a in ctx.expressao()) if ctx.expressao() else ""
        self.set_ast_string(ctx, f"(call {ctx.ID().getText()} {args})")

    def exitFuncCallExpr(self, ctx: JavythonParser.FuncCallExprContext):
        self.set_ast_string(ctx, self.get_ast_string(ctx.chamadaFuncao()))

    # --- Átomos ---
    def exitIdAtom(self, ctx: JavythonParser.IdAtomContext): self.set_ast_string(ctx, ctx.getText())

    def exitIntAtom(self, ctx: JavythonParser.IntAtomContext): self.set_ast_string(ctx, ctx.getText())

    def exitRealAtom(self, ctx: JavythonParser.RealAtomContext): self.set_ast_string(ctx, ctx.getText())

    def exitStringAtom(self, ctx: JavythonParser.StringAtomContext): self.set_ast_string(ctx, ctx.getText())

    def exitBoolAtom(self, ctx: JavythonParser.BoolAtomContext): self.set_ast_string(ctx, ctx.getText())