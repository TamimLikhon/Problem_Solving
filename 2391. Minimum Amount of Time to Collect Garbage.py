garbage = ["MMM", "PGM", "GP"]
travel = [3, 10]
count = 0

for i in range(min(len(garbage), len(travel))):
    if "M" in garbage[i]: 
        count += 3
        print(travel[0])

    count += travel[i]

print(count)
