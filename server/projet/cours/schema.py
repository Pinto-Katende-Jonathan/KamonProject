from apiflask.fields import Integer, String
from apiflask import Schema

# la entrée des valeurs (Cours) au niveau de la doc(api)


class CoursIn(Schema):
    int_cours = String()
    volume = Integer()

 # la sortie des valeurs (Cours) au niveau de la doc(api)


class CoursOut(Schema):
    id = Integer()
    int_cours = String()
    volume = Integer()
