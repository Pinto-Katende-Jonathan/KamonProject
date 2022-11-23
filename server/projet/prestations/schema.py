from apiflask.fields import Integer, String, Date,Time
from apiflask import Schema

 #la entrée des valeurs du User au niveau de la doc(api) 
class PrestationIn(Schema):
    datePrestation = Date()
    heureDebut = String()
    heureFin = String()
    enseignant_id = Integer()
    cours_id = Integer()

 #la sortie des valeurs du User au niveau de la doc(api)  
class PrestationOut(Schema):
    id = Integer()
    datePrestation = Date()
    heureDebut = String()
    heureFin = String()
    enseignant_id = Integer()
    cours_id = Integer()