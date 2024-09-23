from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def set_cookie():
    response = make_response('cookies foi definido')
    response.set_cookie('username','Matheus', max_age=60*60*24)
    return response

@app.route('/get_cookie')
def get_cookie():
    usuario = request.cookies.get('username')
    return f'usuarios armazenados no cookie é: {usuario}'

@app.route('/definir_cookie')
def definir_cookie():
    response = make_response('Vamos definir')
    response.set_cookie('mensagem','Deu certo')
    return response

@app.route('/obter_cookie')
def obter_cookie():    
    return f'{request.cookies.get('mensagem')}'
    
@app.route('/visit_counter')
def visit_counter():
    if request.cookies.get('visit_count'):
        visit_count = int(request.cookies.get('visit_count')) + 1
        response = make_response(render_template('visit.html', visit_count=visit_count))
        response.set_cookie('visit_count', str(visit_count), max_age=60*60*24)
        return response
    else:
        response = make_response(render_template('visit.html', visit_count=1))
        response.set_cookie('visit_count', '1', max_age=60*60*24)
        return response
                                 


if __name__ == '__main__':
    app.run(debug=True)