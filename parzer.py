from tokenizer import Tokenizer
from bin_op import BinOp
from un_op import UnOp
from int_val import IntVal
from no_op import NoOp
from assignment import Assignment
from identifier import Identifier
from print_node import Print
from block import Block
from while_node import WhileOp
from if_node import IfOp
from read_val import ReadVal


class Parser:
    tokenizer = None

    @staticmethod
    def parse_block():

        block = Block(children=[])

        while Parser.tokenizer.next.type != "EOF":
            line = Parser.parse_statement()
            block.children.append(line)

        return block

    @staticmethod
    def parse_statement():

        if Parser.tokenizer.next.type == "NEWLINE":
            Parser.tokenizer.select_next()
            return NoOp()

        elif Parser.tokenizer.next.type == "IDENTIFIER":

            variable = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "ASSIGN":
                raise SyntaxError("Missing '='")

            Parser.tokenizer.select_next()
            res = Parser.bool_expression()

            if Parser.tokenizer.next.type != "NEWLINE":
                print(
                    f"esperado new line, obtido: {Parser.tokenizer.next.type} | {Parser.tokenizer.next.value}"
                )
                raise SyntaxError("Missing newline after empty line")

            Parser.tokenizer.select_next()
            return Assignment(value=variable, children=[res])

        elif Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise SyntaxError("Missing '('")

            Parser.tokenizer.select_next()
            res = Parser.bool_expression()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'print'")

            Parser.tokenizer.select_next()
            return Print(children=[res])

        elif Parser.tokenizer.next.type == "WHILE":
            Parser.tokenizer.select_next()
            while_conditional = Parser.bool_expression()

            if Parser.tokenizer.next.type != "DO":
                raise SyntaxError("Missing 'do'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'do'")

            Parser.tokenizer.select_next()

            while_block = Block(children=[])
            while Parser.tokenizer.next.type != "END":
                line = Parser.parse_statement()
                while_block.children.append(line)

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing newline after 'end' from 'while'")

            Parser.tokenizer.select_next()
            return WhileOp(
                value=None,
                children=[while_conditional, while_block],
            )

        elif Parser.tokenizer.next.type == "IF":
            Parser.tokenizer.select_next()
            if_conditional = Parser.bool_expression()

            if Parser.tokenizer.next.type != "THEN":
                raise SyntaxError("Missing 'then' after 'if'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "NEWLINE":
                raise SyntaxError("Missing nweline after 'then' from 'if'")

            Parser.tokenizer.select_next()

            if_block = Block(children=[])
            else_block = Block(children=[])
            while Parser.tokenizer.next.type not in ["ELSE", "END"]:
                line = Parser.parse_statement()
                if_block.children.append(line)

            if Parser.tokenizer.next.type == "END":
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'end' from 'if'")

                Parser.tokenizer.select_next()
                return IfOp(
                    value=None,
                    children=[if_conditional, if_block, else_block],
                )

            elif Parser.tokenizer.next.type == "ELSE":
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'else'")

                Parser.tokenizer.select_next()

                while Parser.tokenizer.next.type != "END":
                    line = Parser.parse_statement()
                    else_block.children.append(line)

                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type != "NEWLINE":
                    raise SyntaxError("Missing newline after 'end' from 'else'")

                Parser.tokenizer.select_next()
                return IfOp(
                    value=None,
                    children=[if_conditional, if_block, else_block],
                )
            else:
                raise SyntaxError("Missing 'end' or 'else' after 'if'")

        else:
            print(f"{Parser.tokenizer.next.type} | {Parser.tokenizer.next.value}")
            raise SyntaxError("Invalid Input")

    @staticmethod
    def bool_expression():
        result = Parser.bool_term()

        while Parser.tokenizer.next.type == "OR":
            operator = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.bool_term()],
            )

        return result

    @staticmethod
    def bool_term():
        result = Parser.relational_expression()

        while Parser.tokenizer.next.type == "AND":
            operator = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.relational_expression()],
            )

        return result

    @staticmethod
    def relational_expression():
        result = Parser.parse_expression()

        while Parser.tokenizer.next.type in ["EQ", "LT", "GT"]:
            operator = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            result = BinOp(
                value=operator,
                children=[result, Parser.parse_expression()],
            )

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
            return UnOp(
                value="+",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.select_next()
            return UnOp(
                value="-",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.select_next()
            return UnOp(
                value="not",
                children=[Parser.parse_factor()],
            )

        elif Parser.tokenizer.next.type == "LPAREN":
            Parser.tokenizer.select_next()
            result = Parser.bool_expression()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')'")
            Parser.tokenizer.select_next()
            return result

        elif Parser.tokenizer.next.type == "READ":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "LPAREN":
                raise SyntaxError("Missing '(' after 'read'")

            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type != "RPAREN":
                raise SyntaxError("Missing ')' after read")

            Parser.tokenizer.select_next()

            return ReadVal()

        else:
            raise SyntaxError("Invalid Input")

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        return Parser.parse_block()
