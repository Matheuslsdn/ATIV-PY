from flask import Blueprint, render_template

#criação do blueprint
contato_bp = Blueprint('contato',__name__, template_folder='templates/main')

#rotas da pagina inicial
@contato_bp.route('/contato')
def index():
    return render_template('contato.html')

