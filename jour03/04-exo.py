def palindrome(text : str) -> bool:
    textLower = text.lower()
    return textLower == textLower[::-1]  
    
print(palindrome("Bonjour"))
print(palindrome("Lol"))
print(palindrome("KayAk"))