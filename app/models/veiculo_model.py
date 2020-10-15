from app import db
import enum
from sqlalchemy_utils import ChoiceType

class CoresCarro(enum.Enum):
    vermelho = 1
    preto = 2
    amarelo = 3
    prata = 4
    branco = 5
    azul = 6

class Veiculo(db.Model):
    __tablename__ = "veiculo"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.Enum(CoresCarro), nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    potencia = db.Column(db.Float, nullable=False)