from apiflask import APIBlueprint, abort
from .schema import CoursOut, CoursIn
from ..model import Cours
from flask import jsonify
from ..extension import db

crs = APIBlueprint('cours', __name__, tag={
      'name': 'Cours', 'description':'vous pouvez faire le CRUD des cours' 
    })

@crs.get('/cours')
@crs.output(CoursOut)
def all_cours():
    cours = Cours.query.all()
    schema = CoursOut()
    output = schema.dump(cours, many=True)#Pour avoir toute la liste(cfr marshallow)
    return jsonify(output)

@crs.get('/cours/<int:id>')
@crs.output(CoursOut)
def getCoursById(id):
    oneCours = Cours.query.filter_by(id=id).first()
    
    if oneCours is not None:
        return oneCours, 200
    abort(404)

@crs.post('/cours')
@crs.input(CoursIn)
def createCours(data):
    coursSave = Cours(**data)
    coursSave.save()
    return {'message':'cours saved successfully'}
    
@crs.put('/cours/<int:id>')
@crs.input(CoursIn)
@crs.output(CoursOut)#Model de sortie
def updateCours(id, data):
    cours = Cours.query.filter_by(id=id).first()
    if cours is not None:
        cours.int_cours = data['int_cours']
        #print(data['int_cours'])
        cours.volume = data['volume']
        db.session.commit()
        return cours
        #return  {'message':'updated successfully'}
    abort(404)
    #return  {'message':'Error to update'}

@crs.delete('/cours/<int:id>')
def deleteCours(id):
    cours = Cours.query.filter_by(id=id).first()#Selection du cours au travers son id
    if cours is not None:
        cours.remove()
        return {'message': 'deleted successfully'}
    abort(404)