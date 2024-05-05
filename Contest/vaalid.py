def isvalid(word):
    vowels = set()
    consonants = set()

    for char in word:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels.add(char.lower)
            else:
                consonants.add(char.lower)
        elif not char.isalnum():
            return False
        
    if len(word) < 3:
        return False
    
    has_vowel = bool(vowels)
    has_conso = bool(consonants)

    return has_vowel and has_conso