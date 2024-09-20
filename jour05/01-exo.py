class Maison:
    def __init__(self, adresse = "", is_vendu = False):
        self.adresse = adresse
        self.is_vendu = is_vendu

class Personne:
    def __init__(self,valeur = ""):
        self.__nom = valeur

    def acheter(self , instance_maison):
        instance_maison.is_vendu = True

m = Maison("75 rue de Paris 75000 Paris")

print(vars(m))

p = Personne("Alain")

p.acheter(m) # la personne va pouvoir acheter la maison
print(vars(m))

print(m.is_vendu) # True