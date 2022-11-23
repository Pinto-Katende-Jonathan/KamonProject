from apiflask import APIBlueprint, abort
from .schema_ import UserOut, UserIn
from flask import jsonify
from ..model import User
from ..extension import db
from werkzeug.security import generate_password_hash, check_password_hash


use = APIBlueprint('users', __name__, tag={
      'name': 'Users', 'description':"Espace  utilisateur : Vous pouvez même réinitialiser les mots de passe à l'aide de l'email"
    })

#tous les users  
@use.get('/users')
@use.output(UserOut)
def users():
    users = User.query.order_by(User.id.desc()).all()

    schema = UserOut()
    output = schema.dump(users, many=True)#Pour avoir toute la liste(cfr marshallow)

    return jsonify(output)

#obtenir les infos d'un user par son id
@use.get('/user/<int:id>')
@use.output(UserOut)
def user(id):
    user = User.query.filter_by(id=id).first()

    if user is not None:
        return user, 200

    abort(404)

#créer un user
@use.post('/user')
@use.input(UserIn)
def create_user(data):
    #data = request.json
    user = User.query.filter_by(email=data.get('email')).first()
    if user is None:
        user = User(email=data.get('email'), password=generate_password_hash(data.get('password')))
        user.save()
        return {'message':'added successfully'}, 201
    return {'message':"l'email existe déjà"}
    

# MàJ des infos du user à l'aide de son email.
@use.put('/user/<int:id>')
@use.input(UserIn)
@use.output(UserOut)
def user_update(id, data):
    user = User.query.filter_by(id=id).first()
    if user:
        email_check = User.query.filter_by(email=data.get('email')).first()
        if email_check:
            return jsonify({'message':'Cet email existe deja'})
        user.email=data.get('email')
        user.password = generate_password_hash(data.get('password'))
        #print(user.email)
        db.session.commit()
        return user
    abort(404)

#Supprimer un user par son id
@use.delete('/user/<int:id>')
def user_delete(id):
    user = User.query.filter_by(id=id).first()
    if user:
        user.remove()
        return {'message': 'deleted successfully'}
    abort(404)
