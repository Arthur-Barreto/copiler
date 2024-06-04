from node import Node
from write import Write


class Assignment(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        right_child = self.children[1].evaluate(symble_table)
        offset = symble_table.get_identifier(self.children[0])[2]
        if offset > 0:
            Write.code += f"MOV [EBP-{offset}], EAX\n"
        else:
            Write.code += f"MOV [EBP+{abs(offset)}], EAX\n"
        # symble_table.set_identifier(self.children[0], right_child)
