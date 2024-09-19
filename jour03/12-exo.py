chiffres= {
    "I": 1,
    "V": 5,
    "X": 10,
    "L" : 50
}

"""
I => 1
II => 1 1 => 2
III = 1 1 1 => 1 + 1 + 1 = 3
IV  = 1 5   => - 1 + 5  => 4
V  = 5 
IX  =        => -1 + 10 => 9 
"""

def convertifRomainChiffreArabe(nombreEnChiffreRomain : str) -> int :
    total = 0
    for index, valeur in enumerate(nombreEnChiffreRomain) :
        if index + 1 != len(nombreEnChiffreRomain) and chiffres[nombreEnChiffreRomain[index]] < chiffres[nombreEnChiffreRomain[index + 1]]:
            total -= chiffres[nombreEnChiffreRomain[index]]
        else :
            total += chiffres[nombreEnChiffreRomain[index]]
    return total 

print(convertifRomainChiffreArabe("I"))
print(convertifRomainChiffreArabe("II"))
print(convertifRomainChiffreArabe("III"))
print(convertifRomainChiffreArabe("IV"))
print(convertifRomainChiffreArabe("V"))
print(convertifRomainChiffreArabe("IX"))