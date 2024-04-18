class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        max_row_vals = [0] * n
        max_column_vals = [0] * n
        
        for i in range(n):
            for j in range(n):
                max_row_vals[i] = max(max_row_vals[i], grid[i][j])
                max_column_vals[j] = max(max_column_vals[j], grid[i][j])
        
        for i in range(n):
            for j in range(n):
                result += min(max_row_vals[i], max_column_vals[j]) - grid[i][j]
        
        return result