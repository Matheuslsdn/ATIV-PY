from app import db
# from models import User
from app.models import fruta
from app import app
from datetime import date

nova_fruta = fruta(
    nome='Pera', 
    preco=2.20, 
    datacolheita = date(2024,8,22),
    vencimento = date(2024,9,3),
    descricao = 'Uvas frescas e sem sementes'
    )

with app.app_context():
    db.session.add(nova_fruta)
    db.session.commit()

# novo_usuario = User(username='joâo', email='jão@zinho')
# with app.app_context():
#     db.session.add(novo_usuario)
#     db.session.commit()
    
