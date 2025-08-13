from flask import Flask, render_template, request, flash, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'uma string secreta'  # Necessário para flash e sessão

@app.route('/', methods=['GET', 'POST'])
def index():
    name = session.get('name')
    if request.method == 'POST':
        ## Entra se enviado via formulário
        new_name = request.form.get('name')
        if new_name:
            if name and name != new_name:
                flash('Parece que você mudou seu nome!')
            session['name'] = new_name
            return redirect(url_for('index'))
        else:
            flash('Por favor, preencha o nome.')
    ## Entra se acessado via navegador (GET)
    return render_template('index.html', name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True) 