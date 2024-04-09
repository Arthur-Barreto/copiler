# Copiler

![git status]( http://3.129.230.99/svg/Arthur-Barreto/copiler/)

## Diagrama Sintático

![Diagrama Sintático](/img/diagrama.png)

## EBNF

BLOCK = { STATEMENT } ;

STATEMENT = ( "λ" | ASSIGNMENT | PRINT), "\n" ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = NUMBER | IDENTIFIER | (("+" | "-" ), FACTOR ) | "(", EXPRESSION, ")" ;
