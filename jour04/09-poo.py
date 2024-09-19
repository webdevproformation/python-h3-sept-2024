# https://formation.webdevpro.net/python-poo 
# login : python
# password : poo

# en Python TOUT EST OBJET
# fichier => objet
# variable quelquesoit le type objet
# fonction objet
# class objet
# méthode des class / propriété des class sont des objets 

# type  => class 

a = 2 

""" a = new Int(2) """

class AlphabetFrancais : # PascalCase première lettre en majuscule

    nombre = 26

    def combienDeLettres( self ): # self correspond à l'instance de la 
                                  # class
                                  # $this en PHP 
        return self.nombre
     
    def ajouterLettre(self, lettre): # si vous avez des paramètres en +
                                    # mettre après le self 
                                    # self est OBLIGATOIRE même si 
                                    # on n'utilise pas self dans la méthode
        print(lettre)

# à partir de la class AlphabetFrancais on peur créer des instances (objets)

a1 = AlphabetFrancais() # il n'y a pas le mot clé new 
                        # exécuter la class comme vous exécuter une fonction

print(a1.nombre)

print(a1.combienDeLettres())

a1.ajouterLettre("blabla") # "blabla" va remplir la propriété lettre de la méthode

"""
# cas pratique :
# créer un fichier 10-exo.py

# créer une class Etudiant 
# contient 5 propriétés publiques
# nom = "Alain"
# age = 40
# adresse = un dictionnaire de 3 valeurs 
#           rue : 75 rue de Paris
#           ville : paris
#           cp : 75000
# isAdmin = faux
# competences un tableau de 4 valeurs => PHP / JS / NodeJS / Symfony / React

# à partir de cette class créer un objet etudiant1 
# afficher le contenu de cet objet via le module pprint
# et la fonction native vars()

"""