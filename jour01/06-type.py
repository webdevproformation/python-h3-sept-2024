# texte = str

texte = "lorem"
texte = 'lorem'

texte = "lorem \
    bonjour"

long_texte = """
texte
multi
ligne
"""

long_texte = '''
texte
multi
ligne
'''

age = 22 # int
distance = 20000 
distance = 20_000 

prix = 12.5 # float

complex = 3+1j # complexe

verif = True # boolean
isFalse = False 

# tableau / variable complexe => 4 types de tableaux dans Python 

list = [1,2,3 ] # mutable ajouter et modifier valeur 
tuple = (1,2,3) # immutable 
set = { 1,2,3 } # une fois créé plus possible de modifier
                # une valeur existante 
                # par contre tu peux ajouter ET retirer 
                

list = [1,2,3 ] # mutable ajouter et modifier clé / valeur 
dictionnaire = { 
    "clé" : 1,
    "autre clé" : "valeur",
    (1,2) : [],
    True : "toto",
    1 : "coucou"
}


""" 
$site = [
    "1" => "valeur",
    "clé2" => 20 ,
    "clé3" => []
] 
"""


"""
créer un nouveau fichier .py
1/ créer la variable test qui va contenir 
le résultat de la comparaison suivante : 255 <= 3
2/ créer la variable inconnu de type texte contenant le mot 'bonjour'
3/ créer la variable voiture qui est un dictionnaire vide
4/ afficher ces trois variables dans le terminal
"""
