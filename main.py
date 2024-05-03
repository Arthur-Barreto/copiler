from parzer import Parser
from pre_pro import PrePro
from symbol_table import SymbolTable
import sys
from write import Write

if __name__ == "__main__":

    file_name = sys.argv[1]

    with open("file_name.txt", "w") as f:
        f.write(file_name.split(".")[0])

    Write.header()

    lua_code = PrePro.filter(file_name)
    s_table = SymbolTable()
    tree = Parser.run(lua_code)

    if Parser.tokenizer.next.type != "EOF":
        raise SyntaxError("Should have an operator! ")

    result = tree.evaluate(symble_table=s_table)

    Write.footer()

    for k in s_table.symbol:
        print(f"{k} = {s_table.symbol[k]}")

    if result != None:
        print(result)
