ENV = True

USERNAME = 'root'
PASSWORD = 'rootmysql'
SERVER = 'localhost'
DB = 'flask_gerenciador_veiculos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'gerenciador-veiculos-treinaweb'