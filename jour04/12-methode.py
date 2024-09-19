class A :
    # attention en Python on n'a pas le début de la class
    # avec toutes les propriétés public private protected 
    # écrite au début de la définition de la class 

    def calcul(self, a, b):
        self.total = a + b
    
a = A()       # créer instance
a.calcul(1, 2) # exécute une méthode créer une propriété d'instance

print(vars(A)) 
print(vars(a))

"""
{'__module__': '__main__', 'calcul': <function A.calcul at 0x000002647B92E160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{'total': 3}
la propriété total n'est disponible QUE dans l'instance elle n'existe pas dans la class 
"""