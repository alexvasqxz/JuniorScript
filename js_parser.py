# ------------------------------------------------------------
# js_parser.py
#
# (Python Lex & Yacc)
# Analisis Sintaxico
#
# Gustavo Vasquez
# ------------------------------------------------------------

import ply.yacc as yacc
import json
from js_lexer import tokens

# Semantica
from logic.semantica_directorio import DirectorioFunciones

def JSParser():
    # ------------------------------------------------------------
    # Variables Globales
    # ------------------------------------------------------------
    count_funciones = 1

    # ------------------------------------------------------------
    # DIAGRAMAS DE SINTAXIS
    # ------------------------------------------------------------
    def p_programa(p):
        '''
        programa : PROGRAMA puntos_semantica_1 ID puntos_semantica_2 programaB programaC inicio
        programaB : dec_vars
                | empty
        programaC : dec_func programaCC
        programaCC : programaC
                | empty
        '''
        p[0] = None

    def p_dec_vars(p):
        '''
        dec_vars : VAR punto_semantico_3 dec_varsI COLON tipo \
        punto_semantico_5 dec_varsB punto_semantico_8 dec_varsBB
        dec_varsI : ID punto_semantico_4 dec_varsII
        dec_varsII : COMMA ID punto_semantico_4
                | empty
        dec_varsB : LBRACE CTEENT punto_semantico_6 RBRACE
                | LBRACE CTEENT punto_semantico_6 RBRACE LBRACE CTEENT punto_semantico_7 RBRACE
                | empty
        dec_varsBB : dec_vars
                | empty
        '''
        p[0] = None

    def p_tipo(p):
        '''
        tipo : TIPOENT
            | TIPODEC
            | TIPOLETRA
            | TIPOLOGI
        '''
        p[0] = p[1]

    def p_dec_func(p):
        '''
        dec_func : FUNCION punto_semantico_9 ID punto_semantico_10 LPAREN punto_semantico_3 \
        dec_funcB RPAREN COLON tipo_func punto_semantico_13 LCURLY bloque RCURLY punto_semantico_14
        dec_funcB : dec_params
                | empty
        '''
        p[0] = None

    def p_dec_params(p):
        '''
        dec_params : ID punto_semantico_11 COLON tipo punto_semantico_5 punto_semantico_12 dec_paramsB
        dec_paramsB : COMMA dec_params
                    | empty
        '''
        p[0] = None

    def p_tipo_func(p):
        '''
        tipo_func : tipo
                | VOID
        '''
        p[0] = p[1]

    def p_bloque(p):
        '''
        bloque : bloqueB bloqueBB
        bloqueB : asignacion
                | ciclo_para_cada
                | ciclo_mientras
                | condicion
                | escribir
                | leer
                | dec_vars
                | llam_func
                | regresar
        bloqueBB : bloqueB bloqueBB
                | empty
        '''
        p[0] = None

    def p_asignacion(p):
        '''
        asignacion : llam_vars ASSIGN expresion
        '''
        p[0] = None

    def p_llam_vars(p):
        '''
        llam_vars : ID llam_varsB
        llam_varsB : LBRACE CTEENT RBRACE
                | LBRACE CTEENT RBRACE LBRACE CTEENT RBRACE
                | empty
        '''
        p[0] = None

    def p_expresion(p):
        '''
        expresion : peta_exp expresionB
        expresionB : ASSIGN expresion
                | empty
        '''
        p[0] = None

    def p_peta_exp(p):
        '''
        peta_exp : tera_exp peta_expB
        peta_expB : AND peta_exp
                | OR peta_exp
                | empty
        '''
        p[0] = None

    def p_tera_exp(p):
        '''
        tera_exp : mega_exp tera_expB
        tera_expB : LT tera_exp
                | GT tera_exp
                | LTE tera_exp
                | GTE tera_exp
                | EQUAL tera_exp
                | NEQUAL tera_exp
                | empty
        '''
        p[0] = None

    def p_mega_exp(p):
        '''
        mega_exp : kilo_exp mega_expB
        mega_expB : PLUS mega_exp
                | MINUS mega_exp
                | empty
        '''
        p[0] = None

    def p_kilo_exp(p):
        '''
        kilo_exp : factor kilo_expB
        kilo_expB : TIMES kilo_exp
                | DIVIDE kilo_exp
                | empty
        '''
        p[0] = None

    def p_factor(p):
        '''
        factor : LPAREN expresion RPAREN
            | llam_vars
            | llam_func
            | CTEENT
            | CTEDECI
        '''
        p[0] = None

    def p_llam_func(p):
        '''
        llam_func : ID LPAREN llam_params RPAREN
        '''
        p[0] = None

    def p_llam_params(p):
        '''
        llam_params : expresion llam_paramsB
        llam_paramsB : COMMA llam_params
                    | empty
        '''
        p[0] = None

    def p_ciclo_para_cada(p):
        '''
        ciclo_para_cada : FOR LPAREN ID IN ID ciclo_para_cadaB RPAREN LCURLY bloque RCURLY
        ciclo_para_cadaB : CONFORME expresion
                        | empty
        '''
        p[0] = None

    def p_ciclo_mientras(p):
        '''
        ciclo_mientras : WHILE LPAREN expresion RPAREN LCURLY bloque RCURLY
        '''
        p[0] = None

    def p_condicion(p):
        '''
        condicion : IF LPAREN expresion RPAREN LCURLY bloque RCURLY condicionB
        condicionB : ELSE LCURLY bloque RCURLY
                | empty
        '''
        p[0] = None

    def p_escribir(p):
        '''
        escribir : ESCRITURA LPAREN escribirB RPAREN
        escribirB : expresion escribirBB
                | CTEFRASE escribirBB
        escribirBB : COMMA escribirB
                | empty
        '''
        p[0] = None

    def p_leer(p):
        '''
        leer : LECTURA LPAREN leerI RPAREN
        leerI : ID leerII
        leerII : COMMA ID
            | empty
        '''
        p[0] = None

    def p_regresar(p):
        '''
        regresar : RETURN LPAREN expresion RPAREN
        '''
        p[0] = None

    def p_inicio(p):
        '''
        inicio : MAIN puntos_semantica_15 LPAREN RPAREN LCURLY bloque RCURLY punto_semantico_14
        '''
        p[0] = None
        with open("./tests/dir_func_output.txt", "x") as output_file:
            output_file.write("Directorio de Funciones\n")
            output_file.write(json.dumps(dir_func, indent=4))

    def p_empty(p):
        '''
        empty :
        '''
        p[0] = None

    def p_error(p):
        if p == None:
            token = "end of file"
        else:
            token = f"{p.type}({p.value})"
        print(f"Error de sintaxis: Unexpected {token}")

    # ------------------------------------------------------------
    # SEMANTICA - PUNTOS NEURONALES
    # ------------------------------------------------------------
    def p_puntos_semantica_1(p):
        '''
        puntos_semantica_1 :
        '''
        global semantica, dir_func, count_funciones
        count_funciones = 1
        semantica = DirectorioFunciones()
        dir_func = semantica.directorio

    def p_puntos_semantica_2(p):
        '''
        puntos_semantica_2 :
        '''
        global curr_scope
        curr_scope = 'Programa'
        dir_func[curr_scope]['id'] = p[-1]

    def p_punto_semantico_3(p):
        '''
        punto_semantico_3 :
        '''
        global curr_ids
        semantica.create_vars_dict(curr_scope)
        curr_ids = []

    def p_punto_semantico_4(p):
        '''
        punto_semantico_4 :
        '''
        global curr_ids
        curr_ids.append(p[-1])

    def p_punto_semantico_5(p):
        '''
        punto_semantico_5 :
        '''
        global curr_type, curr_size
        curr_size = 1
        curr_type = p[-1]

    def p_punto_semantico_6(p):
        '''
        punto_semantico_6 :
        '''
        global curr_size
        curr_size *= p[-1]

    def p_punto_semantico_7(p):
        '''
        punto_semantico_7 :
        '''
        global curr_size
        curr_size *= p[-1]

    def p_punto_semantico_8(p):
        '''
        punto_semantico_8 :
        '''
        for id in curr_ids:
            semantica.add_variable(curr_scope, id, curr_type, 'TODO', curr_size)

    def p_punto_semantico_9(p):
        '''
        punto_semantico_9 :
        '''
        global curr_scope, count_funciones
        curr_scope = 'Funcion' + str(count_funciones)
        count_funciones += 1
        semantica.add_funcion(curr_scope)

    def p_punto_semantico_10(p):
        '''
        punto_semantico_10 :
        '''
        semantica.update_table(curr_scope, 'id', p[-1])

    def p_punto_semantico_11(p):
        '''
        punto_semantico_11 :
        '''
        global curr_id
        curr_id = p[-1]

    def p_punto_semantico_12(p):
        '''
        punto_semantico_12 :
        '''
        semantica.add_variable(curr_scope, curr_id, curr_type, 'TODO', curr_size)
        dir_func[curr_scope]['param_types'].append(curr_type)

    def p_punto_semantico_13(p):
        '''
        punto_semantico_13 :
        '''
        global curr_type
        curr_type = p[-1]
        semantica.update_table(curr_scope, 'type', curr_type)

    def p_punto_semantico_14(p):
        '''
        punto_semantico_14 :
        '''
        semantica.assign_resources(curr_scope)

    def p_puntos_semantica_15(p):
        '''
        puntos_semantica_15 :
        '''
        global curr_scope
        curr_scope = 'main'
        semantica.add_inicio()

    return yacc.yacc()


def test_parser():
    junior_script = JSParser()
    try:
        file = open("./tests/test_file.txt", "r")
        print(f"----------------- JuniorScript -----------------")
        archivo = file.read()
        file.close()
        junior_script.parse(archivo)
    except EOFError:
        print('ERROR')


if __name__ == '__main__':
    test_parser()
