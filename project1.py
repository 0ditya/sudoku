import time

def solve_sudoku_optimized(board):
    rows = [set(range(1, 10)) for _ in range(9)]
    cols = [set(range(1, 10)) for _ in range(9)]
    grids = [set(range(1, 10)) for _ in range(9)]
    empty_cells = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_cells.append((i, j))
            else:
                num = board[i][j]
                rows[i].remove(num)
                cols[j].remove(num)
                grids[get_grid_index(i, j)].remove(num)

    empty_cells.sort(key=lambda cell: len(get_possible_numbers(cell, rows, cols, grids)))

    def backtrack(index):
        global iteration_count
        if index == len(empty_cells):
            return True  

        row, col = empty_cells[index]
        grid_idx = get_grid_index(row, col)
        possible_numbers = get_possible_numbers((row, col), rows, cols, grids)

        for num in possible_numbers:
            iteration_count += 1
            # Place the number
            board[row][col] = num
            rows[row].remove(num)
            cols[col].remove(num)
            grids[grid_idx].remove(num)

            # Recur to the next cell
            if backtrack(index + 1):
                return True

            # Undo the placement (backtrack)
            board[row][col] = 0
            rows[row].add(num)
            cols[col].add(num)
            grids[grid_idx].add(num)

        return False

    return backtrack(0)

def get_grid_index(row, col):
    return (row // 3) * 3 + (col // 3)

def get_possible_numbers(cell, rows, cols, grids):
    row, col = cell
    grid_idx = get_grid_index(row, col)
    return rows[row] & cols[col] & grids[grid_idx]

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

board = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

iteration_count = 0
start_time = time.time()

if solve_sudoku_optimized(board):
    end_time = time.time()
    print("Solved Sudoku:")
    print_board(board)
    print(f"\nTime taken: {end_time - start_time:.4f} seconds")
    print(f"Iterations: {iteration_count}")
else:
    print("No solution exists.")
