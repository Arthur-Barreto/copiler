from parzer import Parser
from pre_pro import PrePro
from symbol_table import SymbolTable
import sys


if __name__ == "__main__":

    file_name = sys.argv[1]
    lua_code = PrePro.filter(file_name)
    s_table = SymbolTable()
    tree = Parser.run(lua_code)

    if Parser.tokenizer.next.type != "EOF":
        raise SyntaxError("Should have an operator! ")

    result = tree.evaluate(symble_table=s_table)

    # for var in s_table.symbol:
    #     print(f"{var} = {s_table.symbol[var]}")

    if result != None:
        print(result)
