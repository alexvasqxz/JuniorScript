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
        code = get_file_text("test_file.txt")
        result = run_parser(code)

    return render_template('compiler.html', code=code, result=result)

if __name__ == '__main__':
    app.run(debug=True, port='2014')
