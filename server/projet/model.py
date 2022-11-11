from .extension import db
from sqlalchemy.sql import func
"""
A one to many relationship places a foreign key on the child table referencing the parent. relationship() is then specified on the parent, as referencing a collection of items represented by the child
"""
#Article
#------------------
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(80), nullable=False)
    image =db.Column(db.String(255), unique=True, nullable=False, default='default.jpg')
    qty_stock = db.Column(db.Integer)
    prix_unitaire = db.Column(db.Float)
    
    def to_json(self):
        return {
          'produit_id':self.id,
          'code_produit':self.code,
          'description':self.description,
          'image_name':self.image,
          'qty_stock':self.qty_stock,
          'prix_unitaire':self.prix_unitaire
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def remove(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return '<Produit %r>' % self.description

#Client
#------------------
class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    phone =db.Column(db.String(10), unique=True, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())
    #relation with Client (Parent)
    #client_info = db.relationship('Facture', backref='client')
   
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Client %r>' % self.name
        
#Facture
#------------------
class Facture(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createdAt = db.Column(db.Date, server_default=func.now())
    montant = db.Column(db.Integer, default=0)
    discount = db.Column(db.Float, default=0)
    produits = db.Column(db.PickleType, nullable=False)#List of products with all fields in dict format
    #relation with Client
    status = db.Column(db.String(10), default='open', nullable=False)
    #lien avec le client (Enfant)
    #clientId = db.Column(db.Integer, db.ForeignKey('client.id'))
    def __repr__(self):
          return '<Facture %r>' % self.id

#User
#------------------
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username