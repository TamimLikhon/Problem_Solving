import string
def dfs(sentence):
    alph = set(string.ascii_lowercase)
    return alph <= set(sentence.lower())

sentence = "thequickbrownfoxjumpsoverthelazydog"
result =dfs(sentence)
print(result)