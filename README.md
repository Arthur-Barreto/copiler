# Copiler

![git status]( http://3.129.230.99/svg/Arthur-Barreto/copiler/)

## Diagrama Sintático

<img src="img/diagrama.svg" alt="drawing" width="800"/>

## EBNF

BLOCK = { STATEMENT };

STATEMENT = ( "λ" | ASSIGNMENT | PRINT | WHILE | IF ), "\n" ;

ASSIGNMENT = IDENTIFIER, "=", BOOL_EXP ;

PRINT = "print", "(", BOOL_EXP, ")" ;

WHILE = "while", BOOL_EXP, "do", "\n", "λ", { ( STATEMENT ), "λ" }, "end";

IF = "if", BOOL_EXP, "then", "\n", "λ", { ( STATEMENT ), "λ" }, ( "λ" | ( "else", "\n", "λ", { ( STATEMENT ), "λ" })), "end" ;

BOOL_EXP = BOOL_TERM, { ("or"), BOOL_TERM } ;

BOOL_TERM = REL_EXP, { ("and"), REL_EXP } ;

REL_EXP = EXPRESSION, { ("==" | ">" | "<"), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = NUMBER | IDENTIFIER | (("+" | "-" | "not"), FACTOR ) | "(", BOOL_EXP, ")" | "read", "(", ")" ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;

DIGIT = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
