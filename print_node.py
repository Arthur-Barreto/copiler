from node import Node
from write import Write


class Print(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        single_child = self.children[0].evaluate(symble_table)
        Write.code += "PUSH EAX\n"
        Write.code += "PUSH formatout\n"
        Write.code += "CALL printf\n"
        Write.code += "ADD ESP, 8\n"
        # print(single_child)
