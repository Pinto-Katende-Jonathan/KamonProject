from apiflask import APIBlueprint, abort
from .schema_ import *
from ..model import Client
from flask import jsonify
from ..extension import db

cli = APIBlueprint('clients', __name__, tag={
      'name': 'Clients', 'description':'Espace du Client : vous pouvez rechercher une personne par son numéro'
    })

#Test de communication avec le frotend
@cli.get("/hello")
def hello():
    return {
        "message": "hello from Backend"
    }

#tous les clients  
@cli.get('/clients')
@cli.output(ClientOut)
def clients():
    clients = Client.query.all()

    schema = ClientOut()
    output = schema.dump(clients, many=True)#Pour avoir toute la liste(cfr marshallow)
    
    return jsonify(output)

#obtenir les infos d'un client par son numéro
@cli.get('/client/<string:phone>')
@cli.output(ClientOut)
def client(phone):
    client = Client.query.filter_by(phone=phone).first()

    if client is not None:
        return client, 200

    abort(404)

#créer un client
@cli.post('/client')
@cli.input(ClientIn, location='json')
# @app.output(ClientOut)
def create_client(data):
    #data = request.json
    client = Client.query.filter_by(phone=data.get('phone')).first()
    if client is None:
        client = Client(**data)
        client.save()
        return {'message':'added successfully'}, 201
    return {'message':'le numéro existe déjà'}
    

# MàJ des infos du client à l'aide de son numéro.
@cli.put('/client/<int:id>')
@cli.input(ClientIn, location='json')
@cli.output(ClientOut)
def client_update(id, data):
    client = Client.query.filter_by(id=id).first()

    client.name = data.get('name')
    client.phone = data.get('phone')
    db.session.commit()

    return client

#Supprimer un client par son numéro
@cli.delete('/client/<int:id>')
def client_delete(id):
    try:
        client = Client.query.filter_by(id=id).first()
        client.remove()   
        return {'message': 'deleted successfully'}
    except:
        abort(404)