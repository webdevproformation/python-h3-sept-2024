# str chiffre (int float complex) bool
# tableaux / data structure
# list / tuple / set / dictionnaire

"""
en js 
créer une variable et je dirais plus tard mon code sa valeur (et son type) 
null / undefined 

en Python pas possible 

"""

def traitement():
    print("je suis un traitement")

resultat = traitement() # None
# type qui apparait lorsque l'on execute une fonction qui ne return rien 

print(resultat) 
print(type(resultat)) # <class 'NoneType'>

a = 10 

print(type(a)) # <class 'int'>

# possible d'ajouter des annotations 

def calcul(a : float, b : int) -> float :
    """
    effectuer une addition
    """
    return a + b

# calcul("10px", [1,2])
print(help(calcul))
# print(help(type))

"""
créer un nouveau fichier 13-exo.py

dans ce fichier vous allez créer une fonction qui permet de 
convertir une temperature de Celsus => Farenheit
(voir la formule dans le fichier ci joint)
https://github.com/webdevproformation/python-h3-sept-2024/blob/main/jour02/12-exercise-11.png
"""