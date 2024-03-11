from tokenizer import Tokenizer
from bin_op import BinOp
from un_op import UnOp
from int_val import IntVal
from no_op import NoOp


class Parser:
    tokenizer = None

    @staticmethod
    def parse_expression():
        result = Parser.parse_term()

        while Parser.tokenizer.next.value in ["+", "-"]:
            operator = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_term()],
            )
        return result

    @staticmethod
    def parse_term():
        result = Parser.parse_factor()

        while Parser.tokenizer.next.value in ["*", "/"]:
            operator = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_factor()],
            )

        return result

    @staticmethod
    def parse_factor():
        if Parser.tokenizer.next.type == "INT":
            result = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return IntVal(value=result)
        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.select_next()
            return UnOp(value="+", children=[Parser.parse_factor()])
        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.select_next()
            return UnOp(value="-", children=[Parser.parse_factor()])
        elif Parser.tokenizer.next.type == "LPAREN":
            Parser.tokenizer.select_next()
            result = Parser.parse_expression()
            if Parser.tokenizer.next.type != "RPAREN":
                raise TypeError("Missing ')'")
            Parser.tokenizer.select_next()
            return result
        else:
            raise TypeError("Invalid Input")

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_expression()
