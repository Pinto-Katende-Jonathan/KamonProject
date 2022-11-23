from apiflask.fields import Integer, String
from apiflask import Schema

 #la entrée des valeurs du User au niveau de la doc(api) 
class EnseignantIn(Schema):
    noms = String()
    grade = String()
    telephone = String()

 #la sortie des valeurs du User au niveau de la doc(api)  
class EnseignantOut(Schema):
    id = Integer()
    noms = String()
    grade = String()
    telephone = String()