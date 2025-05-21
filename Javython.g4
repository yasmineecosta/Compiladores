grammar Javython;
options { caseInsensitive = true; }

program     : 'program' ':' ID ';' decIds metodo* main 'end' ;
main        : 'main' ':' decIds? comando* ;
decIds      : 'decIds' ':' (decl ';')+ ;

decl        : idList ':' tipo ;
idList      : ID (',' ID)* ;

tipo        : 'int' | 'real' | 'str' | 'bool' | 'void' ;

metodo      : tipo ID '(' parametros? ')' '{' decIds? comando* returnCmd? '}' ;
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
    ;

atribuicao  : ID '=' expressao ';' ;
inputCmd    : 'input' '(' idList ')' ';' ;
printCmd    : 'print' '(' expressao (',' expressao)* ')' ';' ;
breakCmd    : 'break' ';' ;
atribuicaoFor: ID '=' expressao | ID '++' | ID '--' ;
ifCmd       : 'if' '(' expressao ')' '{' comando* '}' ('else' '{' comando* '}')? ;
whileCmd    : 'while' '(' expressao ')' '{' comando* '}' ;
forCmd      : 'for' '(' atribuicaoFor? ';' expressao? ';' atribuicaoFor? ')' '{' comando* '}' ;
expressao   : '(' expressao ')' | op='!' expressao | op='-' expressao
    | expressao op=('*' | '/') expressao | expressao op=('+' | '-') expressao
    | expressao op=('==' | '!=') expressao | expressao op=('>' | '<') expressao
    | chamadaFuncao
    | ID
    | NUM_INT
    | NUM_REAL
    | STRING
    | 'true'
    | 'false'
    ;

incremento : ID '++' ';' ;
decremento : ID '--' ';' ;

chamadaFuncao : ID '(' (expressao (',' expressao)*)? ')' ;

ID      : [a-z_][A-Z_0-9]* ;
NUM_INT : [0-9]+ ;
NUM_REAL: [0-9]+ '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' ;
// string pode aceitar mais de uma linha?

WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
