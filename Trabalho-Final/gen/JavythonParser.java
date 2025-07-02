// Generated from C:/Users/Yasmine Martins/Desktop/vsCode/universidade/sexto_periodo/Compiladores/Trabalho-Final/Javython.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class JavythonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		ID=39, NUM_INT=40, NUM_REAL=41, STRING=42, WS=43, COMMENT=44;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_decIds = 2, RULE_decl = 3, RULE_idList = 4, 
		RULE_tipo = 5, RULE_metodo = 6, RULE_parametros = 7, RULE_parametro = 8, 
		RULE_returnCmd = 9, RULE_comando = 10, RULE_atribuicao = 11, RULE_inputCmd = 12, 
		RULE_printCmd = 13, RULE_breakCmd = 14, RULE_ifCmd = 15, RULE_whileCmd = 16, 
		RULE_forCmd = 17, RULE_atribuicaoFor = 18, RULE_incDecFor = 19, RULE_expressao = 20, 
		RULE_incremento = 21, RULE_decremento = 22, RULE_chamadaFuncao = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "decIds", "decl", "idList", "tipo", "metodo", "parametros", 
			"parametro", "returnCmd", "comando", "atribuicao", "inputCmd", "printCmd", 
			"breakCmd", "ifCmd", "whileCmd", "forCmd", "atribuicaoFor", "incDecFor", 
			"expressao", "incremento", "decremento", "chamadaFuncao"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "':'", "';'", "'end'", "'main'", "'decIds'", "','", 
			"'int'", "'real'", "'str'", "'bool'", "'void'", "'('", "')'", "'{'", 
			"'}'", "'return'", "'='", "'input'", "'print'", "'break'", "'if'", "'else'", 
			"'while'", "'for'", "'++'", "'--'", "'!'", "'-'", "'*'", "'/'", "'+'", 
			"'=='", "'!='", "'>'", "'<'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "NUM_INT", "NUM_REAL", "STRING", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Javython.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JavythonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public DecIdsContext decIds() {
			return getRuleContext(DecIdsContext.class,0);
		}
		public List<MetodoContext> metodo() {
			return getRuleContexts(MetodoContext.class);
		}
		public MetodoContext metodo(int i) {
			return getRuleContext(MetodoContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__0);
			setState(49);
			match(T__1);
			setState(50);
			match(ID);
			setState(51);
			match(T__2);
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(52);
				decIds();
				}
			}

			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7936L) != 0)) {
				{
				{
				setState(55);
				metodo();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
			main();
			setState(62);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MainContext extends ParserRuleContext {
		public DecIdsContext decIds() {
			return getRuleContext(DecIdsContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterMain(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitMain(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitMain(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(T__4);
			setState(65);
			match(T__1);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(66);
				decIds();
				}
			}

			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(69);
				comando();
				}
				}
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DecIdsContext extends ParserRuleContext {
		public List<DeclContext> decl() {
			return getRuleContexts(DeclContext.class);
		}
		public DeclContext decl(int i) {
			return getRuleContext(DeclContext.class,i);
		}
		public DecIdsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decIds; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterDecIds(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitDecIds(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitDecIds(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DecIdsContext decIds() throws RecognitionException {
		DecIdsContext _localctx = new DecIdsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_decIds);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__5);
			setState(76);
			match(T__1);
			setState(80); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(77);
					decl();
					setState(78);
					match(T__2);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(82); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclContext extends ParserRuleContext {
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			idList();
			setState(85);
			match(T__1);
			setState(86);
			tipo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(JavythonParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(JavythonParser.ID, i);
		}
		public IdListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIdList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIdList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIdList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_idList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(ID);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(89);
				match(T__6);
				setState(90);
				match(ID);
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitTipo(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitTipo(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7936L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MetodoContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public DecIdsContext decIds() {
			return getRuleContext(DecIdsContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public MetodoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterMetodo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitMetodo(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitMetodo(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MetodoContext metodo() throws RecognitionException {
		MetodoContext _localctx = new MetodoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_metodo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			tipo();
			setState(99);
			match(ID);
			setState(100);
			match(T__12);
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7936L) != 0)) {
				{
				setState(101);
				parametros();
				}
			}

			setState(104);
			match(T__13);
			setState(105);
			match(T__14);
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(106);
				decIds();
				}
			}

			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(109);
				comando();
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(115);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosContext extends ParserRuleContext {
		public List<ParametroContext> parametro() {
			return getRuleContexts(ParametroContext.class);
		}
		public ParametroContext parametro(int i) {
			return getRuleContext(ParametroContext.class,i);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterParametros(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitParametros(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitParametros(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parametros);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			parametro();
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(118);
				match(T__6);
				setState(119);
				parametro();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametroContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public ParametroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametro; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterParametro(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitParametro(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitParametro(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParametroContext parametro() throws RecognitionException {
		ParametroContext _localctx = new ParametroContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parametro);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			tipo();
			setState(126);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnCmdContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public ReturnCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterReturnCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitReturnCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitReturnCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReturnCmdContext returnCmd() throws RecognitionException {
		ReturnCmdContext _localctx = new ReturnCmdContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_returnCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__16);
			setState(129);
			expressao(0);
			setState(130);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public InputCmdContext inputCmd() {
			return getRuleContext(InputCmdContext.class,0);
		}
		public PrintCmdContext printCmd() {
			return getRuleContext(PrintCmdContext.class,0);
		}
		public IfCmdContext ifCmd() {
			return getRuleContext(IfCmdContext.class,0);
		}
		public WhileCmdContext whileCmd() {
			return getRuleContext(WhileCmdContext.class,0);
		}
		public ForCmdContext forCmd() {
			return getRuleContext(ForCmdContext.class,0);
		}
		public BreakCmdContext breakCmd() {
			return getRuleContext(BreakCmdContext.class,0);
		}
		public IncrementoContext incremento() {
			return getRuleContext(IncrementoContext.class,0);
		}
		public DecrementoContext decremento() {
			return getRuleContext(DecrementoContext.class,0);
		}
		public ReturnCmdContext returnCmd() {
			return getRuleContext(ReturnCmdContext.class,0);
		}
		public ChamadaFuncaoContext chamadaFuncao() {
			return getRuleContext(ChamadaFuncaoContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterComando(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitComando(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitComando(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comando);
		try {
			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				atribuicao();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				inputCmd();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(134);
				printCmd();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(135);
				ifCmd();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(136);
				whileCmd();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(137);
				forCmd();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(138);
				breakCmd();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(139);
				incremento();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(140);
				decremento();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(141);
				returnCmd();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(142);
				chamadaFuncao();
				setState(143);
				match(T__2);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribuicaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterAtribuicao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitAtribuicao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitAtribuicao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(ID);
			setState(148);
			match(T__17);
			setState(149);
			expressao(0);
			setState(150);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputCmdContext extends ParserRuleContext {
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public InputCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterInputCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitInputCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitInputCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InputCmdContext inputCmd() throws RecognitionException {
		InputCmdContext _localctx = new InputCmdContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_inputCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(T__18);
			setState(153);
			match(T__12);
			setState(154);
			idList();
			setState(155);
			match(T__13);
			setState(156);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintCmdContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public PrintCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterPrintCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitPrintCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitPrintCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrintCmdContext printCmd() throws RecognitionException {
		PrintCmdContext _localctx = new PrintCmdContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_printCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(T__19);
			setState(159);
			match(T__12);
			setState(160);
			expressao(0);
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(161);
				match(T__6);
				setState(162);
				expressao(0);
				}
				}
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(168);
			match(T__13);
			setState(169);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakCmdContext extends ParserRuleContext {
		public BreakCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterBreakCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitBreakCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitBreakCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BreakCmdContext breakCmd() throws RecognitionException {
		BreakCmdContext _localctx = new BreakCmdContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_breakCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(T__20);
			setState(172);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfCmdContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public IfCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIfCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIfCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIfCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfCmdContext ifCmd() throws RecognitionException {
		IfCmdContext _localctx = new IfCmdContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ifCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(T__21);
			setState(175);
			match(T__12);
			setState(176);
			expressao(0);
			setState(177);
			match(T__13);
			setState(178);
			match(T__14);
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(179);
				comando();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(185);
			match(T__15);
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(186);
				match(T__22);
				setState(187);
				match(T__14);
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
					{
					{
					setState(188);
					comando();
					}
					}
					setState(193);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(194);
				match(T__15);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileCmdContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public WhileCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterWhileCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitWhileCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitWhileCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileCmdContext whileCmd() throws RecognitionException {
		WhileCmdContext _localctx = new WhileCmdContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(T__23);
			setState(198);
			match(T__12);
			setState(199);
			expressao(0);
			setState(200);
			match(T__13);
			setState(201);
			match(T__14);
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(202);
				comando();
				}
				}
				setState(207);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(208);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForCmdContext extends ParserRuleContext {
		public List<AtribuicaoForContext> atribuicaoFor() {
			return getRuleContexts(AtribuicaoForContext.class);
		}
		public AtribuicaoForContext atribuicaoFor(int i) {
			return getRuleContext(AtribuicaoForContext.class,i);
		}
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public IncDecForContext incDecFor() {
			return getRuleContext(IncDecForContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public ForCmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forCmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterForCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitForCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitForCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ForCmdContext forCmd() throws RecognitionException {
		ForCmdContext _localctx = new ForCmdContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_forCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(T__24);
			setState(211);
			match(T__12);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(212);
				atribuicaoFor();
				}
			}

			setState(215);
			match(T__2);
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8659459383296L) != 0)) {
				{
				setState(216);
				expressao(0);
				}
			}

			setState(219);
			match(T__2);
			setState(222);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(220);
				atribuicaoFor();
				}
				break;
			case 2:
				{
				setState(221);
				incDecFor();
				}
				break;
			}
			setState(224);
			match(T__13);
			setState(225);
			match(T__14);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(226);
				comando();
				}
				}
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(232);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribuicaoForContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public AtribuicaoForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicaoFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterAtribuicaoFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitAtribuicaoFor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitAtribuicaoFor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtribuicaoForContext atribuicaoFor() throws RecognitionException {
		AtribuicaoForContext _localctx = new AtribuicaoForContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_atribuicaoFor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(ID);
			setState(235);
			match(T__17);
			setState(236);
			expressao(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncDecForContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public IncDecForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incDecFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIncDecFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIncDecFor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIncDecFor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IncDecForContext incDecFor() throws RecognitionException {
		IncDecForContext _localctx = new IncDecForContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_incDecFor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(ID);
			setState(239);
			_la = _input.LA(1);
			if ( !(_la==T__25 || _la==T__26) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressaoContext extends ParserRuleContext {
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	 
		public ExpressaoContext() { }
		public void copyFrom(ExpressaoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RealAtomContext extends ExpressaoContext {
		public TerminalNode NUM_REAL() { return getToken(JavythonParser.NUM_REAL, 0); }
		public RealAtomContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterRealAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitRealAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitRealAtom(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivExprContext extends ExpressaoContext {
		public Token op;
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public MulDivExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterMulDivExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitMulDivExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitMulDivExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringAtomContext extends ExpressaoContext {
		public TerminalNode STRING() { return getToken(JavythonParser.STRING, 0); }
		public StringAtomContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterStringAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitStringAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitStringAtom(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolAtomContext extends ExpressaoContext {
		public BoolAtomContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterBoolAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitBoolAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitBoolAtom(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensExprContext extends ExpressaoContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public ParensExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterParensExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitParensExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitParensExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompExprContext extends ExpressaoContext {
		public Token op;
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public CompExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterCompExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitCompExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitCompExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExprContext extends ExpressaoContext {
		public Token op;
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public UnaryExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterUnaryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitUnaryExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitUnaryExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntAtomContext extends ExpressaoContext {
		public TerminalNode NUM_INT() { return getToken(JavythonParser.NUM_INT, 0); }
		public IntAtomContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIntAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIntAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIntAtom(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubExprContext extends ExpressaoContext {
		public Token op;
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public AddSubExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterAddSubExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitAddSubExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitAddSubExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdAtomContext extends ExpressaoContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public IdAtomContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIdAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIdAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIdAtom(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncCallExprContext extends ExpressaoContext {
		public ChamadaFuncaoContext chamadaFuncao() {
			return getRuleContext(ChamadaFuncaoContext.class,0);
		}
		public FuncCallExprContext(ExpressaoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterFuncCallExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitFuncCallExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitFuncCallExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		return expressao(0);
	}

	private ExpressaoContext expressao(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, _parentState);
		ExpressaoContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expressao, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				_localctx = new ParensExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(242);
				match(T__12);
				setState(243);
				expressao(0);
				setState(244);
				match(T__13);
				}
				break;
			case 2:
				{
				_localctx = new UnaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(246);
				((UnaryExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==T__27 || _la==T__28) ) {
					((UnaryExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(247);
				expressao(11);
				}
				break;
			case 3:
				{
				_localctx = new FuncCallExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(248);
				chamadaFuncao();
				}
				break;
			case 4:
				{
				_localctx = new IdAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(249);
				match(ID);
				}
				break;
			case 5:
				{
				_localctx = new IntAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(250);
				match(NUM_INT);
				}
				break;
			case 6:
				{
				_localctx = new RealAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(251);
				match(NUM_REAL);
				}
				break;
			case 7:
				{
				_localctx = new StringAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(252);
				match(STRING);
				}
				break;
			case 8:
				{
				_localctx = new BoolAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(253);
				match(T__36);
				}
				break;
			case 9:
				{
				_localctx = new BoolAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(254);
				match(T__37);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(268);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(266);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivExprContext(new ExpressaoContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(257);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(258);
						((MulDivExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__29 || _la==T__30) ) {
							((MulDivExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(259);
						expressao(11);
						}
						break;
					case 2:
						{
						_localctx = new AddSubExprContext(new ExpressaoContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(260);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(261);
						((AddSubExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__28 || _la==T__31) ) {
							((AddSubExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(262);
						expressao(10);
						}
						break;
					case 3:
						{
						_localctx = new CompExprContext(new ExpressaoContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(263);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(264);
						((CompExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 128849018880L) != 0)) ) {
							((CompExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(265);
						expressao(9);
						}
						break;
					}
					} 
				}
				setState(270);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncrementoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public IncrementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incremento; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterIncremento(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitIncremento(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitIncremento(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IncrementoContext incremento() throws RecognitionException {
		IncrementoContext _localctx = new IncrementoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_incremento);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(ID);
			setState(272);
			match(T__25);
			setState(273);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DecrementoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public DecrementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decremento; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterDecremento(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitDecremento(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitDecremento(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DecrementoContext decremento() throws RecognitionException {
		DecrementoContext _localctx = new DecrementoContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_decremento);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(ID);
			setState(276);
			match(T__26);
			setState(277);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChamadaFuncaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public ChamadaFuncaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chamadaFuncao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).enterChamadaFuncao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JavythonListener ) ((JavythonListener)listener).exitChamadaFuncao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof JavythonVisitor ) return ((JavythonVisitor<? extends T>)visitor).visitChamadaFuncao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ChamadaFuncaoContext chamadaFuncao() throws RecognitionException {
		ChamadaFuncaoContext _localctx = new ChamadaFuncaoContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_chamadaFuncao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			match(ID);
			setState(280);
			match(T__12);
			setState(289);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8659459383296L) != 0)) {
				{
				setState(281);
				expressao(0);
				setState(286);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__6) {
					{
					{
					setState(282);
					match(T__6);
					setState(283);
					expressao(0);
					}
					}
					setState(288);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(291);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 20:
			return expressao_sempred((ExpressaoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expressao_sempred(ExpressaoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001,\u0126\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u00006\b\u0000\u0001\u0000"+
		"\u0005\u00009\b\u0000\n\u0000\f\u0000<\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001D\b\u0001"+
		"\u0001\u0001\u0005\u0001G\b\u0001\n\u0001\f\u0001J\t\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0004\u0002Q\b\u0002"+
		"\u000b\u0002\f\u0002R\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\\\b\u0004\n\u0004\f\u0004"+
		"_\t\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006g\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006l\b\u0006\u0001\u0006\u0005\u0006o\b\u0006\n\u0006\f\u0006"+
		"r\t\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007y\b\u0007\n\u0007\f\u0007|\t\u0007\u0001\b\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u0092\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u00a4\b\r\n\r\f\r\u00a7\t\r\u0001\r\u0001\r"+
		"\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00b5\b\u000f\n"+
		"\u000f\f\u000f\u00b8\t\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0005\u000f\u00be\b\u000f\n\u000f\f\u000f\u00c1\t\u000f\u0001\u000f"+
		"\u0003\u000f\u00c4\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0005\u0010\u00cc\b\u0010\n\u0010\f\u0010\u00cf"+
		"\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u00d6\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00da\b\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00df\b\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0005\u0011\u00e4\b\u0011\n\u0011\f\u0011\u00e7"+
		"\t\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u0100\b\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014\u010b"+
		"\b\u0014\n\u0014\f\u0014\u010e\t\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u011d\b\u0017"+
		"\n\u0017\f\u0017\u0120\t\u0017\u0003\u0017\u0122\b\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0000\u0001(\u0018\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.\u0000\u0006"+
		"\u0001\u0000\b\f\u0001\u0000\u001a\u001b\u0001\u0000\u001c\u001d\u0001"+
		"\u0000\u001e\u001f\u0002\u0000\u001d\u001d  \u0001\u0000!$\u0138\u0000"+
		"0\u0001\u0000\u0000\u0000\u0002@\u0001\u0000\u0000\u0000\u0004K\u0001"+
		"\u0000\u0000\u0000\u0006T\u0001\u0000\u0000\u0000\bX\u0001\u0000\u0000"+
		"\u0000\n`\u0001\u0000\u0000\u0000\fb\u0001\u0000\u0000\u0000\u000eu\u0001"+
		"\u0000\u0000\u0000\u0010}\u0001\u0000\u0000\u0000\u0012\u0080\u0001\u0000"+
		"\u0000\u0000\u0014\u0091\u0001\u0000\u0000\u0000\u0016\u0093\u0001\u0000"+
		"\u0000\u0000\u0018\u0098\u0001\u0000\u0000\u0000\u001a\u009e\u0001\u0000"+
		"\u0000\u0000\u001c\u00ab\u0001\u0000\u0000\u0000\u001e\u00ae\u0001\u0000"+
		"\u0000\u0000 \u00c5\u0001\u0000\u0000\u0000\"\u00d2\u0001\u0000\u0000"+
		"\u0000$\u00ea\u0001\u0000\u0000\u0000&\u00ee\u0001\u0000\u0000\u0000("+
		"\u00ff\u0001\u0000\u0000\u0000*\u010f\u0001\u0000\u0000\u0000,\u0113\u0001"+
		"\u0000\u0000\u0000.\u0117\u0001\u0000\u0000\u000001\u0005\u0001\u0000"+
		"\u000012\u0005\u0002\u0000\u000023\u0005\'\u0000\u000035\u0005\u0003\u0000"+
		"\u000046\u0003\u0004\u0002\u000054\u0001\u0000\u0000\u000056\u0001\u0000"+
		"\u0000\u00006:\u0001\u0000\u0000\u000079\u0003\f\u0006\u000087\u0001\u0000"+
		"\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:;\u0001"+
		"\u0000\u0000\u0000;=\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000"+
		"=>\u0003\u0002\u0001\u0000>?\u0005\u0004\u0000\u0000?\u0001\u0001\u0000"+
		"\u0000\u0000@A\u0005\u0005\u0000\u0000AC\u0005\u0002\u0000\u0000BD\u0003"+
		"\u0004\u0002\u0000CB\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000"+
		"DH\u0001\u0000\u0000\u0000EG\u0003\u0014\n\u0000FE\u0001\u0000\u0000\u0000"+
		"GJ\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000I\u0003\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000KL\u0005"+
		"\u0006\u0000\u0000LP\u0005\u0002\u0000\u0000MN\u0003\u0006\u0003\u0000"+
		"NO\u0005\u0003\u0000\u0000OQ\u0001\u0000\u0000\u0000PM\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000"+
		"\u0000\u0000S\u0005\u0001\u0000\u0000\u0000TU\u0003\b\u0004\u0000UV\u0005"+
		"\u0002\u0000\u0000VW\u0003\n\u0005\u0000W\u0007\u0001\u0000\u0000\u0000"+
		"X]\u0005\'\u0000\u0000YZ\u0005\u0007\u0000\u0000Z\\\u0005\'\u0000\u0000"+
		"[Y\u0001\u0000\u0000\u0000\\_\u0001\u0000\u0000\u0000][\u0001\u0000\u0000"+
		"\u0000]^\u0001\u0000\u0000\u0000^\t\u0001\u0000\u0000\u0000_]\u0001\u0000"+
		"\u0000\u0000`a\u0007\u0000\u0000\u0000a\u000b\u0001\u0000\u0000\u0000"+
		"bc\u0003\n\u0005\u0000cd\u0005\'\u0000\u0000df\u0005\r\u0000\u0000eg\u0003"+
		"\u000e\u0007\u0000fe\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000"+
		"gh\u0001\u0000\u0000\u0000hi\u0005\u000e\u0000\u0000ik\u0005\u000f\u0000"+
		"\u0000jl\u0003\u0004\u0002\u0000kj\u0001\u0000\u0000\u0000kl\u0001\u0000"+
		"\u0000\u0000lp\u0001\u0000\u0000\u0000mo\u0003\u0014\n\u0000nm\u0001\u0000"+
		"\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000qs\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000"+
		"st\u0005\u0010\u0000\u0000t\r\u0001\u0000\u0000\u0000uz\u0003\u0010\b"+
		"\u0000vw\u0005\u0007\u0000\u0000wy\u0003\u0010\b\u0000xv\u0001\u0000\u0000"+
		"\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000"+
		"\u0000\u0000{\u000f\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000"+
		"}~\u0003\n\u0005\u0000~\u007f\u0005\'\u0000\u0000\u007f\u0011\u0001\u0000"+
		"\u0000\u0000\u0080\u0081\u0005\u0011\u0000\u0000\u0081\u0082\u0003(\u0014"+
		"\u0000\u0082\u0083\u0005\u0003\u0000\u0000\u0083\u0013\u0001\u0000\u0000"+
		"\u0000\u0084\u0092\u0003\u0016\u000b\u0000\u0085\u0092\u0003\u0018\f\u0000"+
		"\u0086\u0092\u0003\u001a\r\u0000\u0087\u0092\u0003\u001e\u000f\u0000\u0088"+
		"\u0092\u0003 \u0010\u0000\u0089\u0092\u0003\"\u0011\u0000\u008a\u0092"+
		"\u0003\u001c\u000e\u0000\u008b\u0092\u0003*\u0015\u0000\u008c\u0092\u0003"+
		",\u0016\u0000\u008d\u0092\u0003\u0012\t\u0000\u008e\u008f\u0003.\u0017"+
		"\u0000\u008f\u0090\u0005\u0003\u0000\u0000\u0090\u0092\u0001\u0000\u0000"+
		"\u0000\u0091\u0084\u0001\u0000\u0000\u0000\u0091\u0085\u0001\u0000\u0000"+
		"\u0000\u0091\u0086\u0001\u0000\u0000\u0000\u0091\u0087\u0001\u0000\u0000"+
		"\u0000\u0091\u0088\u0001\u0000\u0000\u0000\u0091\u0089\u0001\u0000\u0000"+
		"\u0000\u0091\u008a\u0001\u0000\u0000\u0000\u0091\u008b\u0001\u0000\u0000"+
		"\u0000\u0091\u008c\u0001\u0000\u0000\u0000\u0091\u008d\u0001\u0000\u0000"+
		"\u0000\u0091\u008e\u0001\u0000\u0000\u0000\u0092\u0015\u0001\u0000\u0000"+
		"\u0000\u0093\u0094\u0005\'\u0000\u0000\u0094\u0095\u0005\u0012\u0000\u0000"+
		"\u0095\u0096\u0003(\u0014\u0000\u0096\u0097\u0005\u0003\u0000\u0000\u0097"+
		"\u0017\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u0013\u0000\u0000\u0099"+
		"\u009a\u0005\r\u0000\u0000\u009a\u009b\u0003\b\u0004\u0000\u009b\u009c"+
		"\u0005\u000e\u0000\u0000\u009c\u009d\u0005\u0003\u0000\u0000\u009d\u0019"+
		"\u0001\u0000\u0000\u0000\u009e\u009f\u0005\u0014\u0000\u0000\u009f\u00a0"+
		"\u0005\r\u0000\u0000\u00a0\u00a5\u0003(\u0014\u0000\u00a1\u00a2\u0005"+
		"\u0007\u0000\u0000\u00a2\u00a4\u0003(\u0014\u0000\u00a3\u00a1\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a7\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a8\u0001\u0000"+
		"\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005\u000e"+
		"\u0000\u0000\u00a9\u00aa\u0005\u0003\u0000\u0000\u00aa\u001b\u0001\u0000"+
		"\u0000\u0000\u00ab\u00ac\u0005\u0015\u0000\u0000\u00ac\u00ad\u0005\u0003"+
		"\u0000\u0000\u00ad\u001d\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\u0016"+
		"\u0000\u0000\u00af\u00b0\u0005\r\u0000\u0000\u00b0\u00b1\u0003(\u0014"+
		"\u0000\u00b1\u00b2\u0005\u000e\u0000\u0000\u00b2\u00b6\u0005\u000f\u0000"+
		"\u0000\u00b3\u00b5\u0003\u0014\n\u0000\u00b4\u00b3\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000"+
		"\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b9\u0001\u0000\u0000\u0000"+
		"\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b9\u00c3\u0005\u0010\u0000\u0000"+
		"\u00ba\u00bb\u0005\u0017\u0000\u0000\u00bb\u00bf\u0005\u000f\u0000\u0000"+
		"\u00bc\u00be\u0003\u0014\n\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00be"+
		"\u00c1\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c2\u0001\u0000\u0000\u0000\u00c1"+
		"\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c4\u0005\u0010\u0000\u0000\u00c3"+
		"\u00ba\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4"+
		"\u001f\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\u0018\u0000\u0000\u00c6"+
		"\u00c7\u0005\r\u0000\u0000\u00c7\u00c8\u0003(\u0014\u0000\u00c8\u00c9"+
		"\u0005\u000e\u0000\u0000\u00c9\u00cd\u0005\u000f\u0000\u0000\u00ca\u00cc"+
		"\u0003\u0014\n\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cf\u0001"+
		"\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001"+
		"\u0000\u0000\u0000\u00ce\u00d0\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001"+
		"\u0000\u0000\u0000\u00d0\u00d1\u0005\u0010\u0000\u0000\u00d1!\u0001\u0000"+
		"\u0000\u0000\u00d2\u00d3\u0005\u0019\u0000\u0000\u00d3\u00d5\u0005\r\u0000"+
		"\u0000\u00d4\u00d6\u0003$\u0012\u0000\u00d5\u00d4\u0001\u0000\u0000\u0000"+
		"\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000"+
		"\u00d7\u00d9\u0005\u0003\u0000\u0000\u00d8\u00da\u0003(\u0014\u0000\u00d9"+
		"\u00d8\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da"+
		"\u00db\u0001\u0000\u0000\u0000\u00db\u00de\u0005\u0003\u0000\u0000\u00dc"+
		"\u00df\u0003$\u0012\u0000\u00dd\u00df\u0003&\u0013\u0000\u00de\u00dc\u0001"+
		"\u0000\u0000\u0000\u00de\u00dd\u0001\u0000\u0000\u0000\u00de\u00df\u0001"+
		"\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0\u00e1\u0005"+
		"\u000e\u0000\u0000\u00e1\u00e5\u0005\u000f\u0000\u0000\u00e2\u00e4\u0003"+
		"\u0014\n\u0000\u00e3\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001\u0000"+
		"\u0000\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000"+
		"\u0000\u0000\u00e6\u00e8\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000"+
		"\u0000\u0000\u00e8\u00e9\u0005\u0010\u0000\u0000\u00e9#\u0001\u0000\u0000"+
		"\u0000\u00ea\u00eb\u0005\'\u0000\u0000\u00eb\u00ec\u0005\u0012\u0000\u0000"+
		"\u00ec\u00ed\u0003(\u0014\u0000\u00ed%\u0001\u0000\u0000\u0000\u00ee\u00ef"+
		"\u0005\'\u0000\u0000\u00ef\u00f0\u0007\u0001\u0000\u0000\u00f0\'\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0006\u0014\uffff\uffff\u0000\u00f2\u00f3"+
		"\u0005\r\u0000\u0000\u00f3\u00f4\u0003(\u0014\u0000\u00f4\u00f5\u0005"+
		"\u000e\u0000\u0000\u00f5\u0100\u0001\u0000\u0000\u0000\u00f6\u00f7\u0007"+
		"\u0002\u0000\u0000\u00f7\u0100\u0003(\u0014\u000b\u00f8\u0100\u0003.\u0017"+
		"\u0000\u00f9\u0100\u0005\'\u0000\u0000\u00fa\u0100\u0005(\u0000\u0000"+
		"\u00fb\u0100\u0005)\u0000\u0000\u00fc\u0100\u0005*\u0000\u0000\u00fd\u0100"+
		"\u0005%\u0000\u0000\u00fe\u0100\u0005&\u0000\u0000\u00ff\u00f1\u0001\u0000"+
		"\u0000\u0000\u00ff\u00f6\u0001\u0000\u0000\u0000\u00ff\u00f8\u0001\u0000"+
		"\u0000\u0000\u00ff\u00f9\u0001\u0000\u0000\u0000\u00ff\u00fa\u0001\u0000"+
		"\u0000\u0000\u00ff\u00fb\u0001\u0000\u0000\u0000\u00ff\u00fc\u0001\u0000"+
		"\u0000\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u00ff\u00fe\u0001\u0000"+
		"\u0000\u0000\u0100\u010c\u0001\u0000\u0000\u0000\u0101\u0102\n\n\u0000"+
		"\u0000\u0102\u0103\u0007\u0003\u0000\u0000\u0103\u010b\u0003(\u0014\u000b"+
		"\u0104\u0105\n\t\u0000\u0000\u0105\u0106\u0007\u0004\u0000\u0000\u0106"+
		"\u010b\u0003(\u0014\n\u0107\u0108\n\b\u0000\u0000\u0108\u0109\u0007\u0005"+
		"\u0000\u0000\u0109\u010b\u0003(\u0014\t\u010a\u0101\u0001\u0000\u0000"+
		"\u0000\u010a\u0104\u0001\u0000\u0000\u0000\u010a\u0107\u0001\u0000\u0000"+
		"\u0000\u010b\u010e\u0001\u0000\u0000\u0000\u010c\u010a\u0001\u0000\u0000"+
		"\u0000\u010c\u010d\u0001\u0000\u0000\u0000\u010d)\u0001\u0000\u0000\u0000"+
		"\u010e\u010c\u0001\u0000\u0000\u0000\u010f\u0110\u0005\'\u0000\u0000\u0110"+
		"\u0111\u0005\u001a\u0000\u0000\u0111\u0112\u0005\u0003\u0000\u0000\u0112"+
		"+\u0001\u0000\u0000\u0000\u0113\u0114\u0005\'\u0000\u0000\u0114\u0115"+
		"\u0005\u001b\u0000\u0000\u0115\u0116\u0005\u0003\u0000\u0000\u0116-\u0001"+
		"\u0000\u0000\u0000\u0117\u0118\u0005\'\u0000\u0000\u0118\u0121\u0005\r"+
		"\u0000\u0000\u0119\u011e\u0003(\u0014\u0000\u011a\u011b\u0005\u0007\u0000"+
		"\u0000\u011b\u011d\u0003(\u0014\u0000\u011c\u011a\u0001\u0000\u0000\u0000"+
		"\u011d\u0120\u0001\u0000\u0000\u0000\u011e\u011c\u0001\u0000\u0000\u0000"+
		"\u011e\u011f\u0001\u0000\u0000\u0000\u011f\u0122\u0001\u0000\u0000\u0000"+
		"\u0120\u011e\u0001\u0000\u0000\u0000\u0121\u0119\u0001\u0000\u0000\u0000"+
		"\u0121\u0122\u0001\u0000\u0000\u0000\u0122\u0123\u0001\u0000\u0000\u0000"+
		"\u0123\u0124\u0005\u000e\u0000\u0000\u0124/\u0001\u0000\u0000\u0000\u0019"+
		"5:CHR]fkpz\u0091\u00a5\u00b6\u00bf\u00c3\u00cd\u00d5\u00d9\u00de\u00e5"+
		"\u00ff\u010a\u010c\u011e\u0121";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}