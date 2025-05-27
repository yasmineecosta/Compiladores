// Generated from c:/Users/KM/Documents/Compilas/Compiladores/Javython.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(JavythonParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(JavythonParser.ExpressaoContext ctx);
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