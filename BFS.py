from collections import deque

# Define the grid
grid = [
    ['S', '.', '.', '.', '.'],
    ['.', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', 'X'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'G']
]

# Define the dimensions of the grid
ROWS = len(grid)
COLS = len(grid[0])

# Define directions: up, down, left, right
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Function to perform BFS
def bfs(start_row, start_col, goal_row, goal_col):
    queue = deque([(start_row, start_col, [])])
    visited = set()
    while queue:
        row, col, path = queue.popleft()
        if (row, col) == (goal_row, goal_col):
            return path
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] != 'X':
                queue.append((new_row, new_col, path + [(new_row, new_col)]))
    return None

# Starting position
start_row, start_col = 0, 0
# Goal position
goal_row, goal_col = 4, 4

# Find the shortest path using BFS
path = bfs(start_row, start_col, goal_row, goal_col)

# Print the path
if path:
    print("Shortest path from start to goal:")
    for row, col in path:
        grid[row][col] = '*'
    for row in grid:
        print(' '.join(row))
else:
    print("No path found!")
