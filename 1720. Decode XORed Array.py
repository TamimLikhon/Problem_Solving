encoded = [1,2,3]
first = 1

ans = []
ans.append(first)
for i in encoded:
    first = first^i
    ans.append(first)

print(ans)
