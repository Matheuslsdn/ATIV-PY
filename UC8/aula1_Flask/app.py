# Importa a classe flask do módulo flask
from flask import Flask

# Cria uma instância da classe Flask
app = Flask(__name__)

# Define a rota para a página inicial
@app.route('/')
def home():
    return 'olá flask'        

@app.route('/contato')
def contato():
    return 'Página de contato'

@app.route('/mensagem/<nome>')
def mensagem(nome):
    return f'Olá, querido {nome}, como você está?'

if __name__== '__main__':
    app.run(debug=True)