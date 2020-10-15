from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views import cliente_view, veiculo_view, funcionario_view
from .models import cliente_model, funcionario_model, veiculo_model
