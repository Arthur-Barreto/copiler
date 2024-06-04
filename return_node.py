from node import Node
from write import Write


class ReturnNode(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        self.children[0].evaluate(symble_table)
        Write.code += f"MOV ESP, EBP\n"
        Write.code += f"POP EBP\n"
        Write.code += "RET\n"
