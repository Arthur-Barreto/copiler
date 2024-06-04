from node import Node
from write import Write


class WhileOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        Write.code += f"LOOP_{self.id}:\n"

        conditional = self.children[0].evaluate(symble_table)

        Write.code += f"CMP EAX, False\n"
        Write.code += f"JE EXIT_{self.id}\n"

        block = self.children[1].evaluate(symble_table)

        Write.code += f"JMP LOOP_{self.id}\n"
        Write.code += f"EXIT_{self.id}:\n"

        # while conditional and block is not None:
        #     block
            
            # if block is not None:
            #     return block
