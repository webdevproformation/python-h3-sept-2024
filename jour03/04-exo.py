def palindrome(text : str) -> bool:
    textLower = text.lower()
    return textLower == textLower[::-1]  
    
print(palindrome("Bonjour"))
print(palindrome("Lol"))
print(palindrome("KayAk"))


palindrome2 = lambda mot : mot.lower() == mot.lower()[::-1] 

print(palindrome2("lol"))
print(palindrome2("Lol"))