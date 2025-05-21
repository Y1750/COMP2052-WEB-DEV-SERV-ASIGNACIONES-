import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-flask')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:asdzxc12@localhost/inventario'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
