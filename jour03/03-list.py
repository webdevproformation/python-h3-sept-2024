# python si vous avez besoin de stocker plusieurs valeurs dans une variable
# tableau 
# par défaut Python met à disposition 4 types de tableaux
# liste => array en PHP array en JS 

tableauVide = []
tableauVide2 = list()

print(tableauVide)
print(tableauVide2)

fleurs = ["rose", "jasmin", "tulipe" , 1 , 1.2, True , []]

# parcourir un tableau 

for i in fleurs:
    print(i)

# parcourir une liste et récupéré l'index et valeur
# enumerate() à utiliser sur des listes 
for index, valeur in enumerate(fleurs):
    print( index )
    print( valeur )

etudiants = ["Alain", "Céline", "Zorro"]
notes =     [20     ,    12   , 12]

for e in zip(etudiants, notes):
    print(e) 
# ('Alain', 20)
# ('Céline', 12)
# ('Zorro', 12)

print(len(etudiants)) # nb d'éléments

# print(help(etudiants)) # quelque soit la variable / class / méthode / fonction => ce sont des objets 

# __xxxx__ => méthode magique 
# __contains__ => méthode magique 
# __add__ => méthode magique 
# __mul__ => méthode magique 
# __len__ => méthode magique 
# count()  => spécifique à ce type 

print( "Zorro" in etudiants ) 

t1 = [1,2,3]
t2 = ["a","b", "c"]
t3 = t1 + t2 
print(t3)
print(t3 * 4)

# CRUD sur les listes

# Create

tableauVide = []
tableauVide.append(1) # ajouter à la fin du tableau 
tableauVide.append((1,2))
tableauVide.append([])
print(tableauVide)
tableauVide.insert(1, "bonjour") # ajouter à l'index 1 le texte bonjour et pousser les autres à droite
print(tableauVide)

# Read 

fruits = ["pomme", "orange", "banane" , "noix de coco"]

print(fruits[1])
# print(fruits[5]) # IndexError: list index out of range

# slicing 
print(fruits[0:3])  # ['pomme', 'orange', 'banane']
print(fruits[1:3])  # ['orange', 'banane']
print(fruits[:3])   # ['pomme', 'orange', 'banane'] # équivalent de [0:3]
print(fruits[2:])   # ["banane" , "noix de coco"] # équivalent de [2:4]
print(fruits[:])   # shallow copy # équivalent de [0:4]

# truc = fruits[:]

print(fruits[::-1]) # reverse
                    # ['noix de coco', 'banane', 'orange', 'pomme']

print(fruits[::2]) # [0:4:2] ["pomme", "banane" ]

# in  => O(n)

# Update

fruits[0] = "poire"

# ["poire", "orange", "banane" , "noix de coco"]
print(fruits) # liste sont mutables

# Delete

fruits.remove("poire") # supprimer par valeur
# ["orange", "banane" , "noix de coco"]
# fruits.remove("poire") # ValueError: list.remove(x): x not in list

del fruits[1]
print(fruits) # ['orange', 'noix de coco']

fruits.clear() # vider 100% des valeurs dans la liste 

tab = [1,4,12,2,5]

# tab.sort() ; tab.reverse()
tab.sort(reverse=True)
print(tab)

etudiants= ["Alain" , "Alain" , "Pierre", "Alain" ]

print(etudiants.count("Alain"))


"""
Créer un nouveau fichier 04-exo.py

créer une fonction dont le nom est palindrome et prenant un paramètre nommé mot

- cette fonction doit retourner True si mot est un palindrome 
- si mot n'est pas un palydrome alors la fonction retourne False

exemples :
print(palindrome("Lol")) # => True
print(palindrome("kayak")) # => True
print(palindrome("laos")) # => False
print(palindrome("Table")) # => False
"""