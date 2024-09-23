from flask import Blueprint, render_template
from .models import fruta

#Cria um blueprint para as rotas
bp = Blueprint('main', __name__)

#Defini a rota para a página inicial

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/frutas_caras')
def frutas_caras():
    frutas = fruta.query.all()
    return render_template('frutas_caras.html', frutas=frutas)
