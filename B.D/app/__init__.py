from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#defini db como método SqlAlchemy
db = SQLAlchemy()

#Cria a função para montar a aplicação e a retorna
def create_app():
    app = Flask(__name__)
    #configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #inicializa o metodo db para app
    db.init_app(app)
    
    #Inicio: importamos e registramos o Blueprint
    from .routes import bp
    app.register_blueprint(bp)
    #Fim: Importamos e registramos o Blueprint
    
    #retorno da montagem da aplicação
    return app
