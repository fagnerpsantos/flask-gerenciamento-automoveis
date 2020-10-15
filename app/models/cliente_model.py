from app import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome_completo = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
