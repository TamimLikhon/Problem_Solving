patterns = ["a","abc","bc","d"]
word = "abc"
count = 0

for pattern in patterns:
    if pattern in word:
        count += 1

print(count)
