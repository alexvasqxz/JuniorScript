class MapeoDatos():
    def __init__(self):
        self.mapa = {
            'vacio': 0,
            'entero': 1,
            'decimal': 2,
            'logico': 3,
            'letra': 4,
            '=': 10,
            '<': 11,
            '>': 12,
            '<=': 13,
            '>=': 14,
            '==': 15,
            '!=': 16,
            '+': 17,
            '-': 18,
            '*': 19,
            '/': 20,
            'YYY': 21,
            'OOO': 22,
            'imprimir': 30,
            'leer': 31,
        }

    def map_type(self, type):
        return self.mapa.get(type, -1)
