# boucle for

"""
en js 
for(let i = 0 ; i < 10 ; i++){
}
"""

for i in range(0,10): # commence à 0 et fin 9 
    pass

"""
en js 
for(let i = 0 ; i < 10 ; i +=2){
}
"""

for i in range(0,10 , 2): # commence à 0 et fin 9 et augment de +2 
    pass

"""
en js 
for(let i = 10 ; i > 0 ; i--){
}
"""

for i in range(10,0 , -1): # commence à 10 et fin 1 et diminue de -1 
    print(i)

# for else 

for i in range(1,5):
    print("je suis dans la boucle" + str(i))
else :
    print("fin de la boucle")

# for else 

for i in range(1,5):
    if i == 6 :
        print("je suis dans la boucle" + str(i))
else : # else s'exécuter à la fin de boucle 
    print("élément introuvable")


for i in range(1,5):
    if i == 2 :
        print("je suis dans la boucle" + str(i))
        break # 
else :
    print("élément introuvable")

"""
for(let i = 10 ; i > 0 ; i--){

    if(i == 1){ 
    }
}
"""


# Créer un nouveau fichier .py

# afficher dans la console des nombres de 1 à n, où n est un nombre entier
# si le chiffre est un multiple de 3, afficher le mot fizz à la place du chiffre
# si le chiffre est un multiple de 5, afficher dans la console le buzz à la place du chiffre
# si le chiffre est une multiple de 3 et 5 afficher dans la console le mot fizzbuzz à la place du chiffre

# par exemple si n = 15 alors voici ce qui doit être affiché dans la console du navigateur

# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
