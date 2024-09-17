ville = "Marseille"

if ville == "Paris" :
    print("vous habitez à Paris")
elif ville == "Boulogne" or \
     ville == "Clamart" or \
     ville == "Montrouge" :
    #   ne pas oublier la comparaison
    print("vous habitez dans le 92")
elif ville == "Saint-Denis" or \
     ville == "Aubervilliers" or \
     ville == "Pantin" :
    print("vous habitez dans le 93")
else :
    print("vous habitez hors d'Ile de France")

tuple = ("Paris" or "Clamart" or "Montrouge")
tuple = ("Paris")
print(ville == tuple)