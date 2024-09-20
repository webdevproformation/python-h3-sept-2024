# setter getter

# encapsulation 
# le fait de stocker du code dans une class
# le fait de stocker propriétés dans la class => va les protéger 

# mettre en place un système qui va permettre de faire en sorte QUE Python vérifie que les valeurs passées à la propriété sont VALIDES

class Personne :
    def getAge(self):
        print("utilisation du getter")
        return f"{self._age} ans" 
    def setAge(self, valeur):
        print("utilisation du setter")
        if valeur > 0:
            self._age = valeur
    age = property(getAge , setAge)

p = Personne()
p.age = 22 # vous êtes en train d'exécuter la méthode setAge() de la class

print(p.age) 
"""
utilisation du getter
22
"""

class Etudiant :

    @property # getter
    def nom(self):
        print("utilisation du getter avec decorateur")
        return f"{self.__nom}".upper() 
    
    @nom.setter # setter
    def nom(self, valeur):
        print("utilisation du setter avec decorateur")
        if len(valeur) > 0:
            self.__nom = valeur

    @property # getter
    def age(self):
        print("utilisation du getter avec decorateur")
        return f"{self.__age} ans" 
    
    @age.setter # setter
    def age(self, valeur):
        print("utilisation du setter avec decorateur")
        if valeur > 0:
            self.__age = valeur

e = Etudiant()
e.age = 44
e.nom = "Zorro"
e._Etudiant__nom = "Pierro"
print(vars(e))


"""
# créer un nouveau fichier 03-exo.py
# créer une class Formation
# 2 propriétés nom / sujets

# créer les setter et getter pour ces deux propriétés
# nom => obligatoire une string de minimum 5 lettres
# sujets => obligatoirement une liste qui contient au moins 2 valeurs 

# créer des  setter et getter qui vont garantir que les valeurs associées à ces propriétés sont conformes à vos attentes 

# Bonus : mettre des messages d'erreur si ce n'est pas conforme ! 

"""