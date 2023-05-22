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
        # Pila de dimensiones para arreglos
        self.pilaDim = Stack()

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
            assignee = self.pilaOperandos.pop()
            if self.cuboSemantico.get_cube_type(value_to_assign[1], assignee[1], operador) != -1:
                quadObj.agregar(operador, value_to_assign[0], None, assignee[0])
            else:
                raise Exception(f"ERROR: Tipos Incompatibles '{value_to_assign[1], assignee[1]}'")
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

    # ------------------------------------------------------------
    # CODIGO - ESTATUTOS CONDICIONALES -- FOR
    # ------------------------------------------------------------
    def estatuto_for(self, scope, quadObj, semanticaObj):
        if (not bool(self.pilaOperandos)):
            return

        operador = self.pilaOperadores.pop()
        expression_result = self.pilaOperandos.pop()
        if (expression_result[1] != 1):
            raise Exception(f"ERROR: El resultado de la expresion debe ser de tipo numerico")
        else:
            # Generar temporal VC
            vc_address = semanticaObj.add_temp(scope, 1, 'VC')
            self.temp_count += 1
            id_for = self.pilaOperandos.pop()
            if self.cuboSemantico.get_cube_type(id_for[1], expression_result[1], operador) != -1:
                quadObj.agregar(operador, expression_result[0], None, id_for[0])
                quadObj.agregar(operador, id_for[0], None, vc_address)
                # Reingresar el id original para usar en el ultimo paso
                self.pilaOperandos.append(id_for)
            else:                                                                                   
                raise Exception(f"ERROR: Tipos Incompatibles '{id_for[1], expression_result[1]}'")

    def estatuto_for_middle(self, scope, quadObj, semanticaObj):
        if (not bool(self.pilaOperandos)):
            return

        expression_result = self.pilaOperandos.pop()
        if (expression_result[1] != 1):
            raise Exception(f"ERROR: El resultado de la expresion debe ser de tipo numerico")
        else:
            # Generar temporal VF
            vf_address = semanticaObj.add_temp(scope, 1, 'VF')
            self.temp_count += 1
            as_op = self.pilaOperadores.pop()
            lt_op = self.pilaOperadores.pop()
            # Generar (=, Exp, , VF)
            quadObj.agregar(as_op, expression_result[0], None, vf_address)
            # Generar (<, VC, VF, Tx)
            temp_address = semanticaObj.add_temp(scope, 1, self.temp_count)
            self.temp_count += 1
            # Obtener VC desde el directorio
            vc_address = semanticaObj.get_temp_address(scope, 'VC')
            quadObj.agregar(lt_op, vc_address, vf_address, temp_address)
            self.pilaOperandos.append((temp_address, 1, 'temp'))
            self.push_salto(quadObj.quads_len() - 1)
            # Generar (SALTOF, Tx)
            operador = self.pilaOperadores.pop()
            result = self.pilaOperandos.pop()
            quadObj.agregar(operador, result[0], None, None)
            self.push_salto(quadObj.quads_len() - 1)

    def estatuto_for_end(self, scope, quadObj, semanticaObj):
        # Generar (+, VControl, 1, Ty)
        sum_op = self.pilaOperadores.pop()
        # VControl
        vc_address = semanticaObj.get_temp_address(scope, 'VC')
        # + 1
        semanticaObj.add_constant(1)
        one_address = semanticaObj.get_vars_address(scope, 1)
        # Ty
        temp_address = semanticaObj.add_temp(scope, 1, self.temp_count)
        self.temp_count += 1
        # Generar Quadruplo
        quadObj.agregar(sum_op, vc_address, one_address, temp_address)

        # Generar (=, Ty, , VControl)
        as_op = self.pilaOperadores.pop()
        quadObj.agregar(as_op, temp_address, None, vc_address)

        # Generar (=, Ty, , IdOriginal)
        id_original = self.pilaOperandos.pop()
        quadObj.agregar(as_op, temp_address, None, id_original[0])

        # SALTO y rellenar quadruplo
        quad_to_modify = self.pilaSaltos.pop()
        linea_retorno = self.pilaSaltos.pop()
        operador = self.pilaOperadores.pop()
        # Generar SALTO linea_retorno
        quadObj.agregar(operador, None, None, linea_retorno)
        # Rellenar Quadruplo [quad_to_modify]
        quadObj.modificar_quad(quad_to_modify, [None, None, None, quadObj.quads_len()])

    # ------------------------------------------------------------
    # CODIGO - ARREGLOS
    # ------------------------------------------------------------
    def arr_start(self, scope, semanticaObj):
        dims = self.obtener_dimensiones(scope, semanticaObj)
        id = self.pilaOperandos.pop()
        self.pilaDim.append((id[0], dims, id[1]))

    def obtener_dimensiones(self, scope, semanticaObj):
        arr_id = self.pilaOperandos[-1]
        # Verifica que el id tenga dimension y obtiene dimensiones
        dimensiones = semanticaObj.find_var_by_address(scope, arr_id[0])
        return dimensiones

    def arr_validar_limites(self, scope, quadObj, semanticaObj, plano):
        # Obtener limite inferior (0)
        semanticaObj.add_constant(0)
        zero_address = semanticaObj.get_vars_address(scope, 0)
        # Generar quad limite inferior
        expression_result = self.pilaOperandos[-1]
        expression_type = expression_result[1]
        if expression_type != 1:
            raise Exception(f"ERROR: El indice de arreglo debe dar como resultado un entero")
        op_inf = self.pilaOperadores.pop()
        quadObj.agregar(op_inf, expression_result[0], zero_address, None)
        # Obtener limite superior (dimensiones)
        # Primera Dimension
        if plano == 1:
            lim_sup = self.pilaDim[-1][1][0] - 1
        # Segunda Dimension
        elif plano == 2 and self.pilaDim:
            lim_sup = self.pilaDim[-1][1][1] - 1
        else:
            raise Exception(f"ERROR: El arreglo solo puede ser de una dimension")
        semanticaObj.add_constant(lim_sup)
        lim_address = semanticaObj.get_vars_address(scope, lim_sup)
        op_sup = self.pilaOperadores.pop()
        quadObj.agregar(op_sup, expression_result[0], lim_address, None)

    def arr_primera_dimension(self, scope, quadObj, semanticaObj):
        dir_dimensiones = self.pilaDim.pop()
        dir_virtual = dir_dimensiones[0]
        dimensiones = dir_dimensiones[1]
        tipo_arreglo = dir_dimensiones[2]

        res_expression = self.pilaOperandos.pop()
        # Para Arreglos se sumara a la direccion virtual del arreglo
        # el resultado de la expresion y guardara en un temporal (Tn)
        if len(dimensiones) == 1:
            self.push_operador('+')
            sum_op = self.pilaOperadores.pop()
            temp_address = semanticaObj.add_temp(scope, 1, self.temp_count)
            self.temp_count += 1
            quadObj.agregar(sum_op, res_expression[0], dir_virtual, temp_address)
            self.pilaOperandos.append((temp_address, tipo_arreglo, 'temp'))
        # Para Matrices se multiplicara el resultado de la expresion
        # por el numero de columnas y guardara en un temporal Tx
        elif len(dimensiones) == 2:
            columnas = dimensiones[1]
            semanticaObj.add_constant(columnas)
            col_address = semanticaObj.get_vars_address(scope, columnas)
            self.push_operador('*')
            operator = self.pilaOperadores.pop()
            temp_address = semanticaObj.add_temp(scope, tipo_arreglo, self.temp_count)
            self.temp_count += 1
            quadObj.agregar(operator, res_expression[0], col_address, temp_address)
            self.pilaOperandos.append((temp_address, tipo_arreglo, 'temp'))
            self.pilaDim.append((dir_virtual, dimensiones, tipo_arreglo))

    def arr_segunda_dimension(self, scope, quadObj, semanticaObj):
        dir_dimensiones = self.pilaDim.pop()
        dir_virtual = dir_dimensiones[0]
        tipo_arreglo = dir_dimensiones[2]
        res_expression = self.pilaOperandos.pop()
        res_1d = self.pilaOperandos.pop()

        # Generar Quadruplo (+, res_exp, res_1d, Tx)
        self.push_operador('+')
        operator = self.pilaOperadores.pop()
        temp_address = semanticaObj.add_temp(scope, tipo_arreglo, self.temp_count)
        self.temp_count += 1
        quadObj.agregar(operator, res_expression[0], res_1d[0], temp_address)
        # Generar Quadruplo (+, resultado_anterior, dir_virtual, (Tn)
        res_anterior = temp_address
        temp_address = semanticaObj.add_temp(scope, tipo_arreglo, self.temp_count)
        self.temp_count += 1
        quadObj.agregar(operator, res_anterior, dir_virtual, temp_address)
        self.pilaOperandos.append((temp_address, tipo_arreglo, 'temp'))

    def arr_end(self):
        # Si el stack de dimensiones no esta vacio es que algo salio mal
        if bool(self.pilaDim):
            raise Exception(f"ERROR: Asegurate de haber indexado bien la matriz")

    # ------------------------------------------------------------
    # CODIGO - MODULOS
    # ------------------------------------------------------------
    def reiniciar_temps(self):
        self.temp_count = 1

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
        print("Pila Dim")
        for item in self.pilaDim:
            print(item)
