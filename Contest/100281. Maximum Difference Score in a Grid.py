rowlen = len(grid)
collen = len(grid[0])

dp = [[0]*collen for _ in range(rowlen)]

res = float('-inf')
for r in range(rowlen-1,-1,-1):
    for c in range(collen-1,-1,-1):
        dp[r][c] = grid[r][c]
        if r < rowLen-1:
            dp[r][c] = max(dp[r+1][c],max(dp[r][c], dp[r+1][c]-grid[r][c]))
        if c < colLen-1:
            dp[r][c] = max(dp[r][c+1],max(dp[r][c], dp[r][c+1]-grid[r][c]))

    for r in range(rowlen):
        for c in range(collen):
            if r < rowlen - 1:
                res = max(res, dp[r+1] - grid[r][c])
            if c < collen - 1:
                res = max(res, dp[r][c+1] - grid[r][c])

    
    return res