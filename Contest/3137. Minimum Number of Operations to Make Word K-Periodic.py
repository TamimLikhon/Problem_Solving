word = "leetcoleet"
k = 2
count = {}
n = len(word)
for i in range(0, n, k):
    substring = word[i:i+k]
    count[substring] = count.get(substring, 0) + 1
mx = max(count.values()) if count else 0
result = (n // k) - mx

print(result)