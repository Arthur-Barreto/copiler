from node import Node


class NoOp(Node):
    def __init__(self, value: any, children: list[Node]):
        super().__init__(value, children)

    def evaluate(self):
        pass
