"""
fonction en javascript

function nom (){

}
"""
# déclare ma fonction
def nom ():
    print("je suis la fonction") 
# exécute la fonction 
nom()

# déclare ma fonction avec deux paramètres
def addition(a, b):
    print(a+b)

# 3 manières d'exécuter la fonction

addition(1,2) # 3

# remettre les noms de paramètres lors de l'exécution de la fonction
addition(a = 2 , b = 4) # 6

# en utilisant cette deuxième syntaxe => vous pouvez mettre les arguments dans 
# l'ordre que vous voulez
addition(b = 10 , a = 15) 

def nettoyageUrl( adresse , encodage = "utf8" , langue = "fr" ):
    return adresse

nettoyageUrl( "http://google.fr" )
nettoyageUrl( "http://google.fr" , langue ="en" ) # très pratique 
nettoyageUrl( "http://google.fr" ,   langue ="en" ) # très pratique 

# je veux créer une fonction qui a un nombre illimité d'arguments
def additionImportante ( *args  ): # équivalent en js ...  spread opérator 
    print(args) # args => type de tableau => tuple ()
    total = 0
    for i in args:
        total += i 
    print(total)

additionImportante(1)
additionImportante(1,2)
additionImportante(1,3,4)
additionImportante(1,3,6,8)
additionImportante(1,3,6,9,10,12)

""" int = 0
tuple2 = (4,5,6)
tuple3 = int + tuple2
print(tuple3) """


def genererPage( **kwarg ): # keyword argments
    print(kwarg)
    # {'titre': 'page 1', 'auteur': 'Victor Hugo', 'dte': '1er janvier'}
    # transforme les arguments envoyés lors de l'exécution du la fonction et les transforme
    # en dictionnaire 

genererPage( titre = "page 1" , auteur = "Victor Hugo" , dte = "1er janvier" )


# Créer un nouveau fichier .py
# 
# 1/ déclarer une fonction aireCercle 
# 
# 2/ cette fonction dispose d'un paramètre rayon
# 
# 3/ cette fonction dispose de deux instructions :
# - déclarer la variable resultat = 3,14 * rayon * rayon
# - afficher dans la console la phrase suivante :
# l'aire d'un cercle de rayon rayon a une aire de resultat
# 
# 4/ exécuter la fonction aireCercle pour le rayon
# 44,5
# 70,43