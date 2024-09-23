from flask import Flask

def create_app():
    app = Flask(__name__)
    
    
    
    
    
    from .user_route import (user_bp)
    app.register_blueprint(user_bp, url_prefix='/perfil')
    
    from .inicial_bp import (inicial_bp)
    app.register_blueprint(inicial_bp)
    
    from .contato_bp import (contato_bp)
    app.register_blueprint(contato_bp)
    
    from .produtos_bp import (produtos_bp)
    app.register_blueprint(produtos_bp, url_prefix='/nossa_empresa')
    
    
    return app