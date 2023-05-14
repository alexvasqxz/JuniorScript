# ------------------------------------------------------------
# js_lexer.py
#
# (Python Lex & Yacc)
# Analisis Lexico
#
# Gustavo Vasquez
# ------------------------------------------------------------

import ply.lex as lex

palabras_reservadas = {
    'mi_programa': 'PROGRAMA',
    'MI_PROGRAMA': 'PROGRAMA',
    'mi_funcion': 'FUNCION',
    'MI_FUNCION': 'FUNCION',
    'iniciar' : 'MAIN',
    'INICIAR' : 'MAIN',
    'variable': 'VAR',
    'VARIABLE': 'VAR',
    'entero': 'TIPOENT',
    'ENTERO' : 'TIPOENT',
    'decimal': 'TIPODEC',
    'DECIMAL': 'TIPODEC',
    'letra' : 'TIPOLETRA',
    'LETRA': 'TIPOLETRA',
    'logico': 'TIPOLOGI',
    'LOGICO': 'TIPOLOGI',
    'verdadero': 'TRUE',
    'VERDADERO': 'TRUE',
    'falso' : 'FALSE',
    'FALSO' : 'FALSE',
    'imprimir': 'ESCRITURA',
    'IMPRIMIR': 'ESCRITURA',
    'leer' : 'LECTURA',
    'LEER' : 'LECTURA',
    'condicion': 'IF',
    'CONDICION' : 'IF',
    'alternativa' : 'ELSE',
    'ALTERNATIVA': 'ELSE',
    'para_cada' : 'FOR',
    'PARA_CADA' : 'FOR',
    'en_cada' : 'IN',
    'EN_CADA' : 'IN',
    'conforme' : 'CONFORME',
    'CONFORME' : 'CONFORME',
    'mientras' : 'WHILE',
    'MIENTRAS' : 'WHILE',
    'regresar' : 'RETURN',
    'REGRESAR' : 'RETURN',
    'YYY' : 'AND',
    'OOO' : 'OR',
    'vacio' : 'VOID',
    'VACIO': 'VOID',
}

# Lista de Tokens
tokens = [
    'ID',
    'CTEDECI',
    'CTEENT',
    'CTELETRA',
    'CTEFRASE',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'LBRACE',
    'RBRACE',
    'COLON',
    'COMMA',
    'ASSIGN',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'EQUAL',
    'NEQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMENTARIO',
] + list(palabras_reservadas.values())

# Expresiones Regulares - Tokens Sencillos
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_COLON = r'\:'
t_COMMA = r'\,'
t_ASSIGN = r'\='
t_LT = r'\<'
t_GT = r'\>'
t_LTE = r'\<='
t_GTE = r'\>='
t_EQUAL = r'\=='
t_NEQUAL = r'\!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Expresiones Regulares - Tokens Complejos

# ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*|[\U0001F300-\U0001F5FF\U0001F900-\U0001F9FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+'
    t.type = palabras_reservadas.get(t.value, 'ID')
    return t

# Expresion regular para decimales
def t_CTEDECI(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

# Expresion regular para enteros
def t_CTEENT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Expresion regular para letras
def t_CTELETRA(t):
    r"'[^']'"
    t.value = str(t.value)
    return t

# Expresion regular para frases
def t_CTEFRASE(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

# Se ignoran comentarios
def t_COMENTARIO(t):
    r'\#{3,}.*'
    pass

# Se ignoran espacios en blanco
t_ignore = ' \t'

def t_newline(t):
    r'\n+'

# Manejo de caracteres invalidos
def t_error(t):
    print("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el Lexer
lexer = lex.lex()
