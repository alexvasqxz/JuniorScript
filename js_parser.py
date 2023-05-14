# ------------------------------------------------------------
# js_parser.py
#
# (Python Lex & Yacc)
# Analisis Sintaxico
#
# Gustavo Vasquez
# ------------------------------------------------------------

import ply.yacc as yacc
from js_lexer import tokens

def JSParser():
    def p_programa(p):
        '''
        programa : PROGRAMA ID programaB programaC inicio
        programaB : dec_vars
                | empty
        programaC : dec_func programaCC
        programaCC : programaC
                | empty
        '''
        p[0] = None

    def p_dec_vars(p):
        '''
        dec_vars : VAR dec_varsI COLON tipo dec_varsB dec_varsBB
        dec_varsI : ID dec_varsII
        dec_varsII : COMMA ID
                | empty
        dec_varsB : LBRACE CTEENT RBRACE
                | LBRACE CTEENT RBRACE LBRACE CTEENT RBRACE
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
        p[0] = None

    def p_dec_func(p):
        '''
        dec_func : FUNCION ID LPAREN dec_params RPAREN COLON tipo_func LCURLY bloque RCURLY
        '''
        p[0] = None


    def p_dec_params(p):
        '''
        dec_params : ID COLON tipo dec_paramsB
        dec_paramsB : COMMA dec_params
                    | empty
        '''
        p[0] = None

    def p_tipo_func(p):
        '''
        tipo_func : tipo
                | VOID
        '''
        p[0] = None

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
        inicio : MAIN LPAREN RPAREN LCURLY bloque RCURLY
        '''
        p[0] = None

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