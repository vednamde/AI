def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != " " for row in board for cell in row])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0-2.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
