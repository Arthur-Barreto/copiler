class SymbolTable:
    def __init__(self):
        self.symbol = {}
        self.offset = 4

    def create_identifier(self, key, value=None, offset=0, signal=1):

        self.symbol[key] = (value, None, (self.offset + offset) * signal)
        self.offset += 4

    def set_identifier(self, key, value=None):

        if key not in self.symbol:
            raise TypeError("You must declare the variable first !")

        offset = self.symbol[key][2]
        self.symbol[key] = (None, None, offset)

    def get_identifier(self, key):
        if key in self.symbol:
            return self.symbol[key]
        raise TypeError("Var not declared !")

    def check_var_exists(self, key):
        return key in self.symbol
