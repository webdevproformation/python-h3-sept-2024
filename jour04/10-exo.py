import pprint

class Etudiant:
    nom = "Alain"
    age = 40
    adresse = {
        "rue": "75 rue de Paris",
        "ville": "Paris",
        "cp" : 75000
    }
    isAdmin = False
    competences = {"PHP" , "JS" , "NodeJS" , "Symfony" , "React"}


etudiant1 = Etudiant()

pprint.pp(etudiant1.nom)
pprint.pp(etudiant1) # <__main__.Etudiant object at 0x00000148214D7EF0>
pprint.pp(etudiant1.__dict__) # {}
pprint.pp(vars(etudiant1))    # {}
pprint.pp(etudiant1.age) # hors on a bien la valeur 40 qui est retournée

pprint.pp(Etudiant) # <class '__main__.Etudiant'>
pprint.pp(Etudiant.__dict__)
pprint.pp(vars(Etudiant))

"""
{'__module__': '__main__', 'nom': 'Alain', 'age': 40, 'adresse': {'rue': '75 rue de Paris', 'ville': 'Paris', 'cp': 75000}, 'isAdmin': False, 'competences': {'PHP', 'JS', 'React', 'NodeJS', 'Symfony'}, '__dict__': <attribute '__dict__' of 'Etudiant' objects>, '__weakref__': <attribute '__weakref__' of 'Etudiant' objects>, '__doc__': None}
"""

"""
noter bien que lorsque l'on crée une instance les propriétés de class 
age 
competence ...
NE SONT PAS dans l'instance par défaut 
Python va créer une relation d'héritage entre class (objet) et l'instance qui est objet aussi 

etudiant1.age => chercher dans l'instance est qu'il y a une propriété age existe ?? 
si elle n'existe pas => il va chercher dans la class qui a permis de créer l'objet => age qui existe ??? si c'est bon => retourne 

"""

class A:
    age = 20

    def setAge(self, valeur):
        self.age = valeur 

a = A()
print(vars(A)) # class
print(vars(a)) # instance
print(a.age) # 20

"""
{'__module__': '__main__', 'age': 20, 'setAge': <function A.setAge at 0x000002EFA4A5E160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{}
20
"""

a.setAge(30)  # modifier l'instance
print(vars(A))
print(vars(a))
print(a.age) # 30

"""
{'__module__': '__main__', 'age': 20, 'setAge': <function A.setAge at 0x000002EFA4A5E160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{'age': 30}
30

=> Arbre d'héritage entre une instance et sa class
"""