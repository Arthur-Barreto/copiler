from node import Node
from write import Write


class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        Write.code += f"IF_{self.id}:\n"

        conditional = self.children[0].evaluate(symble_table)
        # print(f"conditional[0]= {conditional[0]} | conditional[1]= {conditional[1]}")

        Write.code += f"CMP EAX, False\n"
        Write.code += f"JE ELSE_{self.id}\n"

        if_block = self.children[1].evaluate(symble_table)

        Write.code += f"JMP EXIT_{self.id}\n"

        if conditional[0] == 1:
            return_if = if_block

            if return_if is not None:
                return return_if

        else:

            Write.code += f"ELSE_{self.id}:\n"

            else_block = self.children[2].evaluate(symble_table)

            Write.code += f"EXIT_{self.id}:\n"

            return_else = else_block

            if return_else is not None:
                return return_else
