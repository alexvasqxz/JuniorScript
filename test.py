import json
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, datatype):
        if name in self.symbols:
            raise Exception(f"Error: '{name}' already declared in current scope")
        self.symbols[name] = {'datatype': datatype}

    def get_symbol(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return None

    def update_symbol(self, name, value):
        if name in self.symbols:
            self.symbols[name]['value'] = value
            self.symbols["Symbol3"]["Scope"] = "global"
        else:
            raise Exception(f"Error: '{name}' not declared in current scope")

table = SymbolTable()
table.add_symbol("Symbol1", "Integer")
table.add_symbol("Symbol2", "Integer")
table.add_symbol("Symbol3", "Integer")
table.update_symbol("Symbol2", 5)

print(table.symbols)
# {
#     'Symbol1': {
#         'datatype': 'Integer'
#     },
#     'Symbol2': {
#         'datatype': 'Integer',
#         'value': 5
#     },
#     'Symbol3': {
#         'datatype': 'Integer'
#     }
# }

