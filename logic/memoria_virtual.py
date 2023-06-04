from logic.direcciones_virtuales import DireccionesVirtuales

# Variables Globales y Constantes
class DataSegment:
    def __init__(self, directorio):
        self.directorio = directorio
        self.segmento_entero = {}
        self.segmento_decimal = {}
        self.segmento_logico = {}
        self.segmento_letra = {}
        self.direcciones_virtuales = DireccionesVirtuales()

        self.alocar_constantes()
        self.alocar_variables()

    def alocar_constantes(self):
        if 'constantes' in self.directorio:
            for constante, info in self.directorio['constantes'].items():
                address = info['address']
                value = info['value']
                if info['dataType'] == 1:
                    self.segmento_entero[address] = value
                elif info['dataType'] == 2:
                    self.segmento_decimal[address] = value
                elif info['dataType'] == 3:
                    if value == 'verdadero':
                        self.segmento_logico[address] = True
                    else:
                        self.segmento_logico[address] = False
                elif info['dataType'] == 4:
                    self.segmento_letra[address] = value

    def alocar_variables(self):
        if 'variables' in self.directorio:
            for variable, info in self.directorio['variables'].items():
                address = info['address']
                size = info['size']
                if info['dataType'] == 1:
                    self.alocar_variables_helper(self.segmento_entero, address, size)
                elif info['dataType'] == 2:
                    self.alocar_variables_helper(self.segmento_decimal, address, size)
                elif info['dataType'] == 3:
                    self.alocar_variables_helper(self.segmento_logico, address, size)
                elif info['dataType'] == 4:
                    self.alocar_variables_helper(self.segmento_letra, address, size)

    def alocar_variables_helper(self, segmento, address, size):
        while (size > 0):
            segmento[address] = -1
            address += 1
            size -= 1

    def get_value(self, address):
        data_type = self.direcciones_virtuales.get_type_with_address(address)
        if data_type == 1:
            return self.segmento_entero.get(address, -1)
        elif data_type == 2:
            return self.segmento_decimal.get(address, -1)
        elif data_type == 3:
            return self.segmento_logico.get(address, -1)
        elif data_type == 4:
            return self.segmento_letra.get(address, -1)

    def set_value(self, address, value):
        data_type = self.direcciones_virtuales.get_type_with_address(address)
        if data_type == 1:
            self.segmento_entero[address] = value
        elif data_type == 2:
            self.segmento_decimal[address] = value
        elif data_type == 3:
            self.segmento_logico[address] = value
        elif data_type == 4:
            self.segmento_letra[address] = value

# Variables locales
class MemoryStack:
    def __init__(self, directorio):
        self.directorio = directorio
        self.segmento_entero = {}
        self.segmento_decimal = {}
        self.segmento_logico = {}
        self.segmento_letra = {}
        self.inicio_parametros = [5000, 6000, 7000, 8000]
        self.direcciones_virtuales = DireccionesVirtuales()

        self.alocar_variables()
        self.alocar_temporales()

    def alocar_variables(self):
        if 'variables' in self.directorio:
            for variable, info in self.directorio['variables'].items():
                address = info['address']
                size = info['size']
                if info['dataType'] == 1:
                    self.alocar_variables_helper(self.segmento_entero, address, size)
                elif info['dataType'] == 2:
                    self.alocar_variables_helper(self.segmento_decimal, address, size)
                elif info['dataType'] == 3:
                    self.alocar_variables_helper(self.segmento_logico, address, size)
                elif info['dataType'] == 4:
                    self.alocar_variables_helper(self.segmento_letra, address, size)

    def alocar_variables_helper(self, segmento, address, size):
        while (size > 0):
            segmento[address] = -1
            address += 1
            size -= 1

    def alocar_temporales(self):
        if 'temps' in self.directorio:
            for constante, info in self.directorio['temps'].items():
                address = info['address']
                if info['dataType'] == 1:
                    self.segmento_entero[address] = -1
                elif info['dataType'] == 2:
                    self.segmento_decimal[address] = -1
                elif info['dataType'] == 3:
                    self.segmento_logico[address] = -1
                elif info['dataType'] == 4:
                    self.segmento_letra[address] = -1
                elif info['dataType'] == 5:
                    self.segmento_entero[address] = -1

    def get_value(self, address):
        data_type = self.direcciones_virtuales.get_type_with_address(address)
        if data_type == 1:
            return self.segmento_entero.get(address, -1)
        elif data_type == 2:
            return self.segmento_decimal.get(address, -1)
        elif data_type == 3:
            return self.segmento_logico.get(address, -1)
        elif data_type == 4:
            return self.segmento_letra.get(address, -1)
        elif data_type == 5:
            return self.segmento_entero.get(address, -1)


    def set_value(self, address, value):
        data_type = self.direcciones_virtuales.get_type_with_address(address)
        if data_type == 1:
            self.segmento_entero[address] = value
        elif data_type == 2:
            self.segmento_decimal[address] = value
        elif data_type == 3:
            self.segmento_logico[address] = value
        elif data_type == 4:
            self.segmento_letra[address] = value
        elif data_type == 5:
            self.segmento_entero[address] = value