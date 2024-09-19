liste = [1,2,3,4,5,6]

print(liste[0:6:2]) # [1, 3, 5]
print(liste[::2]) # [1, 3, 5]
print(liste[::3]) # [1, 4]


print([ i for i in liste if i > 3  ])


tpl1 = (1,2)
tmp_list = list(tpl1)
tmp_list.append(3)
tpl1 = tuple(tmp_list)

print(tpl1)

etudiants = { "Alain" , "Céline" , "Benois", "Zorro" }

""" for i in etudiants:
    print(i) """
print(etudiants[0]) # TypeError: 'set' object is not subscriptable