from node import Node
from symbol_table import SymbolTable
from func_table import FuncTable
from write import Write


class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        func_node = FuncTable.get_identifier(self.value)
        identifier, args, block = (
            func_node.children[0],
            func_node.children[1:-1],
            func_node.children[-1],
        )

        if len(args) != (len(self.children)):
            raise TypeError(
                f"Function {self.value} called with wrong number of arguments, got {len(self.children)}, expected {len(args)}!"
            )

        # exec from vrdec on local table
        for arg in args:
            Write.code += "PUSH EAX\n"
            arg.evaluate(symble_table)
            
        Write.code += f"CALL {self.value}\n"
        Write.code += f"ADD ESP, {4 * len(args)}\n"

        # # assign form args on local table
        # for i, key in enumerate(symble_table.symbol):
        #     symble_table.set_identifier(key, self.children[i].evaluate(symble_table))

        # return block.evaluate(symble_table)
