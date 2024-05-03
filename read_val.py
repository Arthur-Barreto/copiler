from node import Node
from write import Write


class ReadVal(Node):
    def __init__(self):
        super().__init__(None, [])
        # Node.get_id()

    def evaluate(self, symbol_table):
        Write.write("PUSH scanint\n")
        Write.write("PUSH formatin\n")
        Write.write("call scanf\n")
        Write.write("ADD ESP, 8\n")
        Write.write("MOV EAX, DWORD [scanint]\n")
        return (int(input()), "INT")
