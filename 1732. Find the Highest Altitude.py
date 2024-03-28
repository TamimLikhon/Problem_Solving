gain = [-5,1,5,0,-7]
current_alt = 0
highest_alt = 0

for g in gain:
    current_alt += g
    highest_alt = max(highest_alt, current_alt)

print(highest_alt)