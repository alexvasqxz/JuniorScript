import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from js_lexer import lexer

class MyTestCase(unittest.TestCase):

    # Probar IDs
    def test_ID(self):
        results = []
        input = '''
            🐍🐍🐍
            var_hello_world
            _id_3452
        '''
        lexer.input(input)
        while True:
            tok = lexer.token()
            if not tok:
                break
            assert tok.type == 'ID'

    # Probar Enteros
    def test_CTEENT(self):
        results = []
        input = '''
            -3453
            499392
            92859
        '''
        lexer.input(input)
        while True:
            tok = lexer.token()
            if not tok:
                break
            assert tok.type == 'CTEENT'

    # Probar Decimales
    def test_CTEDECI(self):
        results = []
        input = '''
            -3453.0
            499392.529482
            92859.9249
        '''
        lexer.input(input)
        while True:
            tok = lexer.token()
            if not tok:
                break
            assert tok.type == 'CTEDECI'

    # Probar Letras
    def test_CTELETRA(self):
        results = []
        input = '''
            'a' '5' '#'
        '''
        lexer.input(input)
        while True:
            tok = lexer.token()
            if not tok:
                break
            assert tok.type == 'CTELETRA'

    # Probar Frases
    def test_CTEFRASE(self):
        results = []
        input = '''
            "frase1" "_HelloWorld" "4729302"
        '''
        lexer.input(input)
        while True:
            tok = lexer.token()
            if not tok:
                break
            assert tok.type == 'CTEFRASE'


if __name__ == '__main__':
    data_input = open("./tests/test_file.txt", "r")
    input = data_input.read()
    data_input.close()

    lexer.input(input)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    with open("./tests/lexer_output.txt", "x") as output_file:
        output_file.write("Junior Script Lexer\n")
        output_file.write('\n'.join(str(token) for token in tokens))

    unittest.main()


