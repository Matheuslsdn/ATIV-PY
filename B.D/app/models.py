from app import db 

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(200), unique=True,nullable=False)
   
#     def __repr__(self):
#         return f'<User> {self.username}'
    
class fruta(db.Model):
    
    __tablename__ = 'fruta'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    datacolheita = db.Column(db.Date, nullable=False)
    vencimento = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<fruta> {self.nome}'