def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  
    return None

def is_valid(grid, num, pos):
    row, col = pos

    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True  

    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0 

    return False

if __name__ == "__main__":
    sudoku_grid = [
        [5, 1, 7, 6, 0, 0, 0, 3, 4],
        [2, 8, 9, 0, 0, 4, 0, 0, 0],
        [3, 4, 6, 2, 0, 5, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 3, 8, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 8],
        [7, 0, 3, 4, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("🧩 Unsolved Sudoku:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\n✅ Solved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("❌ No solution exists for the given Sudoku.")
