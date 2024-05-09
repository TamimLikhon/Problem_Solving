max_or = 0
prev = Counter()
prev[0] = 1

for elem in nums:
    max_or |= elem
    for prev_or, ctn in list(prev.items()):
        prev[prev_or | elem] += ctn

return prev[max_or]