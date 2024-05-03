from node import Node
from write import Write


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
        # Node.get_id()

    def evaluate(self, symble_table):

        single_child = self.children[0].evaluate(symble_table)
        print(single_child)

        if self.value == "-":
            Write.write(";;;; unop - ;;;;\n")
            Write.write(f"NEG EAX\n")
            Write.write(";;;; fim unop - ;;;;\n")
            return (-single_child, "INT")
        elif self.value == "+":
            return (single_child, "INT")
        elif self.value == "not":
            return not (single_child, "INT")
