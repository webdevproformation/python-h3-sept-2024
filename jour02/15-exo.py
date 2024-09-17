liste = [1,2,4,5,6,10]

resultat = []
for i in liste:
    if i % 2 != 0 :
        resultat.append(i)

print(resultat)

resultat2 = filter( lambda i : i % 2 != 0 , liste )

print(resultat2)       # <filter object at 0x000001E97E4E79A0>
print(list(resultat2)) # [1, 5]

""" for index, valeur in enumerate(liste):
    print(index , valeur)
    if valeur % 2 == 0 :
        liste.remove(valeur)

print(liste)

l = [1,2,4,5,6,10]
l.remove(6)
print(l) """

