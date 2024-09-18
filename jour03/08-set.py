# set 

set1 = { "valeur" }
print(set1)

set2 = set(["autre valeur"])
print(set2)

# update impossible
# insert  possible 
# delete  possible 

etudiants = { "Alain" , "Pierre" , "Alain" }
print(etudiants) # {'Pierre', 'Alain' }


etudiants = [
    { "nom" : "Alain" , "note" : 15 } , 
    { "nom" : "Benjamin" , "note" : 10 } , 
    { "nom" : "Céline" , "note" : 18 } , 
    { "nom" : "Céline" , "note" : 9 } , 
    { "nom" : "Alain" , "note" : 12 } , 
    { "nom" : "Alain" , "note" : 18 } , 
]

""" listeEtudiant = []

for i in etudiants:
    if not i["nom"] in listeEtudiant :
        listeEtudiant.append(i["nom"])
resultat = [] """

setEtudiant = set() # erreur classique {} pour un set vide 

for i in etudiants:
    setEtudiant.add(i["nom"])

setEtudiant.add("Marie")
setEtudiant.add("Marie")
setEtudiant.add("Marie")
setEtudiant.add("Marie")

print(setEtudiant)

for i in setEtudiant: # attention les set retourne des valeurs 
                      # de manière non ordonnées dans un loop
    print(i)

# set par d'ordre (dans les prints de boucle) et pas de doublon (lorsque l'on add)

# print(setEtudiant[1]) # TypeError: 'set' object is not subscriptable


s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}


s4 = s1.union(s3) # {1, 2, 3, 4, 5}
print(s4)

s5 = s1.intersection(s3)
print(s5) # {3}

s6 = s1.symmetric_difference(s3)
print(s6)  # {1, 2, 4, 5}

## cas pratique 

# créer un nouveau fichier .py
## vous avez 3 listes 

employees = ['Corey', 'Jim' , 'Steven' , 'April' , 'Judy' , 'Jenn' , 'John' , 'Jane'] 
gym_members = ['April', 'John' , 'Corey']
developers = ['Judy' , 'Corey' , 'Steven' , 'Jane' , 'April']

set_employees = set(employees)
set_gym_members = set(gym_members)
set_developers = set(developers)

dev_and_gym = set_developers.intersection(set_gym_members)
print(dev_and_gym)

# quels sont les utilisateurs qui sont developpers et sont inscrits au club de gym

# quels sont les utilisateurs qui ne sont ni developpers ni inscrits au club de gym

# est ce que Steven est inscrit au club de gym ?