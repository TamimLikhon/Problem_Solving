names = ["Alice","Bob","Bob"]
heights = [155,185,150]

people = list(zip(names, heights))
people.sort(key=lambda x: x[1], reverse=True)
sorted_names = [person[0] for person in people]

print(sorted_names)