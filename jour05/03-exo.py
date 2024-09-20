class Formation:

    def __init__(self, nom, sujets):
        self.nom = nom  
        self.sujets = sujets

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        if type(nom) is str and len(nom)> 4:
            self._nom = nom
        else:
            raise ValueError("nom => obligatoire une string de minimum 5 lettres")

    @property
    def sujets(self):
        return self._sujets
    
    @sujets.setter
    def sujets(self, sujets):
        if type(sujets) is list and len(sujets)> 1:
            self._sujets = sujets
        else:
            raise ValueError("sujets => obligatoirement une liste qui contient au moins 2 valeurs")

f1 = Formation("PHP avancé" , ["composer", "namespace" , "symfony"])
# f1.nom = "PHP avancé"
# f1.sujets = ["composer", "namespace" , "symfony"]
print(vars(f1))

try:
    f2 = Formation("PHP", ["composer", "namespace" , "symfony"])
    # f2.nom = "PHP"
except ValueError :
    print ("erreur dans les setter")
except TypeError :
    print ("erreur dans le constructeur")