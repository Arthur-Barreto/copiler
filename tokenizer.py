class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = Token(type=None, value="")

    def select_next(self):

        if len(self.source) == 0:
            raise TypeError(f"Empty Input")

        while self.position < len(self.source):
            char = self.source[self.position]

            print(
                f"type= {self.next.type} value= {self.next.value} idx= {self.position} antessssssss"
            )

            if char == " ":
                self.position += 1

            elif char == "+":
                self.next.type = "PLUS"
                self.next.value = "+"
                self.position += 1
                return

            elif char == "-":
                self.next.type = "MINUS"
                self.next.value = "-"
                self.position += 1
                return

            elif char.isdigit():
                self.next.type = "INT"
                self.next.value = char
                self.position += 1
                while (
                    self.position < len(self.source)
                    and self.source[self.position].isdigit()
                ):
                    self.next.value += self.source[self.position]
                    self.position += 1
                self.next.value = int(self.next.value)
                return

            else:
                raise TypeError(f"invalid char: '{char}' NOT ALLOWED !")

        print(f"type= {self.next.type} value= {self.next.value} idx= {self.position} meioooo")

        self.next.type = "EOF"
        self.next.value = ""

        print(f"type= {self.next.type} value= {self.next.value} idx= {self.position} fimmmmmm")
