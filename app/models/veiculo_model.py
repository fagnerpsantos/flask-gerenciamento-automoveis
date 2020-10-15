from app import db

class Veiculo(db.Model):
    __tablename__ = "veiculo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(10), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    potencia = db.Column(db.Float, nullable=False)