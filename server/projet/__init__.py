from apiflask import APIFlask


def create_app():
    app = APIFlask(__name__, title="Projet Karl")

    from flask_cors import CORS
    CORS(app)

    from .users.view import use
    from .prestations.view import pre
    from .cours.view import crs
    from .enseignants.view import ens
    #from .paiements.view import pai

    app.register_blueprint(use)
    app.register_blueprint(pre)
    app.register_blueprint(crs)
    app.register_blueprint(ens)
    # app.register_blueprint(pai)

    return app
