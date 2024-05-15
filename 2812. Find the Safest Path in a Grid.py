def find_max_safeness(grid):
  """
  Finds the maximum safeness factor (minimum distance to thieves) in a grid.

  Args:
      grid: A 2D list representing the grid with 0s for empty cells and 1s for thieves.

  Returns:
      The maximum safeness factor.
  """
  n = len(grid)
  m = len(grid[0])
  max_safeness = 0

  # Check distances from each cell to nearest thief (top-left, bottom-right, 
  # and consider center cell for equidistance)
  for i in range(n):
    for j in range(m):
      # Distance to top-left thief
      distance_top_left = min(i, j)  # Manhattan distance

      # Distance to bottom-right thief (excluding thief itself)
      distance_bottom_right = min(n - i - 1, m - j - 1) if grid[i][j] != 1 else float('inf')

      # Check if cell is in the center (equidistant to both thieves)
      is_center = i == n // 2 and j == m // 2

      # Update max_safeness considering all possibilities
      max_safeness = max(max_safeness, min(distance_top_left, distance_bottom_right))
      if is_center:
        max_safeness = max(max_safeness, min(distance_top_left, distance_bottom_right) + 1)

  return max_safeness

# Example usage
#  grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
max_factor = find_max_safeness(grid)
print(f"Maximum Safeness Factor: {max_factor}")
