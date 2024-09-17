fleurs = [ "jasmin" , "rose" , "lilas" ]
prix = 12.5

# j'ai acheté des jasmins et des roses pour 12.5 €

# s1 = "j'ai acheté des " + fleurs[0] + "s et des " + fleurs[1] + "s pour " + prix + " €"
s1 = "j'ai acheté des " + fleurs[0] + "s et des " + fleurs[1] + "s pour " + str(prix) + " €"
print(s1)
# TypeError: can only concatenate str (not "float") to str
# utiliser str() sur le chiffre pour le convertir en str 

s2 = f"j'ai acheté des {fleurs[0]}s et des {fleurs[1]}s pour {prix} €"
print(s2)

s3 = "j'ai acheté des {}s et des {}s pour {} €".format(fleurs[0] , fleurs[1] , prix)
print(s3)