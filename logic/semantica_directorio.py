from collections import Counter
from logic.direcciones_virtuales import DireccionesVirtuales
from logic.data_mapping import MapeoDatos

class DirectorioFunciones:
    def __init__(self):
        self.direcciones_virtuales = DireccionesVirtuales()
        self.mapa_datos = MapeoDatos()
        self.directorio = {
            'Programa': {
                'id': None,
                'type': 0,
                'quad_init': 0,
                'resources': [],
                'variables': {},
                'constantes': {},
            }
        }

        self.function_names = set()
        self.global_variables = set()

    def create_vars_dict(self, scope):
        if not ('variables' in self.directorio[scope] and isinstance(self.directorio[scope]['variables'], dict)):
            self.directorio[scope]['variables'] = {}

    def get_vars_dict(self, scope):
        if ('variables' in self.directorio[scope] and isinstance(self.directorio[scope]['variables'], dict)):
            return self.directorio[scope]['variables']
        else:
            raise Exception(f"ERROR: '{id}' el directorio de variables no existe en este scope")

    def add_variable(self, scope, id, type, size, isArray, dim):
        vars_table = self.get_vars_dict(scope)
        if scope == 'Programa':
            self.global_variables.add(id)
        if id in vars_table:
            raise Exception(f"ERROR: '{id}' este nombre ya existe para una variable")
        mapped_type = self.mapa_datos.map_type(type)
        virtual_address = self.assign_virtual_address(scope, 'vars', mapped_type, size)
        # Variables Regulares
        if not isArray:
            vars_table[id] = {'dataType': mapped_type, 'address': virtual_address, 'size': size}
        # Arreglos y Matrices
        else:
            vars_table[id] = {'dataType': mapped_type, 'address': virtual_address, 'size': size, 'dimensions': dim}

    def get_variable(self, scope, id):
        if (id in self.directorio[scope]['variables'] and isinstance(self.directorio[scope]['variables'][id], dict)):
            return self.directorio[scope]['variables'][id]
        else:
            raise Exception(f"ERROR: '{id}' la variable no existe en este scope")

    def add_funcion(self, scope):
        if scope in self.directorio:
            raise Exception(f"ERROR: '{id}' este nombre ya existe para una funcion")
        self.directorio[scope] = {
            'id': None,
            'type': None,
            'quad_init': None,
            'resources': {
                'vars': [],
                'temps': []
            },
            'param_types' : [],
        }

    def update_table(self, scope, key, value):
        if key == 'id':
            if value in self.function_names:
                raise Exception(f"ERROR: '{id}' este nombre ya existe para una funcion")
            self.function_names.add(value)
        elif key == 'type':
            value = self.mapa_datos.map_type(value)
        self.directorio[scope][key] = value

    def add_param_type(self, scope, type):
        mapped_type = self.mapa_datos.map_type(type)
        self.directorio[scope]['param_types'].append(mapped_type)

    def add_constant(self, value):
        id = str(value)
        if not (id in self.directorio['Programa']['constantes']):
            type = self.get_constant_type(value)
            mapped_type = self.mapa_datos.map_type(type)
            virtual_address = self.assign_virtual_address('Programa', 'const', mapped_type, 1)
            self.directorio['Programa']['constantes'][id] = {
                'dataType': mapped_type,
                'value': value,
                'address': virtual_address
            }

    def get_constant_type(self, value):
        if (isinstance(value, float)):
            return 'decimal'
        elif (isinstance(value, int)):
            return 'entero'
        elif (value == 'verdadero' or value == 'falso'):
            return 'logico'
        else:
            return 'letra'

    def add_inicio(self):
        self.directorio['main'] = {
            'id': 'main_inicio',
            'type': 0,
            'quad_init': None,
            'resources': {
                'vars': [],
                'temps': []
            }
        }

    def assign_resources_vars(self, scope):
        # Variables
        if 'variables' in self.directorio[scope]:
            vars = self.get_vars_dict(scope)
            resources_aux = [0, 0, 0, 0]
            for value in vars.values():
                if value['dataType'] == 1:
                    resources_aux[0] += value['size']
                elif value['dataType'] == 2:
                    resources_aux[1] += value['size']
                elif value['dataType'] == 3:
                    resources_aux[2] += value['size']
                elif value['dataType'] == 4:
                    resources_aux[3] += value['size']
            self.directorio[scope]['resources']['vars'] = resources_aux
            # del (self.directorio[scope]['variables'])

    def assign_resources_temps(self, scope):
        # Temps
        if 'temps' in self.directorio[scope]:
            temp_types = [dir_temps.get('dataType') for dir_temps in self.directorio[scope]['temps'].values()]
            recursos = Counter(temp_types)
            lista_recursos = [recursos[1], recursos[2], recursos[3], recursos[4], recursos[5]]
            self.directorio[scope]['resources']['temps'] = lista_recursos
            self.direcciones_virtuales.delete_function_space()
            # del (self.directorio[scope]['temps'])

    def clear_functions(self, scope):
        global_vars = [glob_vars.get('dataType') for glob_vars in self.directorio[scope]['variables'].values()]
        global_const = [glob_cons.get('dataType') for glob_cons in self.directorio[scope]['constantes'].values()]
        global_recursos = Counter(global_vars + global_const)
        lista_recursos = [global_recursos[1], global_recursos[2], global_recursos[3], global_recursos[4]]
        self.directorio[scope]['resources'] = lista_recursos
        # Se borran las tablas de variables y constantes estando ya contabilizadas
        # del(self.directorio[scope]['variables'])
        # del (self.directorio[scope]['constantes'])
        # Se borran las tablas de funciones
        return self.directorio

    def assign_virtual_address(self, scope, type, dataType, size):
        return self.direcciones_virtuales.create_virtual_dir(scope, type, dataType, size)

    def get_vars_address(self, scope, id):
        id_str = str(id)
        # Tipo Constante
        if id_str in self.directorio['Programa']['constantes']:
            return self.directorio['Programa']['constantes'][id_str]['address']
        # Tipo Variable
        # Buscar dentro de la misma funcion
        if 'variables' in self.directorio[scope] and isinstance(self.directorio[scope]['variables'], dict):
            if id in self.directorio[scope]['variables']:
                return self.directorio[scope]['variables'][id]['address']
            # Buscar en variables globales
            elif id in self.global_variables:
                return self.directorio['Programa']['variables'][id]['address']
            else:
                raise Exception(f"ERROR: '{id}' no existe")
        else:
            raise Exception(f"ERROR: '{id}' no existe")

    def get_temp_address(self, scope, id):
        id_str = 't' + str(id)
        # Buscar dentro de la misma funcion
        if 'temps' in self.directorio[scope] and isinstance(self.directorio[scope]['temps'], dict):
            if id_str in self.directorio[scope]['temps']:
                return self.directorio[scope]['temps'][id_str]['address']
        else:
            raise Exception(f"ERROR: '{id_str}' no existe")


    def create_temp_dict(self, scope):
        if not ('temps' in self.directorio[scope] and isinstance(self.directorio[scope]['temps'], dict)):
            self.directorio[scope]['temps'] = {}

    def get_temp_dict(self, scope):
        if ('temps' in self.directorio[scope] and isinstance(self.directorio[scope]['temps'], dict)):
            return self.directorio[scope]['temps']
        else:
            raise Exception(f"ERROR: '{scope}' el directorio de temporales no existe en este scope")

    def add_temp(self, scope, type, count):
        self.create_temp_dict(scope)
        temp_table = self.get_temp_dict(scope)
        virtual_address = self.assign_virtual_address(scope, 'temp', type, 1)
        temp_table["t" + str(count)] = {'dataType': type, 'address': virtual_address, 'size': 1}
        return virtual_address

    def find_var_by_address(self, scope, address):
        # Local
        vars_dict = self.get_vars_dict(scope)
        for key, values in vars_dict.items():
            if values['address'] == address:
                if 'dimensions' in vars_dict[key]:
                    return vars_dict[key]['dimensions']
                else:
                    raise Exception(f"ERROR: Este id no es de tipo arreglo '{key}'")
        # Global
        global_vars_dict = self.directorio['Programa']['variables']
        for var_global in self.global_variables:
            if address == global_vars_dict[var_global]['address']:
                if 'dimensions' in  global_vars_dict[var_global]:
                    return global_vars_dict[var_global]['dimensions']
                else:
                    raise Exception(f"ERROR: Este id no es de tipo arreglo '{var_global}'")
