from flask import Flask, session, request, redirect, url_for, render_template
from datetime import timedelta, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "mopazmano"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
@app.route('/')
def set_session():
    session.permanent = True
    session['username']= "Matheus"
    return 'sessão iniciada com sucesso'

@app.route('/get_session')
def get_session():
    usuario = session.get('username')
    return f'usuario armazenado na sessão é: {usuario}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:  
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return 'Erro: Por favor, insira um nome de usuário.', 400
    return '''
        <form action="" method="post">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <input type="submit" value="Login">
        </form>
    '''
    
@app.route('/bem_vindo')
def welcome():
    if 'username' in session:
        username = session['username']
        return f'Bem-vindo, {username}!'
    return redirect(url_for('login'))

@app.route('/visita_contador_session')
def visita_contador_session():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1
    return f'Você visitou esta página {session["visitas"]} vezes durante a sessão atual.'

@app.route('/set_permanent_session')
def set_permanent_session():
    session.permanent = True
    session.modified_since = datetime.utcnow()
    session['cart'] = []
    return 'Sessão permanente configurada com sucesso!'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/session_time_left')
def session_time_left():
    session_lifetime = app.permanent_session_lifetime
    session_modified_since = session.modified_since
    remaining_time = session_lifetime - (datetime.utcnow() - session_modified_since)
    minutes, seconds = divmod(remaining_time.seconds, 60)
    return render_template('tempo.html', minutes=minutes, seconds=seconds)
    
    


if __name__ == '__main__':
    app.run(debug=True)