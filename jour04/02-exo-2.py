def anagram(string1 : str, string2 : str) -> bool:
    str1 = string1.lower().strip().replace(" ", "")
    str2 = string2.lower().strip().replace(" ", "")
    if len(str1) == len(str2) and sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
def anagram(string1 : str, string2 : str) -> bool:
    if len(string1.lower().replace(" ", "")) == len( string2.lower().replace(" ", "")) and sorted(string1.lower().replace(" ", "")) == sorted( string2.lower().replace(" ", "")):
        return True
    else:
        return False