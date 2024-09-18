
produits = [
    # id   nom            prix  dispo  qte
    ( 1 , "PS4"         , 200, True   , 2),
    ( 2 , "PS5"         , 600, False  , 3),
    ( 3 , "Nintendo DS" , 400, True   , 5 ),
]

# question 1
total = 0
for p in produits :
    #unpacking
    _ , _ , prix , dispo , qte = p 
    if dispo :
        total += prix * qte 
print(total) # 2400


# question 2
deuxieme_produit = list(produits[1])
deuxieme_produit[3] = True 
produits[1] = tuple(deuxieme_produit)

print(produits)