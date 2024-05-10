def find_path(maze, start_row, start_col, end_row, end_col):
    
  rows, cols = len(maze), len(maze[0])
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left

  visited = [[False for _ in range(cols)] for _ in range(rows)]  # Keep track of visited cells

  def dfs(row, col):
    # Check if we reached the end
    if row == end_row and col == end_col:
      return [(row, col)]

    # Mark current cell as visited
    visited[row][col] = True

    # Explore all four directions
    for dx, dy in directions:
      new_row, new_col = row + dx, col + dy

      # Check if new position is valid and not visited
      if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and maze[new_row][new_col] == 0:
        # Try exploring from this point
        path = dfs(new_row, new_col)
        # If a path is found, prepend the current cell and return
        if path:
          return [(row, col)] + path

    # Backtrack if no path found from this cell
    return None

  # Start DFS from the starting position
  path = dfs(start_row, start_col)
  return path

# Example usage
maze = [
  [0, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 0, 0, 0],
]

start_row, start_col = 0, 0
end_row, end_col = 3, 3

path = find_path(maze, start_row, start_col, end_row, end_col)

if path:
  print("Path found:", path)
else:
  print("No path found")
