from node import Node
from func_table import FuncTable
from write import Write
from symbol_table import SymbolTable


class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, func_table):
        func_name = self.children[0].value
        FuncTable.create_identifier(func_name, self)
        Write.code += f"JMP {func_name}_END\n"
        Write.code += f"{func_name}:\n"
        Write.code += f"PUSH EBP\n"
        Write.code += f"MOV EBP, ESP\n"

        local_table = SymbolTable()
        for arg in self.children[1:-1]:
            local_table.create_identifier(arg.value, None, offset=4, signal=-1)

        self.children[-1].evaluate(local_table)

        Write.code += f"MOV ESP, EBP\n"
        Write.code += f"POP EBP\n"
        Write.code += f"RET\n"
        Write.code += f"{func_name}_END:\n"
