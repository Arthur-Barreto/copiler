class FuncTable:
    table = {}

    @staticmethod
    def get_identifier(name):
        if name in FuncTable.table:
            return FuncTable.table[name]
        raise TypeError(f"Function {name} not declared , invalid get!")

    @staticmethod
    def create_identifier(name, value):
        if name in FuncTable.table:
            raise TypeError(f"Function {name} already declared, invalid create!")
        FuncTable.table[name] = value
