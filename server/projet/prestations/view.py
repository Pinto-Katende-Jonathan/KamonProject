from apiflask import APIBlueprint, abort
from .schema import PrestationOut, PrestationIn
from ..model import Prestation, Cours, Enseignant

from flask import jsonify
from ..extension import db

pre = APIBlueprint('Prestations', __name__, tag={
    'name': 'Prestations', 'description': 'Espace des Prestations : Vous pouvez rechercher une Prestation par son id'
})


@pre.get('/prestations')
@pre.output(PrestationOut)
def all_Prestations():
    prestations = Prestation.query.all()
    schema = PrestationOut()

    output = schema.dump(prestations, many=True)
    return jsonify(output)


@pre.get('/prestation/<int:id>')
@pre.output(PrestationOut)
def getPrestationbyId(id):
    prestation = Prestation.query.filter_by(id=id).first()

    if prestation is not None:
        return prestation, 200
    abort(404)


@pre.post('/prestation')
@pre.input(PrestationIn)
def createPrestation(data):
    enseignant = Enseignant.query.filter_by(id=data['enseignant_id']).first()
    cours = Cours.query.filter_by(id=data['cours_id']).first()

    if (enseignant is not None) and (cours is not None):
        prestation = Prestation(
            heureDebut=data['heureDebut'],
            heureFin=data['heureFin'],
            enseignant=enseignant,
            cours=cours)
        prestation.save()
        return {'message': 'Prestation added successfully'}, 201
    return {'message': 'check enseignant and cours'}


@pre.delete('/prestation/<int:id>')
def DeletePrestationById(id):
    prest = Prestation.query.filter_by(id=id).first()
    if prest is not None:
        prest.remove()
        return {'message': 'Deleted successfully'}
    abort(404)
