from apiflask import APIBlueprint, abort
from .schema_ import UserOut, UserIn
from flask import jsonify
from ..model import User
from ..extension import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required)  # Access token


use = APIBlueprint('users', __name__, tag={
    'name': 'Users', 'description': "Espace  utilisateur : Vous pouvez même réinitialiser les mots de passe à l'aide de l'email"
})

# tous les users


@use.get('/users')
@jwt_required()
@use.output(UserOut)
def users():
    users = User.query.order_by(User.id.desc()).all()

    schema = UserOut()
    # Pour avoir toute la liste(cfr marshallow)
    output = schema.dump(users, many=True)

    return jsonify(output)

# obtenir les infos d'un user par son id


@use.get('/user/<int:id>')
@jwt_required()
@use.output(UserOut)
def user(id):
    user = User.query.filter_by(id=id).first()

    if user is not None:
        return user, 200

    abort(404)

# créer un user


@use.post('/user')
@jwt_required()
@use.input(UserIn)
def create_user(data):
    #data = request.json
    user = User.query.filter_by(email=data.get('email')).first()
    if user is None:
        user = User(email=data.get('email'),
                    password=generate_password_hash(data.get('password')))
        user.save()
        return {'message': 'added successfully'}, 201
    return {'message': "l'email existe déjà"}


# MàJ des infos du user à l'aide de son email.
@use.put('/user/<int:id>')
@jwt_required()
@use.input(UserIn)
@use.output(UserOut)
def user_update(id, data):
    user = User.query.filter_by(id=id).first()
    if user:
        email_check = User.query.filter_by(email=data.get('email')).first()
        if email_check:
            return jsonify({'message': 'Cet email existe deja'})
        user.email = data.get('email')
        user.password = generate_password_hash(data.get('password'))
        # print(user.email)
        db.session.commit()
        return user
    abort(404)

# Supprimer un user par son id


@use.delete('/user/<int:id>')
@jwt_required()
def user_delete(id):
    user = User.query.filter_by(id=id).first()
    if user:
        user.remove()
        return {'message': 'deleted successfully'}
    abort(404)


# LOGIN
# =======================================

@use.post('/login')
@use.input(UserIn, location='json')
def login(data):
    email = data.get('email')
    password = data.get('password')

    db_user = User.query.filter_by(email=email).first()

    if db_user and db_user.check_password(password):
        access_token = create_access_token(identity=db_user.email)
        refresh_token = create_refresh_token(identity=db_user.email)

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        })
    else:
        return jsonify({
            "message": "check your email or your password"
        })

# Refresh token
# =======================


@use.post('/refresh')
@jwt_required(refresh=True)
def refresh_tok():
    current_user = get_jwt_identity()

    new_access_token = create_access_token(identity=current_user)

    return make_response(jsonify({
        "access_token": new_access_token
    }), 200)
