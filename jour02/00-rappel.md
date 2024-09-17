# rappel 

=> Python 

## langage interprété et compilé 

=> interprété (PHP) => script.php => passer un logiciel (interpréteur)
exécuter ligne par ligne

=> compilé (C)   => script.c => compiler (traduire en binaire) => exécuter 

.py  
.pyc (compilé)

## IDE 

=> PyCharm
=> Visual Studio Code + extension
=> SublimText (en Python)

# nom => Monthy Python

# philosophie du Python 

=> beau code 
=> beaucoup de règle / convention pour écrire du code 
=> 79 caractères par ligne 
=> 1 ligne de code écrire 1 fois / lire plusieurs fois 

# variables et les types de valeurs que l'on peut stocker

```py
# chiffre (int / float / complex)

age = 10
duree = 1_000
prix = 12.5
coordonnee = 12 + 3j

# texte

t = "lorem"
t = 'lorem'

html = """
<h1>hello</h1>
<p>coucou</p>
"""

# logique 

test1 = True 
test2 = False

# data structure / tableau => 1 variable plusieurs valeurs 
# 4 variants


# dictionnaire (ressemble beaucoup objet en js)

etudiant = {
    "nom" : "Alain",
    "age" : 22,
    "role" : True
}

# liste => (ressemble beaucou aux array en js)

fleurs = [ "jasmin" , "rose" , "lilas" ] # mutable 

# tuple 

fleurs = ( "jasmin" , "rose" , "lilas" ) # immutable => recherche / 

# set 

fleurs = { "jasmin" , "rose" , "lilas" } # mutable (ajouter / supprimer) / pas de double // pas possible de modifier une valeur existante 
# performance 
```


créer un nouveau fichier 01-exo.py

dans ce fichier vous avez une liste 
fleurs = [ "jasmin" , "rose" , "lilas" ]
prix = 12.5

vous devez écrire dans le terminal le texte suivant 

j'ai acheté des jasmins et des roses pour 12.5 €

rappel concaténation
 +
f"  {}"
"{} {}".format()
