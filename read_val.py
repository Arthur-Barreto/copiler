from node import Node
from write import Write


class ReadVal(Node):
    def __init__(self):
        super().__init__(None, [])

    def evaluate(self, symbol_table):
        Write.code += "PUSH scanint\n"
        Write.code += "PUSH formatin\n"
        Write.code += "call scanf\n"
        Write.code += "ADD ESP, 8\n"
        Write.code += "MOV EAX, DWORD [scanint]\n"
        # return (int(input()), "INT")
