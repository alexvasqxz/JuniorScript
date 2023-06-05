import os
from flask import Flask, render_template, request, redirect
from js_parser import run_parser, get_file_text

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/recursos')
def recursos():
    return render_template('preguntas.html')


@app.route('/credits')
def credits():
    return render_template('credits.html')


@app.route('/compiler', methods=['POST', 'GET'])
def compiler():
    if request.method == 'POST':
        code = request.form.get('editor')
        try:
            result = run_parser(code)
        except Exception as err:
            result = str(err)
    else:
        code = ""
        result = "🐍💻📕🎒🤖 JuniorScript 🐍💻📕🎒🤖\nAquí se mostraran tus resultados impresos"

    return render_template('compiler.html', code=code, result=result)


@app.route('/load-file/<filename>')
def load_file(filename):
    filepath = os.path.join('./tests/examples/', f"{filename}.txt")
    with open(filepath, 'r') as file:
        content = file.read()
    return content


if __name__ == '__main__':
    app.run(debug=True, port='4013')
