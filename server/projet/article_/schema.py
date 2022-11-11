from apiflask.fields import Integer, String, Date, Boolean, Float, List, Dict, File
from apiflask import Schema

 #la entrée des valeurs du User au niveau de la doc(api) 
class ArticleIn(Schema):
    code = String()
    description = String()
    image = File()
    qty_stock = Integer()
    prix_unitaire = Float()

 #la sortie des valeurs du User au niveau de la doc(api)  
class ArticleOut(Schema):
    id = Integer()
    code = String()
    description = String()
    image = String()
    qty_stock = Integer()
    prix_unitaire = Float()