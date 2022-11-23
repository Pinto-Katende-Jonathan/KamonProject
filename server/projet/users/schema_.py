from apiflask import Schema
from  apiflask.fields import Integer, String, Date, Boolean, Float, List, Dict, DateTime, Email

#Entrée des valeurs du User au niveau de la doc(api)
class UserIn(Schema):
    email = Email(required=True)
    password = String(required=True)
 
 #la sortie des valeurs du User au niveau de la doc(api) 
class UserOut(Schema):
    id = Integer()
    email = Email()
    password = String()
    created_at = DateTime()