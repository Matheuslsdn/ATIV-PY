from flask import Blueprint, render_template

#criação do blueprint
user_bp = Blueprint('user',__name__,template_folder='templates/user')

#rotas da pagina inicial
@user_bp.route('/user')
def user():
    return render_template('login.html')

@user_bp.route('/user2')
def sobre():
    return render_template('perfil.html')