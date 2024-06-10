from node import Node
from write import Write


class Identifier(Node):
    def __init__(self, value):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        try:
            offset = symble_table.get_identifier(self.value)[2]
            if offset > 0:
                Write.code += f"MOV EAX, [EBP-{offset}]\n"
            else:
                Write.code += f"MOV EAX, [EBP+{abs(offset)}]\n"
            # return symble_table.get_identifier(key=self.value)
        except Exception as e:
            print(f"symbol table: {symble_table}")
            raise TypeError("Undefined variable: " + self.value)
