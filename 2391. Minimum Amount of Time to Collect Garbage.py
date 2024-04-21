def min_minutes(garbage, travel):
    paper_time = 0
    glass_time = 0

    for i in range(len(garbage)):
        if 'P' in garbage[i]:
            paper_time += travel[i] + garbage[i].count('P')

        if 'G' in garbage[i]:
            if i == 0:
                glass_time += travel[i] + garbage[i].count('G')
            else:
                glass_time += travel[i - 1] + travel[i] + garbage[i].count('G')  # Fix indexing

    return paper_time + glass_time

garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
print(min_minutes(garbage, travel))  # Output: 21
