// Generated from c:/Users/Yasmine Martins/Desktop/vsCode/universidade/sexto_periodo/Compiladores/Javython.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JavythonParser}.
 */
public interface JavythonListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JavythonParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(JavythonParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(JavythonParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(JavythonParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(JavythonParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#decIds}.
	 * @param ctx the parse tree
	 */
	void enterDecIds(JavythonParser.DecIdsContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#decIds}.
	 * @param ctx the parse tree
	 */
	void exitDecIds(JavythonParser.DecIdsContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(JavythonParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(JavythonParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#idList}.
	 * @param ctx the parse tree
	 */
	void enterIdList(JavythonParser.IdListContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#idList}.
	 * @param ctx the parse tree
	 */
	void exitIdList(JavythonParser.IdListContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(JavythonParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(JavythonParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#metodo}.
	 * @param ctx the parse tree
	 */
	void enterMetodo(JavythonParser.MetodoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#metodo}.
	 * @param ctx the parse tree
	 */
	void exitMetodo(JavythonParser.MetodoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(JavythonParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(JavythonParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(JavythonParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(JavythonParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#returnCmd}.
	 * @param ctx the parse tree
	 */
	void enterReturnCmd(JavythonParser.ReturnCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#returnCmd}.
	 * @param ctx the parse tree
	 */
	void exitReturnCmd(JavythonParser.ReturnCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(JavythonParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(JavythonParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(JavythonParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(JavythonParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#inputCmd}.
	 * @param ctx the parse tree
	 */
	void enterInputCmd(JavythonParser.InputCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#inputCmd}.
	 * @param ctx the parse tree
	 */
	void exitInputCmd(JavythonParser.InputCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#printCmd}.
	 * @param ctx the parse tree
	 */
	void enterPrintCmd(JavythonParser.PrintCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#printCmd}.
	 * @param ctx the parse tree
	 */
	void exitPrintCmd(JavythonParser.PrintCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#breakCmd}.
	 * @param ctx the parse tree
	 */
	void enterBreakCmd(JavythonParser.BreakCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#breakCmd}.
	 * @param ctx the parse tree
	 */
	void exitBreakCmd(JavythonParser.BreakCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#ifCmd}.
	 * @param ctx the parse tree
	 */
	void enterIfCmd(JavythonParser.IfCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#ifCmd}.
	 * @param ctx the parse tree
	 */
	void exitIfCmd(JavythonParser.IfCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#whileCmd}.
	 * @param ctx the parse tree
	 */
	void enterWhileCmd(JavythonParser.WhileCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#whileCmd}.
	 * @param ctx the parse tree
	 */
	void exitWhileCmd(JavythonParser.WhileCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#forCmd}.
	 * @param ctx the parse tree
	 */
	void enterForCmd(JavythonParser.ForCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#forCmd}.
	 * @param ctx the parse tree
	 */
	void exitForCmd(JavythonParser.ForCmdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code strExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterStrExpr(JavythonParser.StrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code strExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitStrExpr(JavythonParser.StrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterIntExpr(JavythonParser.IntExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitIntExpr(JavythonParser.IntExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code relacional}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterRelacional(JavythonParser.RelacionalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code relacional}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitRelacional(JavythonParser.RelacionalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code boolFalse}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterBoolFalse(JavythonParser.BoolFalseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code boolFalse}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitBoolFalse(JavythonParser.BoolFalseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code chamada}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterChamada(JavythonParser.ChamadaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code chamada}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitChamada(JavythonParser.ChamadaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code realExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterRealExpr(JavythonParser.RealExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code realExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitRealExpr(JavythonParser.RealExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code grupo}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterGrupo(JavythonParser.GrupoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code grupo}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitGrupo(JavythonParser.GrupoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(JavythonParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(JavythonParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code igualdade}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterIgualdade(JavythonParser.IgualdadeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code igualdade}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitIgualdade(JavythonParser.IgualdadeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(JavythonParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(JavythonParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code boolTrue}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterBoolTrue(JavythonParser.BoolTrueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code boolTrue}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitBoolTrue(JavythonParser.BoolTrueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryMinus}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(JavythonParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryMinus}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(JavythonParser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryNot}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterUnaryNot(JavythonParser.UnaryNotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryNot}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitUnaryNot(JavythonParser.UnaryNotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code idExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterIdExpr(JavythonParser.IdExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code idExpr}
	 * labeled alternative in {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitIdExpr(JavythonParser.IdExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#incremento}.
	 * @param ctx the parse tree
	 */
	void enterIncremento(JavythonParser.IncrementoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#incremento}.
	 * @param ctx the parse tree
	 */
	void exitIncremento(JavythonParser.IncrementoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#decremento}.
	 * @param ctx the parse tree
	 */
	void enterDecremento(JavythonParser.DecrementoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#decremento}.
	 * @param ctx the parse tree
	 */
	void exitDecremento(JavythonParser.DecrementoContext ctx);
	/**
	 * Enter a parse tree produced by {@link JavythonParser#chamadaFuncao}.
	 * @param ctx the parse tree
	 */
	void enterChamadaFuncao(JavythonParser.ChamadaFuncaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#chamadaFuncao}.
	 * @param ctx the parse tree
	 */
	void exitChamadaFuncao(JavythonParser.ChamadaFuncaoContext ctx);
}