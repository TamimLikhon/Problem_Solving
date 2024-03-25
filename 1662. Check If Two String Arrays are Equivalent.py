def listtostring(word1, word2):
    str1 = ""
    str2 = ""

    for ele in word1:
        str1 += ele
    for ele in word2:
        str2 += ele

ult_word = listtostring(word1, word2)

if ult_word[0] == ult_word[1]:
    print("True")   

    return str1, str2

word1 = ["ab", "c"]
word2 = ["a", "bc"]

 