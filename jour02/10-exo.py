import math

def aireCercle(rayon):
    resultat = 3.14 * rayon ** 2
    print(f"l'aire d'un cercle de rayon {rayon} a une aire de {math.floor(resultat) }")

# 4/ exécuter la fonction aireCercle pour le rayon
# 44,5
# 70,43

aireCercle(44.5)   # l'aire d'un cercle de rayon 44.5 a une aire de 6217.985000000001
aireCercle(70.43)  # l'aire d'un cercle de rayon 70.43 a une aire de 15575.608586000004