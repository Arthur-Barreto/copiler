class SymbolTable:
    def __init__(self):
        self.symbol = {}
        self.offset = 4

    def create_identifier(self, key, value=None, offset=0, signal=1):
        if key in self.symbol:
            raise TypeError("Var already declared !")
        if value is not None:
            self.symbol[key] = (value[0], value[1], (self.offset + offset) * signal)
        else:
            self.symbol[key] = (None, None, (self.offset + offset) * signal)
        self.offset += 4

    def set_identifier(self, key, value=None):

        if key not in self.symbol:
            raise TypeError("You must declare the variable first !")

        offset = self.symbol[key][2]
        
        self.symbol[key] = (None, None, offset)

        # if type(value) in [int, bool]:
        #     self.symbol[key] = (int(value), "INT", offset)

        # elif type(value) == str:
        #     self.symbol[key] = (value, "STRING", offset)

        # elif type(value) == tuple:
        #     if value[1] == "INT":
        #         self.symbol[key] = (value[0], "INT", offset)
        #     elif value[1] == "STRING":
        #         self.symbol[key] = (value[0], "STRING", offset)

        # elif value is None:
        #     self.symbol[key] = (None, None, offset)

        # else:
        #     print(f"type= {type(value)}")
        #     raise TypeError("Invalid type atribution!")

    def get_identifier(self, key):
        if key in self.symbol:
            return self.symbol[key]
        raise TypeError("Var not declared !")

    def check_var_exists(self, key):
        return key in self.symbol
