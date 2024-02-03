grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

 /* --------------------------  Parser structure ----------------------- */

// declared 
program:(COMMENTS NEWLINE | NEWLINE)* decl_list EOF;
decl_list:  decl decl_list |  decl;
decl: function | variables ignore;

// declared variable
variables: implicit_var | keyword_var | implicit_dynamic; 
// implicit_var, keyword_var , implicit_dynamic
implicit_var: VAR ID ASSIGNINIT expression;

keyword_var: (BOOL | STRING | NUMBER) ID (LP NUMBER_list? RP)?
			| (BOOL | STRING | NUMBER) ID (LP NUMBER_list? RP)?  ASSIGNINIT expression;

implicit_dynamic: DYNAMIC ID 
				| DYNAMIC ID ASSIGNINIT expression?;

NUMBER_list: INT COMMA NUMBER_list | INT ;

// declared function
function: FUNC ID LB prameters_list? RB  (ignore? return_statement | ignore? block_stmt | ignore);
//prameters_list
prameters_list: (NUMBER|BOOL|STRING) ID (LP NUMBER_list RP)? (COMMA prameters_list)?;

// Expression
expression: exp1 CONCAT exp1 | exp1;
exp1: exp2 ( EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREAT | GREAT_EQUAL | ASSIGN) exp2 | exp2;
exp2: exp3 (AND | OR) exp2 | exp3;
exp3: exp4 (ADD | SUB) exp3 | exp4;
exp4: exp5 (MUL | DIV | MOD) exp4 | exp5;
exp5: (NOT) exp5 | exp6;
exp6: (SUB | ADD) exp6 | exp7;
exp7: (ID | func_call) element_expr | exp8;
exp8: literals | LB expression RB | ID |  func_call;

//Value
literals_list: expression COMMA literals_list | expression;
literals: INT | REAL | STRING_LIT | TRUE | FALSE | arr_literals;
arr_literals: LP literals_list RP;

element_expr: LP indx_operator RP;
indx_operator: expression COMMA indx_operator | expression;

//Statements 
statement: decl_stmt | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_stmt;
decl_stmt: variables ignore;
assignment_statement : lhs ASSIGNINIT expression ignore;
lhs: ID element_expr | ID;

if_statement: IF LB expression RP ignore? stmt elseif_statement? ;
elseif_statement: (ELIF LB expression RB ignore? stmt elseif_statement?) | ELSE ignore? stmt;

for_statement: FOR ID UNTIL expression BY expression ignore? stmt;

break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;
return_statement: RETURN expression? ignore;
call_statement: func_call ignore;
func_call: (ID LB indx_operator RB) | ID LB RB;


block_stmt: BEGIN ignore stmt? END ignore;

stmt: statement stmt | statement;

// ignored character
ignore: NEWLINE+;

//fragment
fragment INPART: [0-9]+ ;
fragment DEPART: [0-9]+ '.';
fragment EXPART: [eE] [-+]? [0-9]+;
fragment ILLSTRING:  ~[\r\n\\"] 
                    | '\\' [bfrnt'\\] 
                    | '\'"';
fragment STRINGCHAR : ~[\r\n\f\\"] 
                    | '\\' [bfrnt'\\] 
                    | '\'"';

//! --------------------------  Lexical structure ----------------------- //
// TODO KeyWord
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL:'until';
BY:'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else'; 
ELIF: 'elif';
BEGIN:'begin';
END: 'end';
AND: 'and';
OR: 'or';
NOT: 'not';
WHILE: 'while';
BOOLEAN: TRUE | FALSE;

// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
ASSIGNINIT: '<-';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREAT: '>';
GREAT_EQUAL: '>=';
CONCAT:'...';

// TODO Separators
LB: '('; 
RB: ')';
LP: '[';
RP: ']';
COMMA: ',';

// NEWLINE COMMENTS WS
NEWLINE: [\n]; // newline
COMMENTS: '##' ~[\n\r\f]* -> skip; // Comments
WS : [ \f\b\t\r]+ -> skip ; // skip spaces, tabs

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literal 
INT: [0-9]+;

REAL : DEPART? INPART? EXPART  
	 | DEPART INPART?;

STRING_LIT: '"' (STRINGCHAR)* '"' {self.text = self.text[1:-1];};

// TODO ERROR
UNCLOSE_STRING: '"' (STRINGCHAR)* ('\r\n' | '\n' | EOF)
{
	if self.text[-1] == '\n' and self.text[-2] == '\r':
		raise UncloseString(self.text[1:-2])
	elif self.text[-1] == '\n':
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE
    : '"' (ILLSTRING)* ( '\\' ~[\r\\'"] | [\r]) '"'?
    {
        if self.text[-1] == '"':
            raise IllegalEscape(self.text[1:-1])

        raise IllegalEscape(self.text[1:])
    }
    | '"' (ILLSTRING)* '\\' '"'
    {
            raise IllegalEscape(self.text[1:])
    }
    | '"' (ILLSTRING)* ('\''(~[\r\n\\'"]))* '"'
    {
        raise IllegalEscape(self.text[1:-1])
    };
ERROR_CHAR: . {raise ErrorToken(self.text)};
//!  -------------------------- end Lexical structure ------------------- //