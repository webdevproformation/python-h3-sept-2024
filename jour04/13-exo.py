class Livre:
    auteur = "Victor Hugo"
    nom = "Les Misérables"
    prix = 20
    devise = "euros"
    anneeParution = 1862

    def synopsis(self):
        return f"{self.auteur} a publié {self.nom} en {self.anneeParution}"
    
    def vente(self):
        return f"Pour acheter, {self.nom} il faudra débourser {self.prix} euros"
    
l = Livre()
l.auteur = "George Sand"

print(l.synopsis())
print(l.vente())   

"""
Victor Hugo a publié Les Misérables en 1862
Pour acheter, Les Misérables il faudra débourser 20 euros
"""