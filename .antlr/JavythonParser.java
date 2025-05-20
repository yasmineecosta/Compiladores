// Generated from c:/Users/Yasmine Martins/Desktop/vsCode/universidade/sexto_periodo/Compiladores/Javython.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class JavythonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		ID=39, NUM_INT=40, NUM_REAL=41, STRING=42, COMMENT=43;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_decIds = 2, RULE_decl = 3, RULE_idList = 4, 
		RULE_tipo = 5, RULE_metodo = 6, RULE_parametros = 7, RULE_parametro = 8, 
		RULE_returnCmd = 9, RULE_comando = 10, RULE_atribuicao = 11, RULE_inputCmd = 12, 
		RULE_printCmd = 13, RULE_breakCmd = 14, RULE_ifCmd = 15, RULE_whileCmd = 16, 
		RULE_forCmd = 17, RULE_expressao = 18, RULE_incremento = 19, RULE_decremento = 20, 
		RULE_chamadaFuncao = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "decIds", "decl", "idList", "tipo", "metodo", "parametros", 
			"parametro", "returnCmd", "comando", "atribuicao", "inputCmd", "printCmd", 
			"breakCmd", "ifCmd", "whileCmd", "forCmd", "expressao", "incremento", 
			"decremento", "chamadaFuncao"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "':'", "';'", "'end'", "'main'", "'decIds'", "','", 
			"'int'", "'real'", "'str'", "'bool'", "'void'", "'('", "')'", "'{'", 
			"'}'", "'return'", "'='", "'input'", "'print'", "'break'", "'if'", "'else'", 
			"'while'", "'for'", "'!'", "'-'", "'*'", "'/'", "'+'", "'=='", "'!='", 
			"'>'", "'<'", "'true'", "'false'", "'++'", "'--'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "NUM_INT", "NUM_REAL", "STRING", "COMMENT"
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
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__0);
			setState(45);
			match(T__1);
			setState(46);
			match(ID);
			setState(47);
			match(T__2);
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(48);
				decIds();
				}
			}

			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7936L) != 0)) {
				{
				{
				setState(51);
				metodo();
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			main();
			setState(58);
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
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(T__4);
			setState(61);
			match(T__1);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(62);
				decIds();
				}
			}

			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(65);
				comando();
				}
				}
				setState(70);
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
	}

	public final DecIdsContext decIds() throws RecognitionException {
		DecIdsContext _localctx = new DecIdsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_decIds);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__5);
			setState(72);
			match(T__1);
			setState(76); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(73);
					decl();
					setState(74);
					match(T__2);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(78); 
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
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			idList();
			setState(81);
			match(T__1);
			setState(82);
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
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_idList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(ID);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(85);
				match(T__6);
				setState(86);
				match(ID);
				}
				}
				setState(91);
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
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
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
		public ReturnCmdContext returnCmd() {
			return getRuleContext(ReturnCmdContext.class,0);
		}
		public MetodoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metodo; }
	}

	public final MetodoContext metodo() throws RecognitionException {
		MetodoContext _localctx = new MetodoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_metodo);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			tipo();
			setState(95);
			match(ID);
			setState(96);
			match(T__12);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7936L) != 0)) {
				{
				setState(97);
				parametros();
				}
			}

			setState(100);
			match(T__13);
			setState(101);
			match(T__14);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(102);
				decIds();
				}
			}

			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(105);
					comando();
					}
					} 
				}
				setState(110);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(111);
				returnCmd();
				}
			}

			setState(114);
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
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parametros);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			parametro();
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(117);
				match(T__6);
				setState(118);
				parametro();
				}
				}
				setState(123);
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
	}

	public final ParametroContext parametro() throws RecognitionException {
		ParametroContext _localctx = new ParametroContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parametro);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			tipo();
			setState(125);
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
	}

	public final ReturnCmdContext returnCmd() throws RecognitionException {
		ReturnCmdContext _localctx = new ReturnCmdContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_returnCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__16);
			setState(128);
			expressao(0);
			setState(129);
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
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comando);
		try {
			setState(141);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				atribuicao();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				inputCmd();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(133);
				printCmd();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(134);
				ifCmd();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(135);
				whileCmd();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(136);
				forCmd();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(137);
				breakCmd();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(138);
				incremento();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(139);
				decremento();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(140);
				returnCmd();
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
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(ID);
			setState(144);
			match(T__17);
			setState(145);
			expressao(0);
			setState(146);
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
	}

	public final InputCmdContext inputCmd() throws RecognitionException {
		InputCmdContext _localctx = new InputCmdContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_inputCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__18);
			setState(149);
			match(T__12);
			setState(150);
			idList();
			setState(151);
			match(T__13);
			setState(152);
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
	}

	public final PrintCmdContext printCmd() throws RecognitionException {
		PrintCmdContext _localctx = new PrintCmdContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_printCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(T__19);
			setState(155);
			match(T__12);
			setState(156);
			expressao(0);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(157);
				match(T__6);
				setState(158);
				expressao(0);
				}
				}
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(164);
			match(T__13);
			setState(165);
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
	}

	public final BreakCmdContext breakCmd() throws RecognitionException {
		BreakCmdContext _localctx = new BreakCmdContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_breakCmd);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(T__20);
			setState(168);
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
	}

	public final IfCmdContext ifCmd() throws RecognitionException {
		IfCmdContext _localctx = new IfCmdContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ifCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(T__21);
			setState(171);
			match(T__12);
			setState(172);
			expressao(0);
			setState(173);
			match(T__13);
			setState(174);
			match(T__14);
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(175);
				comando();
				}
				}
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(181);
			match(T__15);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(182);
				match(T__22);
				setState(183);
				match(T__14);
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
					{
					{
					setState(184);
					comando();
					}
					}
					setState(189);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(190);
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
	}

	public final WhileCmdContext whileCmd() throws RecognitionException {
		WhileCmdContext _localctx = new WhileCmdContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(T__23);
			setState(194);
			match(T__12);
			setState(195);
			expressao(0);
			setState(196);
			match(T__13);
			setState(197);
			match(T__14);
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(198);
				comando();
				}
				}
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(204);
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
		public List<AtribuicaoContext> atribuicao() {
			return getRuleContexts(AtribuicaoContext.class);
		}
		public AtribuicaoContext atribuicao(int i) {
			return getRuleContext(AtribuicaoContext.class,i);
		}
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
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
	}

	public final ForCmdContext forCmd() throws RecognitionException {
		ForCmdContext _localctx = new ForCmdContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_forCmd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			match(T__24);
			setState(207);
			match(T__12);
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(208);
				atribuicao();
				}
			}

			setState(211);
			match(T__2);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8349617758208L) != 0)) {
				{
				setState(212);
				expressao(0);
				}
			}

			setState(215);
			match(T__2);
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(216);
				atribuicao();
				}
			}

			setState(219);
			match(T__13);
			setState(220);
			match(T__14);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 549814140928L) != 0)) {
				{
				{
				setState(221);
				comando();
				}
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(227);
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
	public static class ExpressaoContext extends ParserRuleContext {
		public Token op;
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public ChamadaFuncaoContext chamadaFuncao() {
			return getRuleContext(ChamadaFuncaoContext.class,0);
		}
		public TerminalNode ID() { return getToken(JavythonParser.ID, 0); }
		public TerminalNode NUM_INT() { return getToken(JavythonParser.NUM_INT, 0); }
		public TerminalNode NUM_REAL() { return getToken(JavythonParser.NUM_REAL, 0); }
		public TerminalNode STRING() { return getToken(JavythonParser.STRING, 0); }
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		return expressao(0);
	}

	private ExpressaoContext expressao(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, _parentState);
		ExpressaoContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expressao, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(230);
				match(T__12);
				setState(231);
				expressao(0);
				setState(232);
				match(T__13);
				}
				break;
			case 2:
				{
				setState(234);
				((ExpressaoContext)_localctx).op = match(T__25);
				setState(235);
				expressao(13);
				}
				break;
			case 3:
				{
				setState(236);
				((ExpressaoContext)_localctx).op = match(T__26);
				setState(237);
				expressao(12);
				}
				break;
			case 4:
				{
				setState(238);
				chamadaFuncao();
				}
				break;
			case 5:
				{
				setState(239);
				match(ID);
				}
				break;
			case 6:
				{
				setState(240);
				match(NUM_INT);
				}
				break;
			case 7:
				{
				setState(241);
				match(NUM_REAL);
				}
				break;
			case 8:
				{
				setState(242);
				match(STRING);
				}
				break;
			case 9:
				{
				setState(243);
				match(T__34);
				}
				break;
			case 10:
				{
				setState(244);
				match(T__35);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(261);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(259);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(247);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(248);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__27 || _la==T__28) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(249);
						expressao(12);
						}
						break;
					case 2:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(250);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(251);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__26 || _la==T__29) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(252);
						expressao(11);
						}
						break;
					case 3:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(253);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(254);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__30 || _la==T__31) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(255);
						expressao(10);
						}
						break;
					case 4:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(256);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(257);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__32 || _la==T__33) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(258);
						expressao(9);
						}
						break;
					}
					} 
				}
				setState(263);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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
	}

	public final IncrementoContext incremento() throws RecognitionException {
		IncrementoContext _localctx = new IncrementoContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_incremento);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(ID);
			setState(265);
			match(T__36);
			setState(266);
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
	}

	public final DecrementoContext decremento() throws RecognitionException {
		DecrementoContext _localctx = new DecrementoContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_decremento);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(ID);
			setState(269);
			match(T__37);
			setState(270);
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
	}

	public final ChamadaFuncaoContext chamadaFuncao() throws RecognitionException {
		ChamadaFuncaoContext _localctx = new ChamadaFuncaoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_chamadaFuncao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(ID);
			setState(273);
			match(T__12);
			setState(282);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8349617758208L) != 0)) {
				{
				setState(274);
				expressao(0);
				setState(279);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__6) {
					{
					{
					setState(275);
					match(T__6);
					setState(276);
					expressao(0);
					}
					}
					setState(281);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(284);
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
		case 18:
			return expressao_sempred((ExpressaoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expressao_sempred(ExpressaoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		case 1:
			return precpred(_ctx, 10);
		case 2:
			return precpred(_ctx, 9);
		case 3:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001+\u011f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000"+
		"2\b\u0000\u0001\u0000\u0005\u00005\b\u0000\n\u0000\f\u00008\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001@\b\u0001\u0001\u0001\u0005\u0001C\b\u0001\n\u0001\f\u0001F\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0004\u0002"+
		"M\b\u0002\u000b\u0002\f\u0002N\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004X\b\u0004\n\u0004"+
		"\f\u0004[\t\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006c\b\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006h\b\u0006\u0001\u0006\u0005\u0006k\b\u0006\n\u0006\f"+
		"\u0006n\t\u0006\u0001\u0006\u0003\u0006q\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007x\b\u0007\n\u0007\f\u0007"+
		"{\t\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u008e\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0005\r\u00a0\b\r\n\r\f\r\u00a3\t\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00b1\b\u000f"+
		"\n\u000f\f\u000f\u00b4\t\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0005\u000f\u00ba\b\u000f\n\u000f\f\u000f\u00bd\t\u000f\u0001\u000f"+
		"\u0003\u000f\u00c0\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0005\u0010\u00c8\b\u0010\n\u0010\f\u0010\u00cb"+
		"\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u00d2\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00d6\b\u0011"+
		"\u0001\u0011\u0001\u0011\u0003\u0011\u00da\b\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0005\u0011\u00df\b\u0011\n\u0011\f\u0011\u00e2\t\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003"+
		"\u0012\u00f6\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0005\u0012\u0104\b\u0012\n\u0012\f\u0012\u0107\t\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0005\u0015\u0116\b\u0015\n\u0015\f\u0015\u0119\t\u0015\u0003"+
		"\u0015\u011b\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0000\u0001$"+
		"\u0016\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*\u0000\u0005\u0001\u0000\b\f\u0001\u0000\u001c"+
		"\u001d\u0002\u0000\u001b\u001b\u001e\u001e\u0001\u0000\u001f \u0001\u0000"+
		"!\"\u0134\u0000,\u0001\u0000\u0000\u0000\u0002<\u0001\u0000\u0000\u0000"+
		"\u0004G\u0001\u0000\u0000\u0000\u0006P\u0001\u0000\u0000\u0000\bT\u0001"+
		"\u0000\u0000\u0000\n\\\u0001\u0000\u0000\u0000\f^\u0001\u0000\u0000\u0000"+
		"\u000et\u0001\u0000\u0000\u0000\u0010|\u0001\u0000\u0000\u0000\u0012\u007f"+
		"\u0001\u0000\u0000\u0000\u0014\u008d\u0001\u0000\u0000\u0000\u0016\u008f"+
		"\u0001\u0000\u0000\u0000\u0018\u0094\u0001\u0000\u0000\u0000\u001a\u009a"+
		"\u0001\u0000\u0000\u0000\u001c\u00a7\u0001\u0000\u0000\u0000\u001e\u00aa"+
		"\u0001\u0000\u0000\u0000 \u00c1\u0001\u0000\u0000\u0000\"\u00ce\u0001"+
		"\u0000\u0000\u0000$\u00f5\u0001\u0000\u0000\u0000&\u0108\u0001\u0000\u0000"+
		"\u0000(\u010c\u0001\u0000\u0000\u0000*\u0110\u0001\u0000\u0000\u0000,"+
		"-\u0005\u0001\u0000\u0000-.\u0005\u0002\u0000\u0000./\u0005\'\u0000\u0000"+
		"/1\u0005\u0003\u0000\u000002\u0003\u0004\u0002\u000010\u0001\u0000\u0000"+
		"\u000012\u0001\u0000\u0000\u000026\u0001\u0000\u0000\u000035\u0003\f\u0006"+
		"\u000043\u0001\u0000\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000"+
		"\u0000\u000067\u0001\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001"+
		"\u0000\u0000\u00009:\u0003\u0002\u0001\u0000:;\u0005\u0004\u0000\u0000"+
		";\u0001\u0001\u0000\u0000\u0000<=\u0005\u0005\u0000\u0000=?\u0005\u0002"+
		"\u0000\u0000>@\u0003\u0004\u0002\u0000?>\u0001\u0000\u0000\u0000?@\u0001"+
		"\u0000\u0000\u0000@D\u0001\u0000\u0000\u0000AC\u0003\u0014\n\u0000BA\u0001"+
		"\u0000\u0000\u0000CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000"+
		"DE\u0001\u0000\u0000\u0000E\u0003\u0001\u0000\u0000\u0000FD\u0001\u0000"+
		"\u0000\u0000GH\u0005\u0006\u0000\u0000HL\u0005\u0002\u0000\u0000IJ\u0003"+
		"\u0006\u0003\u0000JK\u0005\u0003\u0000\u0000KM\u0001\u0000\u0000\u0000"+
		"LI\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000O\u0005\u0001\u0000\u0000\u0000PQ\u0003"+
		"\b\u0004\u0000QR\u0005\u0002\u0000\u0000RS\u0003\n\u0005\u0000S\u0007"+
		"\u0001\u0000\u0000\u0000TY\u0005\'\u0000\u0000UV\u0005\u0007\u0000\u0000"+
		"VX\u0005\'\u0000\u0000WU\u0001\u0000\u0000\u0000X[\u0001\u0000\u0000\u0000"+
		"YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z\t\u0001\u0000\u0000"+
		"\u0000[Y\u0001\u0000\u0000\u0000\\]\u0007\u0000\u0000\u0000]\u000b\u0001"+
		"\u0000\u0000\u0000^_\u0003\n\u0005\u0000_`\u0005\'\u0000\u0000`b\u0005"+
		"\r\u0000\u0000ac\u0003\u000e\u0007\u0000ba\u0001\u0000\u0000\u0000bc\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0005\u000e\u0000\u0000"+
		"eg\u0005\u000f\u0000\u0000fh\u0003\u0004\u0002\u0000gf\u0001\u0000\u0000"+
		"\u0000gh\u0001\u0000\u0000\u0000hl\u0001\u0000\u0000\u0000ik\u0003\u0014"+
		"\n\u0000ji\u0001\u0000\u0000\u0000kn\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000lm\u0001\u0000\u0000\u0000mp\u0001\u0000\u0000\u0000nl\u0001"+
		"\u0000\u0000\u0000oq\u0003\u0012\t\u0000po\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0005\u0010\u0000\u0000"+
		"s\r\u0001\u0000\u0000\u0000ty\u0003\u0010\b\u0000uv\u0005\u0007\u0000"+
		"\u0000vx\u0003\u0010\b\u0000wu\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000"+
		"\u0000yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z\u000f\u0001"+
		"\u0000\u0000\u0000{y\u0001\u0000\u0000\u0000|}\u0003\n\u0005\u0000}~\u0005"+
		"\'\u0000\u0000~\u0011\u0001\u0000\u0000\u0000\u007f\u0080\u0005\u0011"+
		"\u0000\u0000\u0080\u0081\u0003$\u0012\u0000\u0081\u0082\u0005\u0003\u0000"+
		"\u0000\u0082\u0013\u0001\u0000\u0000\u0000\u0083\u008e\u0003\u0016\u000b"+
		"\u0000\u0084\u008e\u0003\u0018\f\u0000\u0085\u008e\u0003\u001a\r\u0000"+
		"\u0086\u008e\u0003\u001e\u000f\u0000\u0087\u008e\u0003 \u0010\u0000\u0088"+
		"\u008e\u0003\"\u0011\u0000\u0089\u008e\u0003\u001c\u000e\u0000\u008a\u008e"+
		"\u0003&\u0013\u0000\u008b\u008e\u0003(\u0014\u0000\u008c\u008e\u0003\u0012"+
		"\t\u0000\u008d\u0083\u0001\u0000\u0000\u0000\u008d\u0084\u0001\u0000\u0000"+
		"\u0000\u008d\u0085\u0001\u0000\u0000\u0000\u008d\u0086\u0001\u0000\u0000"+
		"\u0000\u008d\u0087\u0001\u0000\u0000\u0000\u008d\u0088\u0001\u0000\u0000"+
		"\u0000\u008d\u0089\u0001\u0000\u0000\u0000\u008d\u008a\u0001\u0000\u0000"+
		"\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000"+
		"\u0000\u008e\u0015\u0001\u0000\u0000\u0000\u008f\u0090\u0005\'\u0000\u0000"+
		"\u0090\u0091\u0005\u0012\u0000\u0000\u0091\u0092\u0003$\u0012\u0000\u0092"+
		"\u0093\u0005\u0003\u0000\u0000\u0093\u0017\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0005\u0013\u0000\u0000\u0095\u0096\u0005\r\u0000\u0000\u0096\u0097"+
		"\u0003\b\u0004\u0000\u0097\u0098\u0005\u000e\u0000\u0000\u0098\u0099\u0005"+
		"\u0003\u0000\u0000\u0099\u0019\u0001\u0000\u0000\u0000\u009a\u009b\u0005"+
		"\u0014\u0000\u0000\u009b\u009c\u0005\r\u0000\u0000\u009c\u00a1\u0003$"+
		"\u0012\u0000\u009d\u009e\u0005\u0007\u0000\u0000\u009e\u00a0\u0003$\u0012"+
		"\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u00a0\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a4\u0001\u0000\u0000\u0000\u00a3\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a4\u00a5\u0005\u000e\u0000\u0000\u00a5\u00a6\u0005\u0003\u0000"+
		"\u0000\u00a6\u001b\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\u0015\u0000"+
		"\u0000\u00a8\u00a9\u0005\u0003\u0000\u0000\u00a9\u001d\u0001\u0000\u0000"+
		"\u0000\u00aa\u00ab\u0005\u0016\u0000\u0000\u00ab\u00ac\u0005\r\u0000\u0000"+
		"\u00ac\u00ad\u0003$\u0012\u0000\u00ad\u00ae\u0005\u000e\u0000\u0000\u00ae"+
		"\u00b2\u0005\u000f\u0000\u0000\u00af\u00b1\u0003\u0014\n\u0000\u00b0\u00af"+
		"\u0001\u0000\u0000\u0000\u00b1\u00b4\u0001\u0000\u0000\u0000\u00b2\u00b0"+
		"\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b5\u00bf"+
		"\u0005\u0010\u0000\u0000\u00b6\u00b7\u0005\u0017\u0000\u0000\u00b7\u00bb"+
		"\u0005\u000f\u0000\u0000\u00b8\u00ba\u0003\u0014\n\u0000\u00b9\u00b8\u0001"+
		"\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00be\u0001"+
		"\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000\u0000\u00be\u00c0\u0005"+
		"\u0010\u0000\u0000\u00bf\u00b6\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001"+
		"\u0000\u0000\u0000\u00c0\u001f\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005"+
		"\u0018\u0000\u0000\u00c2\u00c3\u0005\r\u0000\u0000\u00c3\u00c4\u0003$"+
		"\u0012\u0000\u00c4\u00c5\u0005\u000e\u0000\u0000\u00c5\u00c9\u0005\u000f"+
		"\u0000\u0000\u00c6\u00c8\u0003\u0014\n\u0000\u00c7\u00c6\u0001\u0000\u0000"+
		"\u0000\u00c8\u00cb\u0001\u0000\u0000\u0000\u00c9\u00c7\u0001\u0000\u0000"+
		"\u0000\u00c9\u00ca\u0001\u0000\u0000\u0000\u00ca\u00cc\u0001\u0000\u0000"+
		"\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\u0010\u0000"+
		"\u0000\u00cd!\u0001\u0000\u0000\u0000\u00ce\u00cf\u0005\u0019\u0000\u0000"+
		"\u00cf\u00d1\u0005\r\u0000\u0000\u00d0\u00d2\u0003\u0016\u000b\u0000\u00d1"+
		"\u00d0\u0001\u0000\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d3\u00d5\u0005\u0003\u0000\u0000\u00d4"+
		"\u00d6\u0003$\u0012\u0000\u00d5\u00d4\u0001\u0000\u0000\u0000\u00d5\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d9"+
		"\u0005\u0003\u0000\u0000\u00d8\u00da\u0003\u0016\u000b\u0000\u00d9\u00d8"+
		"\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u00db"+
		"\u0001\u0000\u0000\u0000\u00db\u00dc\u0005\u000e\u0000\u0000\u00dc\u00e0"+
		"\u0005\u000f\u0000\u0000\u00dd\u00df\u0003\u0014\n\u0000\u00de\u00dd\u0001"+
		"\u0000\u0000\u0000\u00df\u00e2\u0001\u0000\u0000\u0000\u00e0\u00de\u0001"+
		"\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1\u00e3\u0001"+
		"\u0000\u0000\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005"+
		"\u0010\u0000\u0000\u00e4#\u0001\u0000\u0000\u0000\u00e5\u00e6\u0006\u0012"+
		"\uffff\uffff\u0000\u00e6\u00e7\u0005\r\u0000\u0000\u00e7\u00e8\u0003$"+
		"\u0012\u0000\u00e8\u00e9\u0005\u000e\u0000\u0000\u00e9\u00f6\u0001\u0000"+
		"\u0000\u0000\u00ea\u00eb\u0005\u001a\u0000\u0000\u00eb\u00f6\u0003$\u0012"+
		"\r\u00ec\u00ed\u0005\u001b\u0000\u0000\u00ed\u00f6\u0003$\u0012\f\u00ee"+
		"\u00f6\u0003*\u0015\u0000\u00ef\u00f6\u0005\'\u0000\u0000\u00f0\u00f6"+
		"\u0005(\u0000\u0000\u00f1\u00f6\u0005)\u0000\u0000\u00f2\u00f6\u0005*"+
		"\u0000\u0000\u00f3\u00f6\u0005#\u0000\u0000\u00f4\u00f6\u0005$\u0000\u0000"+
		"\u00f5\u00e5\u0001\u0000\u0000\u0000\u00f5\u00ea\u0001\u0000\u0000\u0000"+
		"\u00f5\u00ec\u0001\u0000\u0000\u0000\u00f5\u00ee\u0001\u0000\u0000\u0000"+
		"\u00f5\u00ef\u0001\u0000\u0000\u0000\u00f5\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f5\u00f1\u0001\u0000\u0000\u0000\u00f5\u00f2\u0001\u0000\u0000\u0000"+
		"\u00f5\u00f3\u0001\u0000\u0000\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000"+
		"\u00f6\u0105\u0001\u0000\u0000\u0000\u00f7\u00f8\n\u000b\u0000\u0000\u00f8"+
		"\u00f9\u0007\u0001\u0000\u0000\u00f9\u0104\u0003$\u0012\f\u00fa\u00fb"+
		"\n\n\u0000\u0000\u00fb\u00fc\u0007\u0002\u0000\u0000\u00fc\u0104\u0003"+
		"$\u0012\u000b\u00fd\u00fe\n\t\u0000\u0000\u00fe\u00ff\u0007\u0003\u0000"+
		"\u0000\u00ff\u0104\u0003$\u0012\n\u0100\u0101\n\b\u0000\u0000\u0101\u0102"+
		"\u0007\u0004\u0000\u0000\u0102\u0104\u0003$\u0012\t\u0103\u00f7\u0001"+
		"\u0000\u0000\u0000\u0103\u00fa\u0001\u0000\u0000\u0000\u0103\u00fd\u0001"+
		"\u0000\u0000\u0000\u0103\u0100\u0001\u0000\u0000\u0000\u0104\u0107\u0001"+
		"\u0000\u0000\u0000\u0105\u0103\u0001\u0000\u0000\u0000\u0105\u0106\u0001"+
		"\u0000\u0000\u0000\u0106%\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000"+
		"\u0000\u0000\u0108\u0109\u0005\'\u0000\u0000\u0109\u010a\u0005%\u0000"+
		"\u0000\u010a\u010b\u0005\u0003\u0000\u0000\u010b\'\u0001\u0000\u0000\u0000"+
		"\u010c\u010d\u0005\'\u0000\u0000\u010d\u010e\u0005&\u0000\u0000\u010e"+
		"\u010f\u0005\u0003\u0000\u0000\u010f)\u0001\u0000\u0000\u0000\u0110\u0111"+
		"\u0005\'\u0000\u0000\u0111\u011a\u0005\r\u0000\u0000\u0112\u0117\u0003"+
		"$\u0012\u0000\u0113\u0114\u0005\u0007\u0000\u0000\u0114\u0116\u0003$\u0012"+
		"\u0000\u0115\u0113\u0001\u0000\u0000\u0000\u0116\u0119\u0001\u0000\u0000"+
		"\u0000\u0117\u0115\u0001\u0000\u0000\u0000\u0117\u0118\u0001\u0000\u0000"+
		"\u0000\u0118\u011b\u0001\u0000\u0000\u0000\u0119\u0117\u0001\u0000\u0000"+
		"\u0000\u011a\u0112\u0001\u0000\u0000\u0000\u011a\u011b\u0001\u0000\u0000"+
		"\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011d\u0005\u000e\u0000"+
		"\u0000\u011d+\u0001\u0000\u0000\u0000\u001a16?DNYbglpy\u008d\u00a1\u00b2"+
		"\u00bb\u00bf\u00c9\u00d1\u00d5\u00d9\u00e0\u00f5\u0103\u0105\u0117\u011a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}