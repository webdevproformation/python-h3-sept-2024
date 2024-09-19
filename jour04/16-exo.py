class Personnage:
    def __init__(self, nom,vie = 100):
        self.nom = nom
        self.vie = vie
    def frapper(self , personnage):
        personnage.vie -= 10

magicien = Personnage("Merlin")
guerrier = Personnage("Alexandre le Grand")

guerrier.frapper(magicien)
guerrier.frapper(magicien)

print(magicien.vie) # 80
