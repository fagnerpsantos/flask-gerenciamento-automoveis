from ..models import veiculo_model
from app import db


def cadastrar_veiculo(veiculo):
    veiculo_bd = veiculo_model.Veiculo(modelo=veiculo.modelo, cor=veiculo.cor,
                                    marca=veiculo.marca, potencia=veiculo.potencia)
    db.session.add(veiculo_bd)
    db.session.commit()
    return veiculo_bd


def listar_veiculos():
    veiculos = veiculo_model.Veiculo.query.all()
    return veiculos


def listar_veiculo_id(id):
    veiculo = veiculo_model.Veiculo.query.filter_by(id=id).first()
    return veiculo


def editar_veiculo(veiculo_bd, veiculo_nova):
    veiculo_bd.modelo = veiculo_nova.modelo
    veiculo_bd.cor = veiculo_nova.cor
    veiculo_bd.marca = veiculo_nova.marca
    veiculo_bd.potencia = veiculo_nova.potencia
    db.session.commit()


def remover_veiculo(veiculo):
    db.session.delete(veiculo)
    db.session.commit()