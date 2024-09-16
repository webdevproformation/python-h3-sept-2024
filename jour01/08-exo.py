titre = "M"
prenom = "John"
nom = "Doe"

# Je m'appelle Monsieur John Doe

# concaténation
solution1 = "Je m'appelle "+ titre + "onsieur "+ prenom + " " + nom 
print(solution1)

# f string
solution2 = f"Je m'appelle {titre}onsieur {prenom} {nom}"
print(solution2)

solution3 = "Je m'appelle {}onsieur {} {}".format(titre, prenom ,nom)
print(solution3)
