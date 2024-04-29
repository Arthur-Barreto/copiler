from node import Node


class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        if self.children[0].evaluate(symble_table)[1] != "INT":
            raise SyntaxError("Wrong type, should be 'int' for 'unop' !")

        if self.value == "-":
            return (-self.children[0].evaluate(symble_table)[0], "INT")
        elif self.value == "+":
            return (self.children[0].evaluate(symble_table)[0], "INT")
        elif self.value == "not":
            return not (self.children[0].evaluate(symble_table)[0], "INT")
