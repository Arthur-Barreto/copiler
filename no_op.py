from node import Node


class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self):
        pass
