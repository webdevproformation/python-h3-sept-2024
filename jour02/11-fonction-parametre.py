# variable globale
x = 1

# fonction qui réalise des traitements
def augmenter(x):
    x = 2

# exécuter la fonction
augmenter(x)
# afficher la valeur de x 
print(x) # ?? 1 le x dans la fonction n'a pas d'impacte sur le x global


liste = ["a", "b", "c"]

def ajouterLettre(liste):
    liste.append("d")

ajouterLettre(liste) # adresse mémoire passage par référence 
print(liste) # ["a", "b", "c" , "d"] 
# la fonction impacte la valeur stockée dans une variable globale 


set = {"a", "b", "c"}

def modifierSet( set ):
    set.add("valeur en +")

modifierSet( set )
print(set)
    