class A:
    def __init__(self, largeur, hauteur): # __init__() méthode qui va initialiser 
                                        # donner des valeurs aux propriétés de l'instance
        self.largeur = largeur
        self.hauteur = hauteur

    def calculSurface(self):
        return self.largeur * self.hauteur
    
rectangle = A(10, 20)
print(rectangle.calculSurface())

"""
# créer un nouveau fichier 16-exo.py
# créer une class Personnage 
# contenir deux propriétés qui vont être initialisée via un constructeur 
# nom  = ""
# vie = 100

# méthode frapper( $personnage  )
# le fait de frapper va réduire de - 10 la vie de l'autre personnage 

# créer deux personnages 
# magicien  nom "Merlin"
# guerrier nom "Alexandre le Grand"

# le guerrier va frapper 2 fois le magicien => la vie du magicien doit passer de 100 à 80 

vérifier que la vie du magicien a bien réduit de -20 

"""