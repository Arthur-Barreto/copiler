from node import Node
from symbol_table import SymbolTable
from func_table import FuncTable
from write import Write


class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        func_node = FuncTable.get_identifier(self.value)

        if (len(func_node.children) - 2) != (len(self.children)):
            raise TypeError(
                f"Function {self.value} called with wrong number of arguments, got {len(self.children)}, expected {len(func_node.children) - 2}!"
            )

        # exec from vrdec on local table
        for arg in self.children:
            arg.evaluate(symble_table)
            Write.code += "PUSH EAX\n"

        Write.code += f"CALL {self.value}\n"
        Write.code += f"ADD ESP, {4 * len(self.children)}\n"
