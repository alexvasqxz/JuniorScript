import copy
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
        self.local_stack = MemoryStack(directorio_funciones['main'])
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
                instruction_pointer += 1
            elif operador in range(11,23):
                self.expresiones_aritmeticas_helper(operador, left_operand, right_operand, quad_result)
                instruction_pointer += 1
            elif operador == 30:
                self.imprimir(quad_result)
                instruction_pointer += 1
            elif operador == 31:
                self.leer(quad_result)
                instruction_pointer += 1
            elif operador == 40:
                instruction_pointer = quad_result
            elif operador == 41:
                if self.get_value_helper(left_operand):
                    instruction_pointer = quad_result
                else:
                    instruction_pointer += 1
            elif operador == 42:
                if not self.get_value_helper(left_operand):
                    instruction_pointer = quad_result
                else:
                    instruction_pointer += 1
            elif operador == 50:
                instruction_pointer = self.salto_modulo(quad_result, instruction_pointer)
            elif operador == 51:
                self.alocar_recursos(quad_result)
                instruction_pointer += 1
            elif operador == 52:
                self.parametrizar(left_operand)
                instruction_pointer += 1
            elif operador == 53:
                self.regresar_algo(left_operand, quad_result)
                instruction_pointer = self.terminate_func()
            elif operador == 60:
                # Terminar funcion actual
                instruction_pointer = self.terminate_func()
            elif operador == 90 or operador == 91:
                self.verificar_limites(operador, left_operand, right_operand)
                instruction_pointer += 1
            else:
                instruction_pointer += 1

    def terminate_func(self):
        if bool(self.pila_stacks):
            self.local_stack = self.pila_stacks.pop()
            return self.pila_hans_gretel.pop()

    def asignar(self, left, quad_result):
        left_value = self.get_value_helper(left)
        if self.direcciones_virtuales.get_type_with_address(quad_result) != 5:
            self.set_value_helper(quad_result, left_value)
        # Pointer
        else:
            quad_result = self.get_value_helper(quad_result)
            self.set_value_helper(quad_result, left_value)

    def imprimir(self, result):
        if self.direcciones_virtuales.get_type_with_address(result) != 5:
            print(self.get_value_helper(result))
        # Pointer
        else:
            address_value = self.get_value_helper(result)
            print(self.get_value_helper(address_value))

    def leer(self, result):
        type = self.direcciones_virtuales.get_type_with_address(result)
        value = ''
        try:
            if type == 1:
                value = int(input("Ingresa el valor entero variable a leer: "))
            elif type == 2:
                value = float(input("Ingresa el valor decimal variable a leer: "))
            elif type == 3:
                value = input("Ingresa el valor para la variable a leer: ")
                if value == 'verdadero':
                    value = True
                elif value == 'falso':
                    value = False
                else:
                    raise Exception("ERROR: Para logicos solamente se puede ingresar 'verdadero' o 'falso'")
            elif type == 4:
                value = input("Ingresa el valor para la variable letra: ")
            self.set_value_helper(result, value)
        except:
            raise Exception("ERROR: Valor ingresado no es valido")

    def expresiones_aritmeticas_helper(self, operador, left, right, quad_result):
        # El lado Izquierdo es un pointer
        if self.direcciones_virtuales.get_type_with_address(left) == 5:
            left = self.get_value_helper(left)
        # El lado Derecho es un pointer
        if self.direcciones_virtuales.get_type_with_address(right) == 5:
            right = self.get_value_helper(right)
        left_value = self.get_value_helper(left)
        right_value = self.get_value_helper(right)
        result = None
        if operador == 11:
            result = left_value < right_value
        elif operador == 12:
            result = left_value > right_value
        elif operador == 13:
            result = left_value <= right_value
        elif operador == 14:
            result = left_value >= right_value
        elif operador == 15:
            result = left_value == right_value
        elif operador == 16:
            result = left_value != right_value
        elif operador == 17:
            result = left_value + right_value
        elif operador == 18:
            result = left_value - right_value
        elif operador == 19:
            result = left_value * right_value
        elif operador == 20:
            result = left_value / right_value
        elif operador == 21:
            result = left_value and right_value
        elif operador == 22:
            result = left_value or right_value
        self.set_value_helper(quad_result, result)

    def verificar_limites(self, limite, left, right):
        value_evaluar = self.get_value_helper(left)
        value_limite = self.get_value_helper(right)
        if limite == 90:
            if value_evaluar < value_limite:
                raise Exception(f"ERROR: Indice fuera de rango")
        elif limite == 91:
            if value_evaluar > value_limite:
                raise Exception(f"ERROR: Indice fuera de rango")

    def alocar_recursos(self, funcion):
        # Guardar stack anterior en su estado
        self.stack_anterior = self.local_stack
        if len(self.pila_stacks) < 50:
            self.pila_stacks.append(self.stack_anterior)
        else:
            raise Exception(f"ERROR: Overflow: Demasiadas funciones declaradas")
        # Asignar el stack actual a contener los recursos de la nueva funcion
        self.local_stack = MemoryStack(self.directorio_funciones[funcion])

    def parametrizar(self, parametro):
        type = self.direcciones_virtuales.get_type_with_address(parametro)
        valor_parametro = self.get_value_helper(parametro)
        inicio_parametros = self.local_stack.inicio_parametros
        if type == 1:
            self.set_value_helper(inicio_parametros[0], valor_parametro)
            inicio_parametros[0] += 1
        elif type == 2:
            self.set_value_helper(inicio_parametros[1], valor_parametro)
            inicio_parametros[1] += 1
        elif type == 3:
            self.set_value_helper(inicio_parametros[2], valor_parametro)
            inicio_parametros[2] += 1
        elif type == 4:
            self.set_value_helper(inicio_parametros[3], valor_parametro)
            inicio_parametros[3] += 1

    def salto_modulo(self, new_pointer, ip):
        # Guardar Migaja de Pan
        self.pila_hans_gretel.append(ip + 1)
        # Reiniciar stack previo
        self.stack_anterior = None
        return new_pointer

    def regresar_algo(self, value, global_address):
        left_value = self.get_value_helper(value)
        if self.direcciones_virtuales.get_type_with_address(value) != 5:
            self.set_value_helper(global_address, left_value)
        # Pointer
        else:
            left_value = self.get_value_helper(left_value)
            self.set_value_helper(global_address, left_value)

    def get_value_helper(self, address):
        scope = self.direcciones_virtuales.get_scope_with_address(address)
        if scope == 'local':
            value = self.local_stack.get_value(address)
        elif scope == 'global':
            value = self.data_segment.get_value(address)
        if value == -1 and self.stack_anterior is not None:
            value = self.stack_anterior.get_value(address)
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
        print(self.quadruples)
        self.leer_instrucciones()
        print('------DATA SEGMENT--------')
        print("Enteros: ", self.data_segment.segmento_entero)
        print("Decimales: ", self.data_segment.segmento_decimal)
        print("Logicos: ", self.data_segment.segmento_logico)
        print("Letreros: ", self.data_segment.segmento_letra)
        print('------MEMORY STACK--------')
        print("Enteros: ", self.local_stack.segmento_entero)
        print("Decimales: ", self.local_stack.segmento_decimal)
        print("Logicos: ", self.local_stack.segmento_logico)
        print("Letreros: ", self.local_stack.segmento_letra)

