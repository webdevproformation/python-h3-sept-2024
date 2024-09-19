def motNettoyeTrie(mot1):
    # enlever les majuscules
    mot1 = mot1.lower()
    # enlever les espaces début / milieu / fin 
    mot1 = mot1.replace(" ", "")
    # trier les lettres dans l'ordre alphabétiques hello => ehllo
    mot1 = list(mot1)
    mot1.sort()
    return "".join(mot1)


def anagram (mot1, mot2) :
    mot1 =  motNettoyeTrie(mot1)
    mot2 =  motNettoyeTrie(mot2)
    return mot1 == mot2
   

print(anagram("hOlle", "hello"))