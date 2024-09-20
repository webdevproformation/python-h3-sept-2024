# rappels

## modules

- 3 types de modules
    
1. module natif => disponible avec le langage Python
    1. sqlite3
    1. debuggage / mise en forme dans le terminal ...
1. module écrit nous même à la main (fichier)
1. module téléchargé depuis internet => `pip install <nom module>`
    1. pypi.org

```py
import nom_fichier

from nom_fichier import fonction, variable, class
```

le fichier est emballé dans un dictionnaire qui prend chaque variable / fonction / class 
clé d'un dictionnaire => espace de nom /espace de nommage / namespace

```py
import nom_fichier

from nom_fichier import fonction as nom_modifie_fonction
```

## POO

```py
# créer des class

class A:
    cote : 10
    def surface(self)
        return self.cote * 4

# instance de class 
carre = A()
carre.surface()

# méthode magique => initialisateur (constructeur)

class B:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

b = B(10, 20)
```

```py
class A:
    prop = "bonjour"

a = A()

print(vars(A)) # class    => { prop = "bonjour"  }
print(vars(a)) # instance => {}

a.prop
# => arbre d'héritage entre instance et la class
```


- <https://medium.com/analytics-vidhya/simulating-the-solar-system-with-under-100-lines-of-python-code-5c53b3039fc6>