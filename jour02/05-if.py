if 2 == 2 :
    print("la condition est vraie")

age = 30

if age < 10 :
    print("vous êtes mineur")
elif age < 70 : # pas else if()
    print("vous êtes majeur")
elif age < 100 :
    print("vous êtes retraité")
else :
    print("chiffre invalide")

# match => ressemble à switch case
# mais il n'y a pas de switch en Python 

"""
if ternaire 

en PHP 
condition ? "vrai" : "faux"

en Python la syntaxe pour les if ternaire

"vrai" if condition else "faux"

"""

isAdmin = "il est admin" if 2 > 10 else "il n'est pas admin"
print(isAdmin)

"""
Falsy => valeur qui sont transformés en false automatiquement si elles sont
utilisée dans une condition

""
0
[]
set()
{}
0.0
None
"""

couleur = 0 # Falsy

if couleur : # "" => transforme en False 
    print("voici la couleur")


# créer un nouveau fichier py contenant une variable ville
# initialiser la variable ville = "Marseille"

# si ville a pour valeur Paris 
# alors afficher dans la console "vous habitez à Paris"

# si ville a pour valeur Boulogne ou Clamart ou Montrouge 
# alors afficher dans la console "vous habitez dans le 92"

# si ville a pour valeur Saint-Denis ou Aubervilliers ou Pantin
#  alors afficher dans la console "vous habitez dans le 93"

# sinon
# afficher dans la console "vous habitez hors d'Ile de France"
