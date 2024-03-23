from node import Node


class Identifier(Node):
    def __init__(self, value):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        try:
            return symble_table.get_identifier(key=self.value)
        except:
            raise TypeError("Undefined variable: " + self.value)
