from node import Node


class StrVal(Node):
    def __init__(self, value: str):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        pass
        # return (self.value, "STRING")
