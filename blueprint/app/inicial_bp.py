from flask import Blueprint, request, render_template

inicial_bp = Blueprint('inicial',__name__)

#rotas da pagina inicial
@inicial_bp.route('/inicial')
def index():
    return 'Bem vindo a página incial'

lista = [] 
@inicial_bp.route('/produtos/adicionar', methods=['POST', 'GET'])
def add_produtos():
    if request.method == 'POST':
        produto = request.form.get('produto')
        lista.append(produto) 
    return '''
    <form action="/produtos/adicionar" method="post">
        <label for="produtos">Adicione um produto:</label><br>
        <input type="text" id="produto" name="produto"><br>
        <input type="submit" value="Adicionar">
    </form>
    '''

@inicial_bp.route('/produtos', methods=['POST', 'GET'])
def produtos():
    return render_template('produtos.html', lista=lista)

