# méthode bound


# en Python Tout est objet
# class
# instance est un objet
# méthode de class sont des objets

class A:
    def test(self , info):
        return "je suis la méthode self"
    
a = A()

print(A)      # <class '__main__.A'>
print(A.test) # <function A.test at 0x000002339C9FE160>
print(a)      # <__main__.A object at 0x000002339C9D6C30>
print(a.test) # <bound method A.test of <__main__.A object at 0x000002C3A3A46C90>>
              # a.test => bound méthode => méthode objet associé à une instance 

a.test("bonjour") # automatique Python va passer comme premier argument à la méthode test l'instance

A.test(a, "bonjour") # cette ligne est équivalente écrire a.test()
          # ce mécanisme est AUTOMATIQUE 

# expliquer la signature des méthodes dans la class => le premier paramètre est l'instance !! 

print(vars(a)) # {}
print(vars(A))

"""
{
    '__module__': '__main__', 
    'test': <function A.test at 0x000001A2F300E160>, 
    '__dict__': <attribute '__dict__' of 'A' objects>, 
    '__weakref__': <attribute '__weakref__' of 'A' objects>, 
    '__doc__': None
}
"""

