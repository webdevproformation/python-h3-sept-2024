# tuple => autre type de tableau 
# immutable
# update sur une valeur mise au préalable
# ajout
# delete 

tpl = ( 1,2,3 )
print(tpl)
tpl = tuple([1,2,3])
print(tpl) 

for i in tpl:
    print(i)


for index, value in enumerate(tpl):
    print(index)
    print(value)

# vous ne pouvez pas modifier une valeur existante / ajout / supprimer 

etudiant = ("Alain", 22, "a@yahoo.fr")

listEtudiant = list(etudiant) # conversion vers une list
listEtudiant.append("01/01/2021")

etudiant = tuple(listEtudiant) # conversion vers un tuple
print(etudiant)

""" nom = etudiant[0]
print(nom)
age = etudiant[1]
print(age) """

# unpacking 
nom , _ , _ , dt_naissance = etudiant # ('Alain', 22, 'a@yahoo.fr', '01/01/2021')

print(nom)
print(dt_naissance)

# tuple avec 1 seule valeur

URL = ("http://google.fr",)
PATH = tuple("c:\\doc")

""" print = 10 
print("salut") """

"""
créer un nouveau fichier 07-exo.py

dans ce fichier vous avez une liste de produits

produits = [
    #             prix        qte
    ( 1 , "PS4" , 200, True , 2),
    ( 2 , "PS5" , 600, False  , 3),
    ( 3 , "Nintendo DS" , 400, True , 5 ),
]

- à partir de cette liste de tuple vous devez calculer le total de la commande passée
- pouvez vous changer la valeur de False pour la PS5 en True ? (vous devrez passer par une list pour pouvoir effectuer cette modification)


"""