# les fonctions lambda

def calcul (a, b, c):
    return a + b + c

traitement = lambda a,b,c : a + b + c 
# les fonctions lambda sont des fonctions anonymes (pas de nom)
# il faut stocker ces fonctions dans des variables ici traitement 

print(traitement) # <function <lambda> at 0x0000021A24C2E160>

print(traitement(1,2,3)) # 6 


def soustraction(a,b): # 4 instructions => impossible de la transformer en fonction lambda
    if a > 0 and b > 0 :
        return 10
    else:
        return a - b
    
sous2 = lambda a,b : 10 if a > 0 and b > 0 else a - b

# cas pratique
# vous avez une liste qui contient les valeurs suivantes 
# [1,2,4,5,6, 10]
# pouvez vous retourner le tableau avec uniquement les valeurs impaires
# [ 1 , 5  ]

# boucle ET condition
# sort() et une fonction lambda