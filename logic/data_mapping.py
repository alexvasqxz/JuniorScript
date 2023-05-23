class MapeoDatos():
    def __init__(self):
        self.mapa = {
            'vacio': 0,
            'entero': 1,
            'decimal': 2,
            'logico': 3,
            'letra': 4,
            'pointer' : 5,
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
            'SALTO' : 40,
            'SALTOV' : 41,
            'SALTOF' : 42,
            'SALTOMOD' : 50,
            'RECURSOS' : 51,
            'PARAMETRO' : 52,
            'RETURN': 53,
            'FINFUN': 60,
            'FINPRO' : 80,
            'LIMINF' : 90,
            'LIMSUP' : 91,
        }

    def map_type(self, type):
        return self.mapa.get(type, -1)
