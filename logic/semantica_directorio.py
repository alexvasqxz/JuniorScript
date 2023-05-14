from collections import Counter

class DirectorioFunciones:
    def __init__(self):
        self.directorio = {
            'Programa': {
                'id': None,
                'type': 'vacio',
                'quad_init': 0,
                'resources': {
                    'vars': [],
                    'temps': []
                },
                'variables': {},
                'constantes': {}
            }
        }

        self.function_names = set()

    def create_vars_dict(self, scope):
        if not ('variables' in self.directorio[scope] and isinstance(self.directorio[scope]['variables'], dict)):
            self.directorio[scope]['variables'] = {}

    def get_vars_dict(self, scope):
        if ('variables' in self.directorio[scope] and isinstance(self.directorio[scope]['variables'], dict)):
            return self.directorio[scope]['variables']
        else:
            raise Exception(f"ERROR: '{id}' el directorio de variables no existe en este scope")

    def add_variable(self, scope, id, type, address, size):
        vars_table = self.get_vars_dict(scope)
        if id in vars_table:
            raise Exception(f"ERROR: '{id}' este nombre ya existe para una variable")
        vars_table[id] = {'dataType': type, 'address': address, 'size': size}

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
        self.directorio[scope][key] = value

    def add_param_type(self, scope, type):
        self.directorio[scope]['param_types'].append(type)

    def add_inicio(self):
        self.directorio['main'] = {
            'id': 'main_inicio',
            'type': 'vacio',
            'quad_init': None,
            'resources': {
                'vars': [],
                'temps': []
            }
        }

    def assign_resources(self, scope):
        vars_types = [dir_vars.get('dataType') for dir_vars in self.directorio[scope]['variables'].values()]
        recursos = Counter(vars_types)
        lista_recursos = [recursos['entero'], recursos['decimal'], recursos['logico'], recursos['letra']]
        self.directorio[scope]['resources']['vars'] = lista_recursos

        # del(self.directorio[scope]['variables'])

