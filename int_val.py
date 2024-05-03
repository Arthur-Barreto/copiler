from node import Node
from write import Write


class IntVal(Node):
    def __init__(self, value: int):
        super().__init__(value, [])
        # Node.get_id()

    def evaluate(self, symble_table):
        Write.write(";;; int_val ;;;\n")
        Write.write(f"MOV EAX, {self.value}\n")
        Write.write(";;; fim int_val ;;;\n")
        return (self.value, "INT")
