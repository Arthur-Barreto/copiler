# Copiler

![git status]( http://3.129.230.99/svg/Arthur-Barreto/copiler/)

## Diagrama Sintático

![Diagrama Sintático](/img/diagrama.png)

## EBNF

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | number ;
