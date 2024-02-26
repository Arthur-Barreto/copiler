from tokenizer import Tokenizer


class Parser:
    tokenizer = None

    @staticmethod
    def parse_term():
        result = Parser.tokenizer.next.value
        if Parser.tokenizer.next.type == "INT":
            result = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            while Parser.tokenizer.next.value in ["*", "/"]:
                if Parser.tokenizer.next.value == "*":
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "INT":
                        result *= Parser.tokenizer.next.value
                    else:
                        raise TypeError(
                            f"Input must be a number for: {Parser.tokenizer.value}"
                        )
                elif Parser.tokenizer.next.value == "/":
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type == "INT":
                        result //= Parser.tokenizer.next.value
                    else:
                        raise TypeError(
                            f"Input must be a number for: {Parser.tokenizer.value}"
                        )
                Parser.tokenizer.select_next()

            return result
        else:
            raise TypeError(f"Invalid for char= '{Parser.tokenizer.next.value}'")

    @staticmethod
    def parse_expression():
        result = Parser.parse_term()

        while Parser.tokenizer.next.value in ["+", "-"]:
            if Parser.tokenizer.next.value == "+":
                Parser.tokenizer.select_next()
                result += Parser.parse_term()

            elif Parser.tokenizer.next.value == "-":
                Parser.tokenizer.select_next()
                result -= Parser.parse_term()

        return result

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_expression()
