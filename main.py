import sys

# pegar a entrada do programa
raw_data = sys.argv[1]

# removendo os espaços
raw_data = raw_data.replace(" ", "")

# se o primerio ou o último for um caracter nao forem numero, dar raise
if (not raw_data[0].isnumeric() or not raw_data[-1].isnumeric()):
    raise TypeError("Fisrt or Last character not allowed !")

# contando o nuimero de simbolos na entrada
times_plus = raw_data.count("+")
times_subtraction = raw_data.count("-")
total_operations = times_plus + times_subtraction

# quebrando no simbolo do +
splited_plus = raw_data.split('+')

# verificando se digitou mais de um simbolo de + junto
for c in splited_plus:
    if c == "":
        raise TypeError("Two or more '+' were typed together")
    
splited_sub = raw_data.split('-')

# verificando se digitou mais de um simbolo de - junto
for c in splited_sub:
    if c == "":
        raise TypeError("Two or more '-' were typed together")

# lista de carateres permitidos
allowed_icons = ['+', '-']
    
numbers = []
operations = []

for c in raw_data:
    if c.isnumeric():
        numbers.append(c)
    else:
        operations.append(c)
        
print(numbers, operations)