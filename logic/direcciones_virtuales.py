class DireccionesVirtuales():
    def __init__(self):
        self.tabla_direcciones = [
            # Globales - Variables
            [1000, 1999],  # Enteros
            [2000, 2999],  # Decimales
            [3000, 3999],  # Logicos
            [4000, 4999],  # Letras
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
            [5000, 5999],  # Enteros
            [6000, 6999],  # Decimales
            [7000, 7999],  # Logicos
            [8000, 8999],  # Letras
            # Local - Temporales
            [18000, 19999],
            [20000, 21999],
            [22000, 23999],
            [24000, 25999],
            [26000, 27999] # Pointers
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
            ('global', 'vars', 1): 0,
            ('global', 'vars', 2): 1,
            ('global', 'vars', 3): 2,
            ('global', 'vars', 4): 3,
            ('global', 'temp', 1): 4,
            ('global', 'temp', 2): 5,
            ('global', 'temp', 3): 6,
            ('global', 'temp', 4): 7,
            ('global', 'const', 1): 8,
            ('global', 'const', 2): 9,
            ('global', 'const', 3): 10,
            ('global', 'const', 4): 11,
            ('local', 'vars', 1): 12,
            ('local', 'vars', 2): 13,
            ('local', 'vars', 3): 14,
            ('local', 'vars', 4): 15,
            ('local', 'temp', 1): 16,
            ('local', 'temp', 2): 17,
            ('local', 'temp', 3): 18,
            ('local', 'temp', 4): 19,
            ('local', 'temp', 5): 20,
        }

        result = switch.get((scope, type, dataType), -1)
        return result

    def test_offset(self):
        for list in self.tabla_direcciones:
            if list[0] == list[1]:
                raise Exception("ERROR: Stack Overflow")

    def delete_function_space(self):
        vars_bottom = 5000
        temp_bottom = 18000
        for num in range(12, 21):
            if num in range(12, 16):
                self.tabla_direcciones[num][0] = vars_bottom
                vars_bottom += 1000
            else:
                self.tabla_direcciones[num][0] = temp_bottom
                temp_bottom += 2000

    def get_type_with_address(self, address):
        if ((address in range(1000, 2000)) or (address in range(5000, 6000))
                or (address in range(10000, 12000)) or (address in range(18000, 20000))
                or (address in range(30000, 40000))):
                    return 1
        elif ((address in range(2000, 3000)) or (address in range(6000, 7000))
                or (address in range(12000, 14000)) or (address in range(20000, 22000))
                or (address in range(40000, 50000))):
                    return 2
        elif ((address in range(3000, 4000)) or (address in range(7000, 8000))
                or (address in range(14000, 16000)) or (address in range(22000, 24000))
                or (address in range(50000, 60000))):
                    return 3
        elif ((address in range(4000, 5000)) or (address in range(8000, 9000))
                or (address in range(16000, 18000)) or (address in range(24000, 26000))
                or (address in range(60000, 70000))):
                    return 4
        elif (address in range(26000, 28000)):
            return 5
        else:
            raise Exception("ERROR: Tipo no existe para direccion '{address}'")

    def get_scope_with_address(self, address):
        if ((address in range(1000, 5000)) or (address in range(10000, 18000)) or (address in range(30000, 70000))):
            return 'global'
        elif ((address in range(5000, 9000)) or (address in range(18000, 28000))):
            return 'local'
        else:
            raise Exception("ERROR: Scope no existe para direccion '{address}'")