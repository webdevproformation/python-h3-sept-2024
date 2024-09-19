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
# print(etudiants[0]) # TypeError: 'set' object is not subscriptable


u1 = {1,2,3,4,}
u2 = {1,2,3,4,}

commune_au_deux = u1.union(u2)
print(commune_au_deux) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

intersection = u1.intersection(u2)
print(intersection) # {1, 2, 3, 4}

inverse_intersection = u1.symmetric_difference(u2)
print(inverse_intersection) # {5, 6, 7, 8, 9} # set()

a = set()

# if a :