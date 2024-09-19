# rappel 

- data structure => tableau

## liste

- mutable (modifier existant / ajouter / supprimer ) une liste
- doublon 
- boucle => les valeurs retournées sont dans l'ordre dans lesquels elles ont été ajoutées

```py
liste = []
liste = list()
# attention ne pas créer de variable qui ont pour non list

=> in "valeur" in liste
=> + possible de concaténer des listes avec l'opérateur +
=> * oui 

=> append() => ajouter une nouvelle valeur à la liste
=> insert( index , "valeur")

liste = [1,2,3,4,5,6]

liste[3:] # récupérer une partie de la liste à partir de l'élement qui a l'index (position) 3 jusqu' rien (par défaut ) le dernier élément 

[1,3,5]
liste[0:6:2]
liste[::2]

```

## comprehension de liste

```py 
liste = [1,2,3,4,5,6]
 # avoir un tableau qui contient uniquement les valeurs > 3 de liste

resultat = []
for i in liste :
    if i > 3 :
        resultat.append(i)

resultat = [ i for i in liste if i > 3  ]
```

## tuple

- immutable => impossible de modifier une valeur existante / pas possible d'ajouter des valeurs / supprimer des valeurs
- possible d'avoir des doublons
- très rapide pour les recherches

```py
liste = [1,2,3,4,5,6]
tuple1 = tuple(liste)
in

# Read 

tuple1[0]
tuple1[1:]

# si vous avez besoin de modifier un tuple => il faut le transformer en list

tpl1 = (1,2)
tmp_list = list(tpl1)
tmp_list.append(3)
tpl1 = tuple(tmp_list)

# ATTENTION 

a = (1) # ce n'est pas un tuple
a = (1,) # ça oui 

```

## set

- pas possible de modifier une valeur existante
- possible d'ajouter / supprimer des valeurs 
- non pas de doublon possible 
- attention un set ne retourne pas les valeurs dans l'ordre dans lequel vous les avez insérés

```py
# pas possible de faire de Read  / update 
print(etudiants[0])  # TypeError: 'set' object is not subscriptable

# comparer des sets les uns avec les autres 

# https://webdevpro.net/toutes-les-jointures-sql/


```

## dictionnaire

- mutable ajouter / modifier / supprimer une valeur existante
- pas possible d'avoir deux clés avec le même nom


```py

etudiant = {
    "clé" : "valeur",
    1     : 20,
    True  : 20,
    # [1] : 12
    (1,2) : "heure"  
}

etudiant[(1,2)]
etudiant.get((1,2)) # retourne la valeur si elle existe sinon None
etudiant.get((1,2), "NaN") # retourne la valeur si elle existe sinon "NaN"

```

Créer un nouveau fichier 01-exo.py

- écrire une fonction nommée anagram qui vérifie si deux chaînes fournies sont des anagrammes l'une de l'autre; 
- la casse des lettres ne devrait pas avoir d’importance.
- En outre, ne considérez que les caractères, pas les espaces ou la ponctuation 


Voici quelques exemples :
anagram('finder', 'Friend')  => True
anagram('hello', 'bye') => False
anagram('Mary', 'Army') => True
anagram('nectar', 'carnet ') => True

