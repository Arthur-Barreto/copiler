from node import Node


class Block(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        for line in self.children:
            line.evaluate(symble_table)
