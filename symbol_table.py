class SymbolTable:
    def __init__(self):
        self.symbol = {}

    def get_identifier(self, key):
        if key in self.symbol:
            return self.symbol[key]
        raise TypeError("Var not declared !")
        
        
    def set_identifier(self, key, value):
        self.symbol[key] = value
