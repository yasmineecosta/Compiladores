grammar TresEnderecos;

// Regras parser (sintaxe)

program : instrucoes* EOF ;

instrucoes : declaracaoVariavel
           | atribuicao;

declaracaoVariavel : 'number' ID ';' ;

atribuicao : ID '=' expr ';' ;

expr: expr op=('*'|'/') expr     # MulDiv
    | expr op=('+'|'-') expr     # AddSub
    | op=('+'|'-') expr          # UnaryOp
    | ID                         # Id
    | INT                        # Int
    | '(' expr ')'               # Parens
    ;

// Regras lexer (tokens)


NUMBER : 'number' ;
SEMI : ';' ;
EQUAL : '=' ;
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
LPAREN : '(' ;
RPAREN : ')' ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;

WS      : [ \t\r\n]+ -> skip ;
