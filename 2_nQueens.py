def print_board(position, N):
    for row in range(N):
        line = ""
        for col in range(N):
            if col == position[row]:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def is_safe(position, row, col):
    for i in range(row):
        if position[i] == col or \
           position[i] - i == col - row or \
           position[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(position, row, N, solutions):
    if row == N:
        solutions.append(position[:])
        return
    for col in range(N):
        if is_safe(position, row, col):
            position[row] = col
            solve_n_queens_util(position, row + 1, N, solutions)

def solve_n_queens(N):
    solutions = []
    position = [-1] * N
    solve_n_queens_util(position, 0, N, solutions)
    print(f"Total Solutions for N={N}: {len(solutions)}\n")
    for sol in solutions:
        print_board(sol, N)

# Run the N-Queens solver
if __name__ == "__main__":
    N = 5  # You can change this to any N (e.g., 8)
    solve_n_queens(N)
