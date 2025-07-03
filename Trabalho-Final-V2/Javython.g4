grammar Javython;

// MELHORIA: A opção caseInsensitive atende ao requisito da especificação [cite: 27]
options { caseInsensitive = true; }

/*------------------------------------------------------------------
 * Regras do Parser
 *------------------------------------------------------------------*/
program     : 'program' ':' ID ';' decIds? metodo* main 'end' ;
main        : 'main' ':' decIds? comando* ;

decIds      : 'decIds' ':' (declVar | declConst)+ ;
declVar     : idList ':' tipo ';' ;
declConst   : ID '=' expressao ';' ;


idList      : ID (',' ID)* ;
tipo        : 'int' | 'real' | 'str' | 'bool' | 'void' ;

metodo      : tipo ID '(' parametros? ')' '{' decIds? comando* '}' ;
parametros  : parametro (',' parametro)* ;
parametro   : tipo ID ;
returnCmd   : 'return' expressao ';' ;

comando
    : atribuicao
    | inputCmd
    | printCmd
    | ifCmd
    | whileCmd
    | forCmd
    | breakCmd
    | incremento
    | decremento
    | returnCmd
    | chamadaFuncao ';'
    ;

atribuicao  : ID '=' expressao ';' ;
inputCmd    : 'input' '(' idList ')' ';' ;
printCmd    : 'print' '(' expressao (',' expressao)* ')' ';' ;
breakCmd    : 'break' ';' ;

ifCmd       : 'if' '(' expressao ')' '{' comando* '}' ('else' '{' comando* '}')? ;
whileCmd    : 'while' '(' expressao ')' '{' comando* '}' ;

forCmd      : 'for' '(' forInit? ';' expressao? ';' forUpdate? ')' '{' comando* '}' ;
forInit     : atribuicaoFor (',' atribuicaoFor)* ;
forUpdate   : incDecUpdate (',' incDecUpdate)* ;
incDecUpdate: atribuicaoFor | incDecFor;
atribuicaoFor : ID '=' expressao ;
incDecFor   : ID ('++' | '--') ;

expressao
    : '(' expressao ')'                                     # ParensExpr
    | op=('!' | '-') expressao                              # UnaryExpr
    | expressao op=('*' | '/') expressao                    # MulDivExpr
    | expressao op=('+' | '-') expressao                    # AddSubExpr
    | expressao op=('==' | '!=' | '>' | '<') expressao      # CompExpr
    | chamadaFuncao                                         # FuncCallExpr
    | ID                                                    # IdAtom
    | NUM_INT                                               # IntAtom
    | NUM_REAL                                              # RealAtom
    | STRING                                                # StringAtom
    | 'true'                                                # BoolAtom
    | 'false'                                               # BoolAtom
    ;

incremento  : ID '++' ';' ;
decremento  : ID '--' ';' ;
chamadaFuncao : ID '(' (expressao (',' expressao)*)? ')' ;


//------------------------------------------------------------------
//Regras do Lexer
ID      : [a-z_] [a-z_0-9]* ; // Identificadores começam com letra ou underscore
NUM_INT : [0-9]+ ;
NUM_REAL: [0-9]+ '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;