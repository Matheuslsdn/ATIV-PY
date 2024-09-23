from app import db
from app import app
from app.models import fruta

with app.app_context():
    db.create_all()