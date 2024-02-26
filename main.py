from parzer import Parser
import sys

if __name__ == "__main__":
    res = Parser.run(sys.argv[1])

    if Parser.tokenizer.next.type != "EOF":
        raise TypeError("Should have an operator! ")

    print(res)
