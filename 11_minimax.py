import math

# Initialize empty board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Check if the board has a winner or draw
def evaluate(board):
    # Check rows, columns, diagonals
    lines = []
    for i in range(3):
        lines.append(board[i])  # rows
        lines.append([board[0][i], board[1][i], board[2][i]])  # columns
    lines.append([board[0][0], board[1][1], board[2][2]])  # main diag
    lines.append([board[0][2], board[1][1], board[2][0]])  # anti diag
    for line in lines:
        if line == ['X', 'X', 'X']:
            return 10
        elif line == ['O', 'O', 'O']:
            return -10
    return 0

# Check if moves are left
def is_moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

# Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)
    # Terminal states
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

# Find best move for AI (X)
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Game loop (AI vs Human)
def play_game():
    board = create_board()
    print("Tic Tac Toe: You (O) vs AI (X)")
    print_board(board)
    while True:
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move!")
            continue
        board[row][col] = 'O'
        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break
        if not is_moves_left(board):
            print_board(board)
            print("Draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)
        if evaluate(board) == 10:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("Draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
