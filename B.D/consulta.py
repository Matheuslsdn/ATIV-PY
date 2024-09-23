from app import db
from app import app
from app.models import fruta

# with app.app_context():
#     users = User.query.all()
#     print(users)

with app.app_context():
    users = fruta.query.all()
    print(users)