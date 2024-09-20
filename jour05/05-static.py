# méthode / propriété static 

class A:
    def toto(self):
        return "toto"
    
a = A() # créer un objet
a.toto() # PUIS ON peut utiliser la méthode 

class B:
    @staticmethod
    def titi():
        return "test"
    
print(B.titi())

class Page :
    Url = "https://domaine.fr"

    def __init__(self, nom):
        self.nom = nom

    @staticmethod
    def genererUrl(param):
        return f"{Page.Url}/{param}"
    
print(Page.genererUrl("nous-contacter"))

# cas pratique 

# créer un nouveau fichier 06-exo.py

# class Role 
# 3 constantes (propriété static)
# ADMIN =>  2
# REDACTEUR => 1
# USER => 0

# class Profil 
# propriété nom string
# propriété rôle ne peuvent avoir QUE les rôles définis dans la class Rôle
# créer les setter et getter nécessaires pour cette class
