from node import Node
from func_table import FuncTable


class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, func_table):
        func_name = self.children[0].value
        FuncTable.create_identifier(func_name, self)
