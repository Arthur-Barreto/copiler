from node import Node


class UnOp(Node):
    def __init__(self, value, children: list[Node]):
        super().__init__(value, children)

    def evaluate(self):
        if self.value == "-":
            return -self.children[0].evaluate()
        return self.children[0].evaluate()
