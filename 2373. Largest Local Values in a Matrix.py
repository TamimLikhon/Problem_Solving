class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []        
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                max_val = max(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2])
                row.append(max_val)
            maxLocal.append(row)
    
        return maxLocal
