from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class VeiculoForm(FlaskForm):
    modelo = StringField("modelo", validators=[DataRequired()])
    cor = StringField("cor", validators=[DataRequired()])
    marca = StringField("marca", validators=[DataRequired()])
    potencia = FloatField("potencia", validators=[DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()],
                       choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')])
