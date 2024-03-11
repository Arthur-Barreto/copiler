from parzer import Parser
from pre_pro import PrePro
import sys

if __name__ == "__main__":

    file_name = sys.argv[1]

    lua_code = PrePro.filter(file_name)

    tree = Parser.run(lua_code)

    if Parser.tokenizer.next.type != "EOF":
        raise TypeError("Should have an operator! ")

    print(tree.evaluate())
