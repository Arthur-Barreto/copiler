from node import Node
from write import Write


class IntVal(Node):
    def __init__(self, value: int):
        super().__init__(value, [])

    def evaluate(self, symble_table):
        Write.code += f"MOV EAX, {self.value}\n"
