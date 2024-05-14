def findFarmland(land):
    def dfs(i, j):
        if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] != 1:
            return
        land[i][j] = -1  # Mark current land as visited
        farmland.append([i, j])
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    farmlands = []
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                farmland = []
                dfs(i, j)
                farmlands.append(
                    [min(x[0] for x in farmland) , min(x[1] for x in farmland)] +
                    [max(x[0] for x in farmland) , max(x[1] for x in farmland)]
                )

    return farmlands

# Example usage:
matrix = [[1,0,0],[0,1,1],[0,1,1]]

print(findFarmland(matrix))
