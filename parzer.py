from tokenizer import Tokenizer
from bin_op import BinOp
from un_op import UnOp
from int_val import IntVal
from no_op import NoOp
from assignment import Assignment
from identifier import Identifier
from print_node import Print
from block import Block


class Parser:
    tokenizer = None

    @staticmethod
    def parse_block():

        block = Block(children=[])

        while Parser.tokenizer.next.type != "EOF":
            line = Parser.parse_statement()
            block.children.append(line)
            Parser.tokenizer.select_next()

        return block

    @staticmethod
    def parse_statement():

        result = NoOp()

        if Parser.tokenizer.next.type == "IDENTIFIER":

            variable = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "ASSIGN":
                raise TypeError("Missing '='")

            Parser.tokenizer.select_next()
            res = Parser.parse_expression()
            result = Assignment(value=variable, children=[res])

        elif Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise TypeError("Missing '('")

            Parser.tokenizer.select_next()
            res = Parser.parse_expression()

            if Parser.tokenizer.next.type != "RPAREN":
                raise TypeError("Missing ')'")

            Parser.tokenizer.select_next()
            result = Print(children=[res])

        return result

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
        elif Parser.tokenizer.next.type == "IDENTIFIER":
            result = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return Identifier(value=result)
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
        return Parser.parse_block()
