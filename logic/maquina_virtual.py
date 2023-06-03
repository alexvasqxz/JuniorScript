from collections import deque as Stack
from logic.memoria_virtual import DataSegment, MemoryStack
from logic.direcciones_virtuales import DireccionesVirtuales
class MaquinaVirtual:
    def __init__(self, quadruples, directorio_funciones):
        self.quadruples = quadruples
        self.directorio_funciones = directorio_funciones
        self.pila_stacks = Stack()
        self.stack_anterior = None
        self.pila_hans_gretel = Stack()
        # Crear Memoria Global (Data Segment)
        self.data_segment = DataSegment(directorio_funciones['Programa'])
        # Crear Memoria Local para Main (Stack)
        self.local_stack = MemoryStack(directorio_funciones['Funcion1'])
        self.direcciones_virtuales = DireccionesVirtuales()

    def leer_instrucciones(self):
        instruction_pointer = 0
        instrucciones_totales = len(self.quadruples)
        while (instruction_pointer < instrucciones_totales):
            current_quad = self.quadruples[instruction_pointer]
            operador = current_quad[0]
            left_operand = current_quad[1]
            right_operand = current_quad[2]
            quad_result = current_quad[3]

            if operador == 10:
                self.asignar(left_operand, quad_result)
            elif operador == 11:
                self.menor_a(left_operand, right_operand, quad_result)
            elif operador == 12:
                self.mayor_a(left_operand, right_operand, quad_result)
            elif operador == 13:
                self.menor_igual_a(left_operand, right_operand, quad_result)
            elif operador == 14:
                self.mayor_igual_a(left_operand, right_operand, quad_result)
            elif operador == 17:
                self.sumar(left_operand, right_operand, quad_result)
            elif operador == 18:
                self.restar(left_operand, right_operand, quad_result)
            elif operador == 19:
                self.multiplicar(left_operand, right_operand, quad_result)
            elif operador == 20:
                self.dividir(left_operand, right_operand, quad_result)
            elif operador == 21:
                self.logica_and(left_operand, right_operand, quad_result)
            elif operador == 22:
                self.logica_or(left_operand, right_operand, quad_result)
            elif operador == 30:
                self.imprimir(quad_result)

            instruction_pointer += 1

    def asignar(self, left, quad_result):
        left_value = self.get_value_helper(left)
        self.set_value_helper(quad_result, left_value)

    def menor_a(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value < right_value
        self.set_value_helper(quad_result, result)

    def mayor_a(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value > right_value
        self.set_value_helper(quad_result, result)

    def menor_igual_a(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value <= right_value
        self.set_value_helper(quad_result, result)

    def mayor_igual_a(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value >= right_value
        self.set_value_helper(quad_result, result)

    def sumar(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value + right_value
        self.set_value_helper(quad_result, result)

    def restar(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value - right_value
        self.set_value_helper(quad_result, result)

    def multiplicar(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value * right_value
        self.set_value_helper(quad_result, result)

    def dividir(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value / right_value
        self.set_value_helper(quad_result, result)

    def logica_and(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value & right_value
        self.set_value_helper(quad_result, result)

    def logica_or(self, left, right, quad_result):
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = left_value | right_value
        self.set_value_helper(quad_result, result)

    def imprimir(self, result):
        print(self.get_value_helper(result))

    def get_value_helper(self, address):
        scope = self.direcciones_virtuales.get_scope_with_address(address)
        if scope == 'local':
            value = self.local_stack.get_value(address)
        elif scope == 'global':
            value = self.data_segment.get_value(address)
        if value == -1:
            raise Exception(f"ERROR: Se debe asignar un valor a la variable con direccion {address}")
        return value

    def set_value_helper(self, result_address, value):
        scope = self.direcciones_virtuales.get_scope_with_address(result_address)
        if scope == 'local':
            self.local_stack.set_value(result_address, value)
        elif scope == 'global':
            self.data_segment.set_value(result_address, value)
    def ejecutar(self):
        self.leer_instrucciones()
        print('------DS--------')
        print(self.data_segment.segmento_entero)
        print('------MS--------')
        print(self.local_stack.segmento_entero)

