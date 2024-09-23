from flask import Flask, render_template, request

app1 = Flask(__name__)

@app1.route('/')
def index():
    return render_template('index.html') 

#ativ 1
@app1.route('/tchau') 
def adeus():
    return 'Tchau mundo'


#ativ 2
@app1.route('/soma/<int:a>/<int:b>')
def soma(a, b):
    soma = a + b
    return f'A soma de {a} + {b} = {soma}'


#ativ 3    
@app1.route('/invert/<text>')
def modify(text):
    text = text[::-1]
    return f'O texto invertido fica, {text}'


#ativ 4
@app1.route('/paridade/<int:n>')
def paridade(n):
    if n % 2 == 0:
        return f'O número {n} é par'
    else:
        return f'O número {n} é impar'
    
#ativ 5
@app1.route('/calc/<operacao>/<int:a>/<int:b>')
def calculo(operacao, a, b):
    if operacao == 'adicao':
        return f'A soma é {a + b}'
    elif operacao == 'subtracao':
        return f'A subtração é {a - b}'
    elif operacao == 'multiplicacao':
        return f'A multiplicacao é {a * b}'
    elif operacao == 'divisao':
        if b != 0:
            return f'A divisao é {a / b}'
        else:
            return 'Erro: divisão por zero!'
    else:
        return 'Operação inválida!'
    
#ativ 6
@app1.route('/home')
def home():
    return render_template('home.html')

#ativ 7
@app1.route('/lista')
def lista():
    lista = ['ovos', 'leite', 'miojo', 'oleo', 'fandango']
    return render_template('lista.html', lista=lista)

#ativ 8
@app1.route('/perfil')
def perfil():
    # Nas listas utilizamos [] e nos dicionários usamos {}. 
    # Anotei pq tinha duvidas.
    usuario = {'nome':'Matheus', 'idade':'25', 'peso':'115'}
    return render_template('perfil.html', usuario=usuario)

#ativ 9
@app1.route('/ativ9')
def ativ9():
    logged = 'True'
    if logged == 'True':
        return render_template('ativ9.html', logged=logged)
    else:
        return render_template('ativ9.html', logged=logged)

#ativ 10
@app1.route('/ativ10')
def ativ10():
    dicionario = {'nome':'Matheus', 'idade': '25', 'cidade': 'Curitiba'}
    return render_template('ativ10.html', dicionario=dicionario)

#ativ 11
@app1.route('/ativ11')
def ativ11():
    dicionario = [
        {'nome': 'João Victor', 'endereço': 'Rua Alberto fontes, n° 83', 'telefone': '(11) 12345-6789', 'email': 'joaovictor123@gmail.com', 'cpf':'123.465.789-01', 'tipodeconta': 'cliente'},
        {'nome': 'Maria Silva', 'endereço': 'Rua das Flores, n° 12', 'telefone': '(11) 98765-4321', 'email': 'mariasilva@email.com', 'cpf':'987.654.321-10', 'tipodeconta': 'cliente'},
        {'nome': 'Pedro Oliveira', 'endereço': 'Rua do Mercado, n° 45', 'telefone': '(11) 55555-5555', 'email': 'pedrooliveira@hotmail.com', 'cpf':'555.555.555-55', 'tipodeconta': 'cliente'},
        {'nome': 'Ana Paula', 'endereço': 'Rua da Praia, n° 678', 'telefone': '(11) 77777-7777', 'email': 'anapaula@yahoo.com', 'cpf':'777.777.777-77', 'tipodeconta': 'cliente'},
        {'nome': 'Luiz Fernando', 'endereço': 'Rua do Parque, n° 90', 'telefone': '(11) 33333-3333', 'email': 'luizfernando@gmail.com', 'cpf':'333.333.333-33', 'tipodeconta': 'cliente'},
        {'nome': 'Julia Martins', 'endereço': 'Rua do Centro, n° 111', 'telefone': '(11) 66666-6666', 'email': 'juliamartins@outlook.com', 'cpf':'666.666.666-66', 'tipodeconta': 'cliente'}
        ]
    return render_template('ativ11.html', dicionario=dicionario)


@app1.route('/inicial')
def casa():
    return render_template('index.html')

@app1.route('/contato')
def contato():
    return render_template('contato.html')

@app1.route('/sobre', methods=['GET'])
def sobre():
    palavra= request.args.get('palavra')
    return render_template('sobre.html', palavra=palavra)

@app1.route('/team')
def team():
    return render_template('team.html')

@app1.route('/layout', methods=['GET'])
def layout():
    return render_template('layout.html')

@app1.route('/info')
def info():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    return render_template('info.html', nome=nome, idade=idade)

@app1.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome')
    return render_template('saudacao.html', nome=nome)

@app1.route('/produtos', methods=['GET'])
def produtos():
    produtos = [
        {'nome': 'Python', 'categoria':'linguagem'},
        {'nome': 'Facebook', 'categoria':'rede social'},
        {'nome': 'Java', 'categoria':'linguagem'},
        {'nome': 'Instagram', 'categoria':'rede social'}
    ]
    return render_template('produtos.html', produtos=produtos)

@app1.route('/verificar', methods=['GET'])
def verificar():
    numero = request.args.get('numero')
    return render_template('verificar.html', numero=numero)

@app1.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        usuario = request.form['usuario']
        return f'Formulário submetido com sucesso! Olá {usuario}!'
    return '''
        <form method='POST' action='/submit'>
            <label for='usuario'>Nome do usuário: </label><br>
            <input type='text' id='username' name='usuario'><br>
            <input type='submit' value='enviar'>
        </form>
    ''' 
    
    
# @app1.route('/formulario', methods=['GET', 'POST'])
# def formulario():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         email = request.form['email']
#         return f'Formulário submetido com sucesso! Olá {nome}!Seu email, {email} foi salvo no nosso Banco de Dados!'
#     return '''
#         <form method='POST' action='/formulario'>
#             <label for='nome'>Nome do usuário: </label><br>
#             <input type='text' id='name' name='nome'><br>
#             <label for='usuario'>Email usuário: </label><br>
#             <input type='text' id='email' name='email'><br>
#             <input type='submit' value='enviar'>
#         </form>
#     ''' 

usuarios = []  
  
@app1.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        usuarios.append({'nome': nome, 'email': email})  # Add the new user to the list
        return '/enviar'
    return '''
        <form method='POST' action='/enviar'>
            <label for='nome'>Nome do usuário: </label><br>
            <input type='text' id='name' name='nome'><br>
            <label for='usuario'>Email usuário: </label><br>
            <input type='text' id='email' name='email'><br>
            <input type='submit' value='enviar'>
        </form>
        <h2>Lista de usuários:</h2>
        <ul>
            {% for usuario in usuarios %}
                <li>{{ usuario['nome'] }} ({{ usuario['email'] }})</li>
            {% endfor %}
        </ul>
    '''
    
@app1.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files('arquivo')
        file.save(f"/upload/{file.filename}")
        return 'Formulário salvo com sucesso!'
    
    return '''
        <form method='POST' action='/upload' enctype="multipart/form-data">
            <input type='file' id='arquivo' name='arquivo'><br>
            <input type='submit' value='Enviar'>
        </form>
    ''' 

if __name__== '__main__':
    app1.run(debug=True)