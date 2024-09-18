# dictionnaire (vous avez en même temps => espace de nommage)

# si vous venez de PHP => namespace 

# tableau ayant plusieurs valeurs 
# chiffre pour trouver la valeur MAIS une clé (nom)

organisation = {
    "id" : 1,
    "nom" : "H3",   
    "adresse" : "75 rue de Paris",
    (1,2) : "clé en plus", 
    1 : "hello",
    # [1,2] : "un texte"
}

for cle in organisation:
    print(cle)
    print(organisation[cle])

print(organisation.get("id")) # 1
print(organisation.get("dt_creation")) # None
print(organisation.get("dt_creation" , "info inconnue")) # texte par défaut "info inconnue" si la clé n'existe pas 

print(organisation.values()) # dict_values([1, 'H3', '75 rue de Paris', 'hello', 'clé en plus'])
print(organisation.keys())  # dict_keys(['id', 'nom', 'adresse', 1, (1, 2)])

print(organisation.items()) # dict_items([('id', 1), ('nom', 'H3'), ('adresse', '75 rue de Paris'), (1, 'hello'), ((1, 2), 'clé en plus')])

# modifier une valeur existante

organisation["id"] = 10 

# modifier le dictionnaire en ajoutant une clé : valeur

organisation["isOpen"] = True

print(organisation)

# supprimer une clé : valeur existante

del organisation["adresse"]

print(organisation)

# recherche de clé dans un dictionnaire

print( "id" in organisation) # True


a = 10 

## 