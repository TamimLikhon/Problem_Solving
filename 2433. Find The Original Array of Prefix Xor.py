pref = [5, 2, 0, 3, 1]
result = [pref[0]]

for i in range(len(pref) - 1):
    result.append(pref[i] ^ pref[i+1])
return result