from node import Node


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        if self.value == "-":
            return -self.children[0].evaluate(symble_table)
        return self.children[0].evaluate(symble_table)
