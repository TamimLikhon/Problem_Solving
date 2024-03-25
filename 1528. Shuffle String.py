s = "abc"
indices = [0,1,2]
new_str = ""

for i in range(len(s)):
    new_str += s[indices.index(i)]

print(new_str)