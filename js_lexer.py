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
    'mi_funcion': 'FUNCION',
    'iniciar' : 'MAIN',
    'variable': 'VAR',
    'entero': 'TIPOENT',
    'decimal': 'TIPODEC',
    'letra' : 'TIPOLETRA',
    'logico': 'TIPOLOGI',
    'verdadero': 'TRUE',
    'falso' : 'FALSE',
    'imprimir': 'ESCRITURA',
    'leer' : 'LECTURA',
    'condicion': 'IF',
    'alternativa' : 'ELSE',
    'desde' : 'FOR',
    'hasta' : 'TO',
    'mientras' : 'WHILE',
    'regresar' : 'RETURN',
    'YYY' : 'AND',
    'OOO' : 'OR',
    'vacio' : 'VOID'
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
    r'[a-zA-Z_][a-zA-Z0-9_]*|[\U0001F000-\U0001FFFF]+'
    t.type = palabras_reservadas.get(t.value, 'ID')
    return t

# Expresion regular para decimales
def t_CTEDECI(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Expresion regular para enteros
def t_CTEENT(t):
    r'\d+'
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
