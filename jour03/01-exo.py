etudiants = [
    { "nom" : "Alain" , "note" : 15 } , 
    { "nom" : "Benjamin" , "note" : 10 } , 
    { "nom" : "Céline" , "note" : 18 } , 
    { "nom" : "Céline" , "note" : 9 } , 
    { "nom" : "Alain" , "note" : 12 } , 
    { "nom" : "Alain" , "note" : 18 } , 
]

listeEtudiant = []

for i in etudiants:
    if not i["nom"] in listeEtudiant :
        listeEtudiant.append(i["nom"])
resultat = []

for nom in listeEtudiant:
    total = 0
    compteur = 0
    for etudiant in etudiants:
        if nom == etudiant["nom"]:
            total += etudiant["note"]
            compteur += 1
    moyenne = total / compteur
    resultat.append({ "nom" : nom , "moyenne" : moyenne })

print(resultat)
        