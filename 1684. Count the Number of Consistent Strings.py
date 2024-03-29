allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
count = 0

for word in words:
    if all(char in allowed for char in word):
        count+=1

print(count)