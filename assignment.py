from node import Node


class Assignment(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):
        if self.children[0] is not None:
            symble_table.set_identifier(
                key=self.value, value=self.children[0].evaluate(symble_table)
            )
        else:
            symble_table.set_identifier(key=self.value, value=None)
