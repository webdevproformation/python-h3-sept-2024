class Role:
    ADMIN =  2
    REDACTEUR = 1
    USER = 0

class Profil:
    def __init__(self, nom , role):
        self.nom = nom
        self.role = role

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        if type(nom) is str and len(nom)>0:
            self._nom = nom
        else:
            raise ValueError("le nom doit être une string avec au moins un lettre")

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, valeur):
        if valeur in [Role.ADMIN, Role.REDACTEUR, Role.USER]:
            self._role = valeur
        else:
            raise ValueError("le role n'est pas valide")
        
p = Profil("Alain", 1)
print(vars(p))