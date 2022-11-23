from apiflask import APIBlueprint, abort
from flask import jsonify

from ..extension import db
from ..model import Enseignant
from .schema import EnseignantIn, EnseignantOut

ens = APIBlueprint('Enseignant', __name__, tag={
    'name': 'Enseignant', 'description': 'Espace Enseignant : Vous pouvez rechercher un Enseignant par son id, vous pouvez aussi faire le Crud'
})


@ens.get('/enseignants')
@ens.output(EnseignantOut)
def all_Enseignants():
    enseignants = Enseignant.query.all()
    schema = EnseignantOut()

    output = schema.dump(enseignants, many=True)
    return jsonify(output)


@ens.get('/enseignant/<int:id>')
@ens.output(EnseignantOut)
def getEnseignantById(id):
    enseignant = Enseignant.query.filter_by(id=id).first()

    if enseignant is not None:
        return enseignant, 200
    abort(404)


@ens.post('/enseignant')
@ens.input(EnseignantIn)
def createEnseignant(data):
    EnseignantSave = Enseignant(**data)
    EnseignantSave.save()
    return {'message': 'Enseignant saved successfully'}


@ens.put('/enseignant/<int:id>')
@ens.input(EnseignantIn)
@ens.output(EnseignantOut)  # Model de sortie
def updateEnseignant(id, data):
    enseignant = Enseignant.query.filter_by(id=id).first()
    if enseignant is not None:
        enseignant.noms = data['noms']
        enseignant.grade = data['grade']
        enseignant.telephone = data['telephone']
        db.session.commit()
        return enseignant
    abort(404)


@ens.delete('/enseignant/<int:id>')
def deleteEnseignant(id):
    enseignant = Enseignant.query.filter_by(id=id).first()
    if enseignant is not None:
        enseignant.remove()
        return {'message': 'deleted successfully'}
    abort(404)
