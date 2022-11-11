from apiflask import APIFlask

def create_app():
    app = APIFlask(__name__, title="Projet Gloire Kamon")

    from flask_jwt_extended import JWTManager
    JWTManager(app)#Initialisation de jwt

    from flask_cors import CORS
    CORS(app)
    
    from .client_.view import cli
    from .facture_.view import fac
    from .article_.view import art
    from .user_.view import use

    app.register_blueprint(cli)
    app.register_blueprint(fac)
    app.register_blueprint(art)
    app.register_blueprint(use)
    
    return app