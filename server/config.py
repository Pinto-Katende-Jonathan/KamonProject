"""Flask configuration."""
import os

class Config:
    """Base config."""
    SECRET_KEY = 'Pinto Katende Jonathan secret'
    MAX_CONTENT_LENGTH = 1*1024*1024 #1MB
    UPLOAD_PATH = "/projet/produit_/images_produits"
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    #SQLALCHEMY_ECHO='True'