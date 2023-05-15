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
        virtual_address = self.direcciones_virtuales.create_virtual_dir(scope, 'vars', type)
        mapped_type = self.mapa_datos.map_type(type)
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
            virtual_address = self.direcciones_virtuales.create_virtual_dir('Programa', 'const', type)
            self.directorio['Programa']['constantes'][id] = {
                'type': mapped_type,
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

        # del(self.directorio[scope]['variables'])

