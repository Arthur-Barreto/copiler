# Copiler

![git status]( http://3.129.230.99/svg/Arthur-Barreto/copiler/)

## Diagrama Sintático

![Diagrama Sintático](/img/diagrama.png)

## EBNF

BLOCK = { STATEMENT } ;

STATEMENT = ("\n" | IDENTIFIER, "=",  EXPRESSION , "\n" | PRINT + "(" + EXPRESSION + ")", "\n") ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | number | identifier ;
