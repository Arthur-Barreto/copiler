from node import Node
from write import Write


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        single_child = self.children[0].evaluate(symble_table)

        if type(single_child) == bool:
            if single_child:
                single_child = (1, "INT")
            else:
                single_child = (0, "INT")

        if self.value == "-":
            Write.write(";;;; unop - ;;;;\n")
            Write.write(f"NEG EAX\n")
            Write.write(";;;; fim unop - ;;;;\n")
            return (-single_child[0], "INT")
        elif self.value == "+":
            return (single_child[0], "INT")
        elif self.value == "not":
            Write.write(";;;; unop not ;;;;\n")
            Write.write(f"NOT EAX\n")
            Write.write(";;;; fim unop not ;;;;\n")
            return not (single_child[0], "INT")
