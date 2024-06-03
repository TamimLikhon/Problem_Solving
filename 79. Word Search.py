def exist(board, word):
    m, n = len(board), len(board[0])
    
    def dfs(i, j, k):
        # Check if we have completed the word
        if k == len(word):
            return True
        
        # Check boundaries and character match
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:  #dfs checking for grid
            
            return False
        
        # Mark the cell as visited by changing its value
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore all four directions
        found = (dfs(i + 1, j, k + 1) or
                 dfs(i - 1, j, k + 1) or
                 dfs(i, j + 1, k + 1) or
                 dfs(i, j - 1, k + 1))
        
        # Restore the cell's original value
        board[i][j] = temp
        
        return found
    
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    
    return False

# Example usage:
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCCED"

print(exist(board, word))  # Output: True
