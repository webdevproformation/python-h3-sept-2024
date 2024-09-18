etudiants = [
    { "nom" : "Alain" , "note" : 15 } , 
    { "nom" : "Benjamin" , "note" : 10 } , 
    { "nom" : "Céline" , "note" : 18 } , 
    { "nom" : "Céline" , "note" : 9 } , 
    { "nom" : "Alain" , "note" : 12 } , 
    { "nom" : "Alain" , "note" : 18 } , 
]

def moyenne(name):
    """
    permet de calculer la note par nom d'étudiant
    pour un étudiant il y a un tableau qui va contenir autant de notes
    qu'il a reçues
    """
    notes = []
    total = 0
    for student in etudiants:
        if student['nom'] == name:
            notes.append(student['note'])

    for note in notes:
        total += note

    return total / len(notes)

def displayMoyenne(*args):
    """
    fonction qui va générer le tableau final à afficher dans 
    le terminal
    """
    moyenne_students = []
    for nomEtudiant in args:
        dict = {}
        dict["nom"] = nomEtudiant
        dict["moyenne"] = moyenne(nomEtudiant) # utilisation de la fonction moyenne
        moyenne_students.append(dict)
    print( moyenne_students)

displayMoyenne("Alain", "Céline", "Benjamin")