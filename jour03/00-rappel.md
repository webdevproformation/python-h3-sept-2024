# rappel d'hier

=> nous avons vu les structures 


# chiffre

```py

chiffre = 10

chiffre++ # n'existe pas en python

chiffre += 1

```

# condition

```py

== # le === n'existe pas en Python 
== # équivant au === verification en type et en valeur 

&& => and

||  => or

!   => not 


if condition :
    pass 
    

if condition1 :
    pass
elif condition2:
    pass
else:
    pass

"vrai" if condition else "false"

```

# boucle 

```py

for i in range(0, 10, 2):
    pass 

for i in range(0, 10, 2):
    pass 
else :
    # exécuter un traitement à la fin de la boucle 
    pass 

for i in range(0, 10, 2):
    if condition :
        break 
    pass 
else :
    # exécuter un traitement à la fin de la boucle sauf si il y a un break
    pass 

i = 0

while i < 10
    # traitements
    i += 2

```

# fonction

```py

def traitement():
    pass

traitement()

def traitement2(a , b):
    pass

traitement2(1 , 2)
traitement2(a = 1 ,b = 2)
traitement2(b = 2 , a = 1 )

def traitement3( *args ):
    args[0]
    pass 

traitement3(1 )
traitement3(1 ,2)
traitement3(1 ,2,3)  # args = (1,2,3) tuple
traitement3(1 ,2,3,4) # args = (1,2,3,4)

def traitement4( **kwargs ): # keyword arguments
    pass

traitement4( a = 1 )
traitement4( a = 1 , b = 2 )   # kwargs => { "a" : 1 , "b" : 2 }
traitement4( a = 1 , b = 2 , c = 3 )
```

# portée des variables 

LEGB
Local
Englobant
Global
BuildIn

```py
import buildins # print range # variable build ins 

x = 10 # variable globale

def calcul():
    y = 50 # variable englobante
    def traitement():
        z = 12 # variable locale
        x = 33
        print(x)
        print(y)
        print(z)
        print(toto)

```

```php

$x = 2

function traitement(){
    global $x ; 
    echo $x;
}
```

# fonction lambda

```py

# ne contient QUE 1 seul traitement ECRIT en 1 ligne

def addition(a,b):
    return a + b

addition = lambda a,b : a + b 

def convertCtoF(temperatureCelsus : float) -> float:
    return  temperatureCelsus / 5 * 9 + 32

convertCtoF = lambda temperatureCelsus : temperatureCelsus / 5 * 9 + 32
```

# décorateur (disponible aussi en Typescript / Angular)

- réutiliser des fonctions 
- etendre une autre fonction 

```py

def insertBdd(f):
    def wrapper():
        print("insertion en base de données")
        f()
    return wrapper 

@insertBdd
def connexion():
    print("vous êtes connecté")

connexion()
```

créer le fichier 01-exo.py

ce fichier contient une liste de dictionnaire : etudiants 

etudiants = [
    { "nom" : "Alain" , "note" : 15 } , 
    { "nom" : "Benjamin" , "note" : 10 } , 
    { "nom" : "Céline" , "note" : 18 } , 
    { "nom" : "Céline" , "note" : 9 } , 
    { "nom" : "Alain" , "note" : 12 } , 
    { "nom" : "Alain" , "note" : 18 } , 
]

// pouvez vous afficher dans le terminal : 
[ 
    {"nom" : "Alain" , "moyenne" : ? }
    {"nom" : "Benjamin" , "moyenne" : ? }
    {"nom" : "Céline" , "moyenne" :  ? }
]
