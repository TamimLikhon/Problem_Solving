grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]

onesRow = [0] * len(grid)
onesCol = [0] * len(grid[0])
ZeroRow = [0] * len(grid)
ZeroCol = [0] * len(grid[0])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            onesRow[i] += 1
            onesCol[j] += 1
        else:
            ZeroRow[i] += 1
            ZeroCol[j] += 1


last_diff = []
for i in range(len(grid)):
    row_diff = []
    for j in range(len(grid[0])):
        row_diff.append(onesRow[i] + onesCol[j] - ZeroRow[i] - ZeroCol[j])
    last_diff.append(row_diff)

print(last_diff)