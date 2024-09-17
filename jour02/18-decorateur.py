
# le concept est le même en typescript 

""" def f1():
    pass 

print(f1) # <function f1 at 0x000001E57CA2A3E0>
          # f1 est objet de type fonction  """

""" def f2():
    def traitement():
        print("start")
    return traitement # je retourne la fonction à l'intérieur de f2 

f2() # il ne se passe rien car la fonction retourne un objet de type fonction 
f2()() # il faut exécuter une deuxieme fois pour exécuter traitement qui est dans f2
 """
def f3():
    def traitement():
        print("traitement")
    return traitement

variable = f3() # stocker la ref de la fonction traitement DANS une variable que je vais 
variable()      # exécuter

# f3()()

# fonction design pattern décorateur 
def timer(f):
    def wrapper():
        print("start timer")
        f()
        print("fin timer")
    return wrapper 

@timer # décorateur => décorer les fonctiond direBonjour
def direBonjour():
    print("bonjour")
    
direBonjour() # fonction qui s'exécute sur une autre fonction 

"""
start timer
bonjour
fin timer
"""


def mailAdmin(f):
    def wrapper():
        f()
        print("envoyer email admin")
    return wrapper

def mailRemerciement(f):
    def wrapper():
        f()
        print("envoyer au user inscrit")
    return wrapper

@mailAdmin     # fonction décoratrice etendre le comportement de la fonction insertEnBdd
               # class => @property (setter et getter en PHP Java)
@mailRemerciement
def insertEnBdd():
    print("insert")

insertEnBdd()

# cas pratique créer le fichier 19-exo.py
# dans ce fichier créer deux fonctions décoratrices
# bonjour qui va afficher le texte bonjour 
# identifiant cette deuxième fonction => vous demande de saisir dans le terminal un id => input()

# si la valeur saisie == "10" alors exécuter la fonction login
# 
# afficher le texte "bienvenue dans l'espace de gestion"
