from node import Node
from symbol_table import SymbolTable
from func_table import FuncTable


class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        func_node = FuncTable.get_identifier(self.value)
        identifier, args, block = func_node.children[0], func_node.children[1:-1], func_node.children[-1]

        if len(args) != (len(self.children)):
            raise TypeError(
                f"Function {self.value} called with wrong number of arguments, got {len(self.children)}, expected {len(args)}!"
            )

        local_table = SymbolTable()

        # exec from vrdec on local table
        for arg in args:
            arg.evaluate(local_table)

        # assign form args on local table
        for i, key in enumerate(local_table.symbol):
            local_table.set_identifier(key, self.children[i].evaluate(symble_table))

        return block.evaluate(local_table)
