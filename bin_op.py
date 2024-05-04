from node import Node
from write import Write


class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symble_table):

        right_child = self.children[1].evaluate(symble_table)
        Write.code += f"PUSH EAX\n"
        left_child = self.children[0].evaluate(symble_table)
        Write.code += f"POP EBX\n"

        if type(left_child) == bool:
            if left_child:
                left_child = (1, "INT")
            else:
                left_child = (0, "INT")

        if type(right_child) == bool:
            if right_child:
                right_child = (1, "INT")
            else:
                right_child = (0, "INT")

        if left_child[1] == right_child[1] and (self.value in ["EQ", "LT", "GT"]):

            Write.code += f"CMP EAX, EBX\n"

            if self.value == "EQ":
                Write.code += f"CALL binop_je\n"
                if left_child[0] == right_child[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

            elif self.value == "LT":
                Write.code += f"CALL binop_jl\n"
                if left_child[0] < right_child[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

            elif self.value == "GT":
                Write.code += f"CALL binop_jg\n"
                if left_child[0] > right_child[0]:
                    return (1, "INT")
                else:
                    return (0, "INT")

        elif (
            (left_child[1] == "INT")
            and (right_child[1] == "INT")
            and (self.value in ["PLUS", "MINUS", "MULT", "DIV", "AND", "OR"])
        ):

            if self.value == "PLUS":
                Write.code += f"ADD EAX, EBX\n"
                return (left_child[0] + right_child[0], "INT")

            elif self.value == "MINUS":
                Write.code += f"SUB EAX, EBX\n"
                return (left_child[0] - right_child[0], "INT")

            elif self.value == "MULT":
                Write.code += f"IMUL EAX, EBX\n"
                return (left_child[0] * right_child[0], "INT")

            elif self.value == "DIV":
                Write.code += f"IDIV EAX, EBX\n"
                return (left_child[0] // right_child[0], "INT")

            elif self.value == "AND":
                bool_value = left_child[0] and right_child[0]
                Write.code += f"AND EAX, EBX\n"
                if bool_value:
                    return (1, "INT")
                else:
                    return (0, "INT")

            elif self.value == "OR":
                bool_value = left_child[0] or right_child[0]
                Write.code += f"OR EAX, EBX\n"
                if bool_value:
                    return (1, "INT")
                else:
                    return (0, "INT")

        elif self.value == "DOUBLE_DOT":
            return (str(left_child[0]) + str(right_child[0]), "STRING")

        else:
            print(f"op= {self.value}")
            raise TypeError("Unknow operation !")
