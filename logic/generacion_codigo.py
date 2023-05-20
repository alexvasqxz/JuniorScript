from collections import deque as Stack
from logic.direcciones_virtuales import DireccionesVirtuales
from logic.data_mapping import MapeoDatos
from logic.cubo_semantico import CuboSemantico
class CodigoExpresionesEstatutos:
    def __init__(self):
        # Pila de Duplas, el primer elemento contendra el Operando
        # mientras que el segundo elemento contendra el tipo del Operando
        self.pilaOperandos = Stack()
        # Pila de un solo elemento conteniendo los Operadores
        self.pilaOperadores = Stack()
        # Pila de saltos para estatutos condiconales
        self.pilaSaltos = Stack()

        self.direccionesVirtuales = DireccionesVirtuales()
        self.mapeoDatos = MapeoDatos()
        self.cuboSemantico = CuboSemantico()

        # Conteo temporales
        self.temp_count = 1

    def push_operando(self, address):
        type = self.direccionesVirtuales.get_type_with_address(address)
        self.pilaOperandos.append((address, type))

    def push_operador(self, id):
        mapped_type = self.mapeoDatos.map_type(id)
        self.pilaOperadores.append(mapped_type)

    def push_salto(self, count):
        self.pilaSaltos.append(count)

    # ------------------------------------------------------------
    # CODIGO - QUADRUPLOS EXPRESIONES Y ESTATUTOS
    # ------------------------------------------------------------
    def create_expression_quad(self, depth_level, scope, quadObj, semanticaObj):
        if (not bool(self.pilaOperadores)):
            return

        if depth_level == 1:
            operators_list = [21, 22]
        elif depth_level == 2:
            operators_list = [11, 12, 13, 14, 15, 16]
        elif depth_level == 3:
            operators_list = [17, 18]
        elif depth_level == 4:
            operators_list = [19, 20]

        if self.pilaOperadores[-1] in operators_list:
            right = self.pilaOperandos.pop()
            right_address = right[0]
            right_type = right[1]
            left = self.pilaOperandos.pop()
            left_address = left[0]
            left_type = left[1]
            operador = self.pilaOperadores.pop()
            result_type = self.cuboSemantico.get_cube_type(left_type, right_type, operador)
            if result_type != -1:
                temp_address = semanticaObj.add_temp(scope, result_type, self.temp_count)
                self.temp_count += 1
                quadObj.agregar(operador, left_address, right_address, temp_address)
                self.pilaOperandos.append((temp_address, result_type, 'temp'))
            else:
                raise Exception(f"ERROR: Tipos Incompatibles '{left_type, right_type}'")
    def create_estatuto_quad(self, quadObj):
        if (not bool(self.pilaOperandos)):
            return

        operador = self.pilaOperadores.pop()
        if operador == 10:
            value_to_assign = self.pilaOperandos.pop()
            asignee = self.pilaOperandos.pop()
            quadObj.agregar(operador, value_to_assign[0], None, asignee[0])
        else :
            top_operand = self.pilaOperandos.pop()
            op_to_print = top_operand[0]
            quadObj.agregar(operador, None, None, op_to_print)

    def agregar_fondo(self):
        self.pilaOperadores.append('(')

    def quitar_fondo(self):
        if self.pilaOperadores[-1] == '(':
            self.pilaOperadores.pop()
        else:
            raise Exception(f"ERROR: El fondo falso ha fallado")

    # ------------------------------------------------------------
    # CODIGO - ESTATUTOS CONDICIONALES -- IF
    # ------------------------------------------------------------
    def estatuto_if(self, quadObj):
        expresion = self.pilaOperandos.pop()
        if expresion[1] != 3:
            raise Exception(f"ERROR: Tipo Incompatible '{expresion[0], expresion[1]}'")
        else:
            result = expresion[0]
            operador = self.pilaOperadores.pop()
            quadObj.agregar(operador, result, None, None)
            self.push_salto(quadObj.quads_len() - 1)

    def estatuto_if_else(self, quadObj):
        operador = self.pilaOperadores.pop()
        quadObj.agregar(operador, None, None, None)
        if_a_modificar = self.pilaSaltos.pop()
        self.push_salto(quadObj.quads_len() - 1)
        quadObj.modificar_quad(if_a_modificar, [None, None, None, quadObj.quads_len()])

    def estatuto_if_end(self, quadObj):
        end = self.pilaSaltos.pop()
        quadObj.modificar_quad(end, [None, None, None, quadObj.quads_len()])

    # ------------------------------------------------------------
    # CODIGO - ESTATUTOS CONDICIONALES -- WHILE
    # ------------------------------------------------------------
    def estatuto_while(self, quadObj):
        expresion = self.pilaOperandos.pop()
        if expresion[1] != 3:
            raise Exception(f"ERROR: Tipo Incompatible '{expresion[0], expresion[1]}'")
        else:
            result = expresion[0]
            operador = self.pilaOperadores.pop()
            quadObj.agregar(operador, result, None, None)
            self.push_salto(quadObj.quads_len() - 1)

    def estatuto_while_end(self, quadObj):
        while_a_modificar = self.pilaSaltos.pop()
        inicio = self.pilaSaltos.pop()
        operador = self.pilaOperadores.pop()
        quadObj.agregar(operador, None, None, inicio)
        quadObj.modificar_quad(while_a_modificar, [None, None, None, quadObj.quads_len()])

    def debug(self):
        print("Pila Operadores")
        for item in self.pilaOperadores:
            print(item)
        print("Pila Operandos")
        for item in self.pilaOperandos:
            print(item)
        print("Pila Saltos")
        for item in self.pilaSaltos:
            print(item)
