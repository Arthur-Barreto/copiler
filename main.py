import sys

# pegar a entrada do programa
raw_data = sys.argv[1]

# removendo os espaços
processed = raw_data.replace(" ", "")

actual_number = ""

allowed_operations = ["+", "-"]

numbers = []
operations = []

for i in range(len(processed)):

    char = processed[i]

    if char.isnumeric():
        actual_number += char

    else:
        if i == 0:
            raise TypeError("First character must be a number")
        elif i == (len(processed) - 1):
            raise TypeError("Last character must be a number")
        elif char not in allowed_operations:
            raise TypeError(f"Invalid operation for {char}")
        elif char in allowed_operations:
            numbers.append(int(actual_number))
            actual_number = ""
            operations.append(char)

numbers.append(int(actual_number))

res = numbers[0]

numbers.pop(0)

for num, op in zip(numbers, operations):
    if op == "+":
        res += num
    else:
        res -= num
print(res)