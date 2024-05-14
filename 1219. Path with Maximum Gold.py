def max_gold(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        
        gold = grid[i][j]
        grid[i][j] = 0  # Mark the cell as visited
        max_gold_amount = max(
            dfs(i+1, j),  # Move down
            dfs(i-1, j),  # Move up
            dfs(i, j+1),  # Move right
            dfs(i, j-1)   # Move left
        )
        grid[i][j] = gold  # Backtrack
        return gold + max_gold_amount

    max_gold_amount = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_gold_amount = max(max_gold_amount, dfs(i, j))
    return max_gold_amount

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print("Maximum gold collected:", max_gold(grid))
