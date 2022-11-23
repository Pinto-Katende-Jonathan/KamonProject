from projet import create_app
from projet.extension import db
from flask_migrate import Migrate

app = create_app()
app.config.from_object('config.DevConfig')

app.app_context().push()
db.init_app(app)
migrate = Migrate(app, db)

db.create_all()

if __name__=="__main__":
    app.run(debug=True)