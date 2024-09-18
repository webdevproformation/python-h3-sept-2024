liste = [ 1,2,3]

liste2 = []

for i in liste:
    liste2.append(i + 2)

print(liste2)

# comprehension de liste 
liste3 = [ chiffre + 2  for  chiffre in liste  ]

print(liste3)


# -------------------------

liste4 = [ 1,2,3 ,4,5]

liste5 = []

for i in liste4:
    if i % 2 == 0 :
        liste5.append(i + 2)

print(liste5)

liste6 = [ chiffre + 2 for chiffre in liste4 if chiffre % 2 == 0 ]

print(liste6)