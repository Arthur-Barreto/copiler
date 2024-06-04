from node import Node
from write import Write


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        self.children[0].evaluate(symble_table)

        # if type(single_child) == bool:
        #     if single_child:
        #         single_child = (1, "INT")
        #     else:
        #         single_child = (0, "INT")

        if self.value == "-":
            Write.code += f"NEG EAX\n"
            # return (-single_child[0], "INT")
        elif self.value == "not":
            Write.code += f"NOT EAX\n"
            # return not (single_child[0], "INT")
        else:
            raise TypeError(f"Invalid unary operator {self.value}!")
