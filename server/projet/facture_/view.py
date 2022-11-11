from apiflask import APIBlueprint
from ..model import Facture
fac = APIBlueprint('factures', __name__, tag={
      'name': 'Factures', 'description':'Espace Factures: vous pouvez rechercher une facture par son id'
    })

#toutes les factures  
@fac.get('/factures')
def all_invoices():
    pass

#obtenir les infos d'une facture par son numéro
@fac.get('/facture/<int:num>')
def get_invoice_by_num(num):
    pass

#créer une facture
@fac.post('/facture')
def create_facture():
    pass