from flask import Blueprint, render_template

#criação do blueprint
main_bp = Blueprint('main',__name__,template_folder='templates/main')

#rotas da pagina inicial
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/sobre')
def sobre():
    return 'página sobre'

#tratamento do erro 404
@main_bp.app_errorhandler(404)
def pagina_404(e):
    return render_template('404.html'), 404

#tratamento do erro 500
@main_bp.app_errorhandler(500)
def pagina_500(e):
    return render_template('500.html'), 500

