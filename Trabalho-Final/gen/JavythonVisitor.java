// Generated from C:/Users/Yasmine Martins/Desktop/vsCode/universidade/sexto_periodo/Compiladores/Javython.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link JavythonParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface JavythonVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link JavythonParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(JavythonParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#main}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMain(JavythonParser.MainContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#decIds}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecIds(JavythonParser.DecIdsContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl(JavythonParser.DeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#idList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdList(JavythonParser.IdListContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#tipo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo(JavythonParser.TipoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#metodo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMetodo(JavythonParser.MetodoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#parametros}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParametros(JavythonParser.ParametrosContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#parametro}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParametro(JavythonParser.ParametroContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#returnCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnCmd(JavythonParser.ReturnCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#comando}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComando(JavythonParser.ComandoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#atribuicao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtribuicao(JavythonParser.AtribuicaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#inputCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInputCmd(JavythonParser.InputCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#printCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintCmd(JavythonParser.PrintCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#breakCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakCmd(JavythonParser.BreakCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#atribuicaoFor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtribuicaoFor(JavythonParser.AtribuicaoForContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#ifCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfCmd(JavythonParser.IfCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#whileCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileCmd(JavythonParser.WhileCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#forCmd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForCmd(JavythonParser.ForCmdContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#expressao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao(JavythonParser.ExpressaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#incremento}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIncremento(JavythonParser.IncrementoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#decremento}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecremento(JavythonParser.DecrementoContext ctx);
	/**
	 * Visit a parse tree produced by {@link JavythonParser#chamadaFuncao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChamadaFuncao(JavythonParser.ChamadaFuncaoContext ctx);
}