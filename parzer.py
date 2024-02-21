from tokenizer import Tokenizer


class Parser:
    tokenizer = None

    @staticmethod
    def parse_expression():
        while Parser.tokenizer.next.type != "EOF":
            result = None
            if Parser.tokenizer.next.type == "INT":
                result = Parser.tokenizer.next.value
                Parser.tokenizer.select_next()
                while Parser.tokenizer.next.value in ["+", "-"]:
                    if Parser.tokenizer.next.value == "+":
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "INT":
                            result += Parser.tokenizer.next.value
                        else:
                            raise TypeError(
                                f"Input must be a number for: {Parser.tokenizer.value}"
                            )
                    elif Parser.tokenizer.next.value == "-":
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "INT":
                            result -= Parser.tokenizer.next.value
                        else:
                            raise TypeError(
                                f"Input must be a number for: {Parser.tokenizer.value}"
                            )
                    Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "EOF":
                    raise TypeError(f"Invalid token for end of file!")

                return result
            else:
                raise TypeError(f"Invalid for char= '{Parser.tokenizer.next.value}'")

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_expression()
