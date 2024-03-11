from node import Node


class BinOp(Node):
    def __init__(self, value, children: list[Node]):
        super().__init__(value, children)

    def evaluate(self):
        n1 = self.children[0].evaluate()
        n2 = self.children[1].evaluate()
        if self.value == "+":
            return n1 + n2
        elif self.value == "-":
            return n1 - n2
        elif self.value == "*":
            return n1 * n2
        elif self.value == "/":
            return n1 // n2
