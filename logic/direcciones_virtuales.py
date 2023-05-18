class DireccionesVirtuales():
    def __init__(self):
        self.tabla_direcciones = [
            #Globales - Variables
            [1000, 1999], # Enteros
            [2000, 2999], # Decimales
            [3000, 3999], # Logicos
            [4000, 4999], # Letras
            # Globales - Temporales
            [10000, 11999],
            [12000, 13999],
            [14000, 15999],
            [16000, 17999],
            # Globales - Constantes
            [30000, 39999],
            [40000, 49999],
            [50000, 59999],
            [60000, 69999],
            # Local - Variables
            [5000, 5999], # Enteros
            [6000, 6999], # Decimales
            [7000, 7999], # Logicos
            [8000, 8999], # Letras
            # Local - Temporales
            [18000, 19999],
            [20000, 21999],
            [22000, 23999],
            [24000, 25999]
        ]

    def create_virtual_dir(self, scope, type, dataType, size):
        my_scope = 'local'
        if scope == 'Programa':
            my_scope = 'global'
        index = self.switch_cases(my_scope, type, dataType)
        result = self.tabla_direcciones[index][0]
        self.test_offset()
        self.tabla_direcciones[index][0] += size
        return result
    def switch_cases(self, scope, type, dataType):
        switch = {
            ('global', 'vars', 'entero'): 0,
            ('global', 'vars', 'decimal'): 1,
            ('global', 'vars', 'logico'): 2,
            ('global', 'vars', 'letra'): 3,
            ('global', 'temp', 'entero'): 4,
            ('global', 'temp', 'decimal'): 5,
            ('global', 'temp', 'logico'): 6,
            ('global', 'temp', 'letra'): 7,
            ('global', 'const', 'entero'): 8,
            ('global', 'const', 'decimal'): 9,
            ('global', 'const', 'logico'): 10,
            ('global', 'const', 'letra'): 11,
            ('local', 'vars', 'entero'): 12,
            ('local', 'vars', 'decimal'): 13,
            ('local', 'vars', 'logico'): 14,
            ('local', 'vars', 'letra'): 15,
            ('local', 'temp', 'entero'): 16,
            ('local', 'temp', 'decimal'): 17,
            ('local', 'temp', 'logico'): 18,
            ('local', 'temp', 'letra'): 19,
        }

        result = switch.get((scope, type, dataType), -1)
        return result

    def test_offset(self):
        for list in self.tabla_direcciones:
            if list[0] == list[1]:
                raise Exception("ERROR: Stack Overflow")
