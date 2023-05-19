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
                'resources': {
                    'vars': [],
                    'temps': []
                },
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

    def add_variable(self, scope, id, type, size):
        vars_table = self.get_vars_dict(scope)
        if scope == 'Programa':
            self.global_variables.add(id)
        if id in vars_table:
            raise Exception(f"ERROR: '{id}' este nombre ya existe para una variable")
        mapped_type = self.mapa_datos.map_type(type)
        virtual_address = self.assign_virtual_address(scope, 'vars', mapped_type, size)
        vars_table[id] = {'dataType': mapped_type, 'address': virtual_address, 'size': size}

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

    def assign_resources(self, scope):
        vars_types = [dir_vars.get('dataType') for dir_vars in self.directorio[scope]['variables'].values()]
        recursos = Counter(vars_types)
        lista_recursos = [recursos[1], recursos[2], recursos[3], recursos[4]]
        self.directorio[scope]['resources']['vars'] = lista_recursos
        self.direcciones_virtuales.delete_function_space()
        # del (self.directorio[scope]['variables'])

    def clear_functions(self, scope):
        global_vars = [glob_vars.get('dataType') for glob_vars in self.directorio[scope]['variables'].values()]
        global_const = [glob_cons.get('dataType') for glob_cons in self.directorio[scope]['constantes'].values()]
        global_recursos = Counter(global_vars + global_const)
        lista_recursos = [global_recursos[1], global_recursos[2], global_recursos[3], global_recursos[4]]
        self.directorio[scope]['resources']['vars'] = lista_recursos
        # Se borran las tablas de variables y constantes estando ya contabilizadas
        # del(self.directorio[scope]['variables'])
        # del (self.directorio[scope]['constantes'])
        # Se borran las tablas de funciones
        return self.directorio
        #[scope]

    def assign_virtual_address(self, scope, type, dataType, size):
        return self.direcciones_virtuales.create_virtual_dir(scope, type, dataType, size)

    def get_vars_address(self, scope, id):
        if id in self.directorio[scope]['variables']:
            return self.directorio[scope]['variables'][id]['address']
        elif id in self.directorio['Programa']['variables']:
            return self.directorio['Programa']['variables'][id]['address']
        elif str(id) in self.directorio['Programa']['constantes']:
            return self.directorio['Programa']['constantes'][str(id)]['address']
        else:
            raise Exception(f"ERROR: '{id}' no existe")

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
