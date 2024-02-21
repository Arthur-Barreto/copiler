from parzer import Parser
import sys

if __name__ == "__main__":
    res = Parser.run(sys.argv[1])

    print(res)
