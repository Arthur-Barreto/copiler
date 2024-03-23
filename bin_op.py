from node import Node


class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        n1 = self.children[0].evaluate(symble_table)
        n2 = self.children[1].evaluate(symble_table)

        if self.value == "+":
            return n1 + n2
        elif self.value == "-":
            return n1 - n2
        elif self.value == "*":
            return n1 * n2
        elif self.value == "/":
            return n1 // n2
