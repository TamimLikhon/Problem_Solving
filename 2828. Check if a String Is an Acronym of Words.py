words = ["an","apple"]
s = "a"

word = []
for i in range(len(words)):
    word.append(words[i][:1])
    
first_words = ''.join(word)
if first_words == s:
    print(True)
else:
    print(False)