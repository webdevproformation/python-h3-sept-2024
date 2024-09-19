
prix = 12.5

def prixTTC(prix):
    return prix * 1.1

class A:
    pass 

# automatiquement Python va les stocker dans un dictionnaire si on n'a besoin de les utiliser dans un autre fichier 
# espace de nom / espace de nommage / namespace 
"""
{
    "prix" : 12.5,
    "prixTTC" : function(....){ .... },
    "A" : class ...
}
"""

print(__name__) # si je me mets dans l'autre fichier (import)
                # exécuter le code 
                # __name__ == "lib"


if __name__ == "__main__": # si tu exécutes le fichier lib.js 
    verif = prixTTC(10)
    if verif != 12 :
        raise ValueError("la fonction de calcul de TVA n'est pas conforme")