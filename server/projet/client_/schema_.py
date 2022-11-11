from apiflask.fields import Integer, String, Date, Boolean, Float, List, Dict
from apiflask import Schema

#l'entrée des valeurs du client au niveau de la doc(api)
class ClientIn(Schema):
    name = String(required=True)
    phone = String(required=True)
 
 #la sortie des valeurs au niveau de la doc(api) 
class ClientOut(Schema):
    id = Integer()
    name = String()
    phone = String()
    date = Date()