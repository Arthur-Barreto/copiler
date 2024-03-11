from node import Node


class IntVal(Node):
    def __init__(self, value: int):
        super().__init__(value, [])

    def evaluate(self):
        return self.value
