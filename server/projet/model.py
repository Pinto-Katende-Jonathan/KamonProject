from .extension import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

# -------- User--------------------------
"""
Class User:
    id int
    email str
    password str
    created_at datetime
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email


# --------Cours--------------------------
"""
Class Cours:
    id int
    int_cours str(25)
    volume int
"""


class Cours(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    int_cours = db.Column(db.String(25),
                          nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    prestations = db.relationship('Prestation', backref='cours')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Cours {self.int_cours} VH:{self.volume}>'


# --------Enseignant---------------------
"""
Class Enseignant:
    id int
    noms str(75)
    grade str
    telephone str(10)
"""


class Enseignant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    noms = db.Column(db.String(75), nullable=False)
    grade = db.Column(db.String(15), nullable=False)
    telephone = db.Column(db.String(10),
                          nullable=False, unique=True)
    prestations = db.relationship(
        'Prestation', backref='enseignant')  # 1 to many
    # backref : nom de la colonne parent au niveau de l'enfant (enf : Prestation).
    # l'enfant pourrait manipuler le parent à l'aide de backref

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Ens : {self.noms} Grade : {self.grade}>'


# ------Prestation----------------
"""
Class Prestation:
    id int
    datePrestation date
    heureDebut time
    heureFin time
"""


class Prestation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datePrestation = db.Column(db.Date, server_default=func.now())
    heureDebut = db.Column(db.String(10), nullable=False)
    heureFin = db.Column(db.String(10), nullable=False)
    enseignant_id = db.Column(db.Integer, db.ForeignKey(
        'enseignant.id'), nullable=False)  # child
    cours_id = db.Column(db.Integer, db.ForeignKey(
        'cours.id'), nullable=False)  # child
    paiements = db.relationship('Paiement', backref='prestation')  # parent

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Prestation : {self.datePrestation}>'


# -----Paiement---------------------
"""
Class Paiement :
    id int
    datePaiement date
"""


class Paiement (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datePaiement = db.Column(db.Date, server_default=func.now())
    prestation_id = db.Column(db.Integer, db.ForeignKey(
        'prestation.id'), unique=True, nullable=False)  # child

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
