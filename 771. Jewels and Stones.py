jewels = "aA"
stones = "aAAbbbb"

count = 0
jewel_set = set(jewels)
print("set", jewel_set)

for stone in stones:
    if stone in jewel_set:
        count+=1

print(count)