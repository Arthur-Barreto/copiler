from node import Node
from write import Write


class Print(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def evaluate(self, symble_table):
        single_child = self.children[0].evaluate(symble_table)[0]
        Write.write("PUSH EAX\n")
        Write.write("PUSH formatout\n")
        Write.write("CALL printf\n")
        Write.write("ADD ESP, 8\n")
        print(single_child)
