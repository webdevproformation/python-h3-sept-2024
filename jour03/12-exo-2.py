chiffres_romains = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def convertir_chiffre_romain(romain):

    total = 0
    prev_value = 0

    # inversion de la chaine de caractère => IV => VI
    for char in reversed(romain):
        current_value = chiffres_romains.get(char, 0) # V

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total

romain_input = input("Veuillez entrer un chiffre romain : ")

resultat = convertir_chiffre_romain(romain_input.upper())
print(f"Le chiffre correspondant à {romain_input} est : {resultat}")

# good !!!