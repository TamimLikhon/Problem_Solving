s = "aAbBcC"
count = 0
for i in range(len(s) - 1):
    if s[i].lower() != s[i + 1].lower():
        count += 1
print(count)