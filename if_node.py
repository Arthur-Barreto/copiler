from node import Node
from write import Write


class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        Write.code += f"IF_{self.id}:\n"

        conditional = self.children[0].evaluate(symble_table)

        Write.code += f"CMP EAX, False\n"
        Write.code += f"JE ELSE_{self.id}\n"

        self.children[1].evaluate(symble_table)

        Write.code += f"JMP EXIT_{self.id}\n"

        Write.code += f"ELSE_{self.id}:\n"

        self.children[2].evaluate(symble_table)

        Write.code += f"EXIT_{self.id}:\n"
