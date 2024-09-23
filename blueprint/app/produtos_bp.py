from flask import Blueprint, render_template

#criação do blueprint
produtos_bp = Blueprint('produto',__name__, template_folder='templates/main')

#rotas da pagina inicial
@produtos_bp.route('/produto')
def index():
    lista = ['Produto 1', 'Produto 2', 'Produto 3']
    return render_template('produto.html', lista=lista)