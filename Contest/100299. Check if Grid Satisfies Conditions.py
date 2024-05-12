def checkgrid(grid):
    n = len(grid)
    subgrid_lengths = [len(subgrid) for subgrid in grid]

    for i in range(n - 1):
        for j in range(subgrid_lengths[i]):  # Iterate based on the length of each sublist
            if grid[i][j] == grid[i + 1][j]:
                return True
            if grid[i][j] != grid[i + 1][j]:
                return True
    return False

grid = [[1,1,1],[0,0,0]]
result = checkgrid(grid)
print(result)  # Output: True
