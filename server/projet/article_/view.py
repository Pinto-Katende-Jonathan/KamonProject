from apiflask import APIBlueprint, abort
from .schema import ArticleOut, ArticleIn
from ..model import Article
import os
from .preprocessing_image import *
from flask import jsonify
from ..extension import db

art = APIBlueprint('articles', __name__, tag={
      'name': 'Articles', 'description':'Espace des articles : Vous pouvez rechercher un Article par son code'
    })

@art.get('/articles')
@art.output(ArticleOut)
def all_articles():
    articles = Article.query.all()
    schema = ArticleOut()

    output = schema.dump(articles, many=True)#Pour avoir toute la liste(cfr marshallow)
    return jsonify(output)

@art.get('/article/<string:code>')
@art.output(ArticleOut)
def get_article_by_code(code):
    article = Article.query.filter_by(code=code.lower()).first()

    if article is not None:
        return article, 200

    abort(404)
    
"""
@art.get('/article/<string:name>')
@art.output(ArticleOut)
def get_all_articles_started_by_name():
    pass
"""

@art.post('/article')
@art.input(ArticleIn, location='form_and_files')
def create_article(data):
    code = data['code']
    description = data['description']
    image = data['image']
    qty_stock = data['qty_stock']
    prix_unitaire = data['prix_unitaire']
    
    article = Article.query.filter_by(code = data.get('code')).first()

    if allowed_file(image.filename):
        image_filename = secure_filename(image.filename)
        
        extension_img = image_filename.split('.')[1]
        image_filename_uuid = get_uuid()+'.'+extension_img
        image_filename_uuid = get_uuid()+'.'+extension_img   
        donnees = {
        'code': code.lower(),
        'description': description,
        'image':image_filename_uuid,
        'qty_stock': prix_unitaire,
        'prix_unitaire': prix_unitaire
        }

        try:
            if article is None:
                article = Article(**donnees)
                image.save(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', image_filename_uuid))
                #image.save(os.path.join(app.config['UPLOAD_PATH'],image_filename))
                article.save()

                return {'message': 'created successfully'}
        except:
            return {'message': 'already exist or verify your information entry'}
    return  {'message': 'seules les images sont autorisées'}
    
@art.put('/article/<string:code>')
@art.input(ArticleIn, location='form_and_files')
@art.output(ArticleOut)#Model de sortie
def update_article(code, data):
    article = Article.query.filter_by(code=code.lower()).first()#Selection du article au travers son code

    #on vérifie si article existe dans la bdd
    if article is not None:

        #On récupère l'image de la requête
        image = data['image']

        #On vérifie si le l'image a une extension valide
        if allowed_file(image.filename):

            #on recupère le nom de la nouvelle image de manière sécurisée, pour prevenir la faille XSS.
            image_filename = secure_filename(image.filename)
            extension_img = image_filename.split('.')[1]
            image_filename_uuid = get_uuid()+'.'+extension_img
            #On sauvegarde la nouvelle image dans le dossier images_articles
            image.save(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', image_filename_uuid))

            #Si l'image a une extension valide, on vérifie, puis on supprime l'ancienne image
            if os.path.exists(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', article.image)):
                #suppression de l'image du article
                os.remove(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', article.image))

            #Puis nous stockons les nouvelles infos dans la bdd
            article.image = image_filename_uuid
            article.code = data['code']
            article.description = data['description']
            article.qty_stock = data['qty_stock']
            article.prix_unitaire = data['prix_unitaire']

            #On prend en compte le nouveau changement
            db.session.commit()

        #On retourne le nouveau changement sous le format définit par articleOut
        return article

    #Si le article n'exite pas, on abort le code 404
    abort(404)

@art.delete('/article/<string:code>')
def delete_article(code):
    try:
        article = Article.query.filter_by(code=code.lower()).first()#Selection du article au travers son code

        #On vérifie si le fichier exist
        if os.path.exists(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', article.image)):
            #suppression de l'image du article
            os.remove(os.path.join(f'{os.getcwd()}/projet/article_/images_articles', article.image))

        #suppression du article    
        article.remove()
        
        return {'message': 'deleted successfully'}
        
    except:
       abort(404)