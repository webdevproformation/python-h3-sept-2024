# Règle LEGB

# Local
# Englobante
# Global
# BuildIn

def affiche():
    x = 1 # locale à la fonction 
    print(x)

affiche()


def calcul():
    y = 2 # variable dans une fonction englobante 
    def soustraction():
        print(y)
    soustraction()

calcul()


z = 3 # la variable z est globale 

def f1():
    def f2():
        print(z)
    f2()

f1()


import builtins # ce module est automatiquement chargé lorsque vous créez un fichier .py 
import pprint 

largeur = 10

def aire():
    largeur = 30
    def distance():
        print(largeur)
    distance()

aire() # ??? largeur 30

""" 
print()
type()
list()
tuple()
set()
...
range() 
"""

#pprint.pp(vars(builtins))


def final():
    def info():
        print(prints)
    info()

# final() # NameError: name 'prints' is not defined. Did you mean: 'pprint'?

# mode de recherche des variables dans Python 
# mode LEGB 
# le système de portées des variables en Python !



var = 10
def f():
    var = 20
    def g():
        return var
    return g()
print(f()) # 20