from node import Node
from write import Write


class Identifier(Node):
    def __init__(self, value):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        try:
            offset = symble_table.get_identifier(self.value)[2]
            Write.write(f"MOV EAX, [EBP-{offset}]\n")
            return symble_table.get_identifier(key=self.value)
        except:
            raise TypeError("Undefined variable: " + self.value)
