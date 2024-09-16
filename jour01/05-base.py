# commentaire monoligne
"""
commentaire 
avec saut de ligne
...
// 
/*
 ne fonctionnent pas 
*/
"""

prenom = "valeur"
nom = "autre valeur"

# en python 1 ligne = 1 instruction 

# il est possible d'avoir plusieurs instructions sur une ligne 
# pour écrire plusieurs inscruction sur la même ligne 
age = 20 ; largeur = 40  

list = [0,5,2]
list.sort() ; list.reverse()

# en pythonon n'utilise pas les { } et les ;
# avec le même sens que javascript ou en PHP 
# les indentations vous déterminer les blocs de codes 

def traitement() :
    a = 1
    b = 2
    return a + b + \
           59

# dans la mesure du possible => contient au maximum 79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères   79 caractères  

variable = 30

if 2 > 1 and \
   variable > 10 or  \
   30 < 10 :
    pass

# une ligne de code => écrit 1 seule 
# lire plusieurs fois 

# variable en python => snake_case 
prenom_auteur : str = "Victor Hugo"

def camelCase(a : int, b : str) -> str: # camelCase
    """
    présentation de la manière de créer une fonction en python
    docstring 
    """
    pass

class ArbreAbstract : # PascalCase 
    pass 

prenom_auteur = 10

camelCase(10 , []) # annotation => aide pour le développeur / bloquant 

toto : int = 10 

## 

## variable en javascript 
# var a = 2
# let a = 2
## constante en javascript 
# const a = 2

## variable en PHP
# $a = 2 ;
## constante en PHP
# define("A", 2) ;

# en Python le concept de constante n'existe pas 
# convention d'écriture  => TOUT EN MAJUSCULE 

URL_SITE = "http://google.fr"
URL_SITE = 10 # rien qui empêche le fait de modifier la valeur stockée dans cette VARIABLE

# affectation multiple 

premier = 10 
deuxieme = 20 

## affectation multiple => unpacking 
premier , deuxieme = 10 , 20

# cas pratique 

""" 
nom de variable 
Variable
Nom de Variable
123Nom_De_Variable
Nom_De_Variable
nom_de_variable
toto@mailcity.com
nom_de_variable_123
Nom-de-variable
_function
function 
"""

# quelle nom de variable est valide / invalide => si invalide pourquoi ??