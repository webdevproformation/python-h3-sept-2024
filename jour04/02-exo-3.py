def anagram (mot1, mot2):
    mot1 = sorted(mot1.lower().replace(" ", ""))
    mot2 = sorted(mot2.lower().replace(" ", ""))
    return mot1 == mot2

print(anagram("Eva", "vAe"))