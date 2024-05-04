import sys
from write import Write

if __name__ == "__main__":
    filename = sys.argv[1]
    Write.header(filename)
    Write.write(filename, "ola testesteeeeeee\n")
    Write.footer(filename)
