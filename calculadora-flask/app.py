from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = request.form.get('num1', type=float)
    num2 = request.form.get('num2', type=float)
    op = request.form.get('op')
    if op == 'add':
        resultado = num1 + num2
    elif op == 'sub':
        resultado = num1 - num2
    elif op == 'mul':
        resultado = num1 * num2
    elif op == 'div':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    else:
        resultado = "Operação inválida"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)