s = "abc"
t = "bac"

n = len(s)
value = 0

for i in range(n):
        value +=  abs(s.index(s[i]) - t.index(s[i]))


print(value)