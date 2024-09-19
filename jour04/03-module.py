# module 

# python fichier = module 


# module créer vous même
# créer un fichier lib.py === le nom de votre module 

""" import lib

print(lib.prix) ## 12.5
print(lib.A)  ## <class 'lib.A'>

print(lib.__dict__) # affiche moi toutes les clé - valeurs disponibles dans la variable lib 
## toutes les variables / fonction / class écrites dans le fichier "lib.py" MAIS aussi les fonctions builtins  """

from lib import prix  as prix_lib

# prix = 50 

# print(prix_lib) # 12.5


print(__name__) # variable générée automatiquement par Python
                # "__main__" 

# module buildins (livré par défaut par Python)
# module téléchargé depuis internet => pypi.org