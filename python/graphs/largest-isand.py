# You are given a 2D map of integers where each cell is 0 or 1 – 1 representing a landmass and 0 representing water. 
# Landmasses are only connected in the four cardinal directions (up, down, left, right). 
# Find the area of the largest island. Note that any water bodies (lakes) surrounded by landmass are included in the area of the island. 
    # 1 1 1 1 0 
    # 1 0 0 1 0 
    # 1 1 1 1 0 
    # 0 0 0 0 0 
    # 1 1 0 0 1 
    # 0 0 0 0 0 
    # Output: 12

def find_largest_island(grid):
    # Initialize variables
    max_area = 0
    visited_set = set()  # Declare the visited_set variable

    # Iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if the cell is unvisited landmass or water body surrounded by landmass
            if ((grid[row][col] == 1 and not visited(row, col)) or
                (grid[row][col] == 0 and is_water_body(grid, row, col, visited_set))):
                # Count the area of the current island/water body
                current_area = bfs(grid, row, col, visited_set)
                max_area = max(max_area, current_area)

    return max_area


def visited(row, col):
    return (row, col) in visited_set


def is_water_body(grid, row, col, visited_set):
    # Check if the cell is water (0) and has at least one landmass neighbor
    if grid[row][col] == 0:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc

            # Check if the adjacent cell is within the grid bounds and is landmass (1)
            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                    grid[new_row][new_col] == 1):
                return True

    return False


def bfs(grid, row, col, visited_set):
    # Initialize the stack and mark the starting cell as visited
    stack = [(row, col)]
    visited_set = set()  # Declare the visited_set variable
    visited_set.add((row, col))

    # Initialize area counter
    area = 1

    # Explore adjacent cells using a stack
    while stack:
        # Pop the next cell from the stack
        current_row, current_col = stack.pop()

        # Explore adjacent cells in the four cardinal directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current_row + dr
            new_col = current_col + dc

            # Check if the adjacent cell is within the grid bounds and is either landmass or water body
            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                    ((grid[new_row][new_col] == 1 and not visited(new_row, new_col)) or
                     (grid[new_row][new_col] == 0 and is_water_body(grid, new_row, new_col, visited_set)))):
                # Mark the adjacent cell as visited and add it to the stack
                visited_set.add((new_row, new_col))
                stack.append((new_row, new_col))

                # Increment the area counter
                area += 1

    return area


# Example grid
grid = [
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
]

largest_island_area = find_largest_island(grid)
print("Largest island/water body area:", largest_island_area)
