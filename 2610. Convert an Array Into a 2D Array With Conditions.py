nums = [1,3,4,1,2,3,1]

nums.sort()

matrix = []

for num in nums:
    placed = False
    for row in matrix:
        if num not in row:
            row.append(num)
            placed = True
            break
    if not placed:
        matrix.append([num])
