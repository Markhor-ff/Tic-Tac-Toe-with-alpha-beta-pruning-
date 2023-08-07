import random

def show_board(board):
    """
    Displays the tic-tac-toe board.
    """
    print("     0   1   2")
    print()
    for row in range(3):
        print(" {}  {} | {} | {}".format(row, display_cell(board[row][0]), display_cell(board[row][1]), display_cell(board[row][2])))
        if row < 2:
            print("    ___|___|___")
    print("      |   |")

def display_cell(cell):
    """
    Converts the cell value to "?" if it is None, otherwise returns the cell value.
    """
    return "?" if cell is None else cell

def check_winner(board):
    """
    Checks if there is a winner in the current state of the board.
    Returns 'X' if the player wins, 'O' if the computer wins, or None if there is no winner yet.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner
    return None

def get_empty_cells(board):
    """
    Returns a list of coordinates (row, col) of empty cells on the board.
    """
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                empty_cells.append((row, col))
    return empty_cells

def make_player_move(board):
    """
    Prompts the player to enter their move and updates the board accordingly.
    """
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] is None:
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def make_computer_move(board):
    """
    Makes a move for the computer using the Alpha-Beta Pruning algorithm.
    """
    best_score = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = None

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        board[row][col] = 'O'

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    The minimax algorithm implementation with Alpha-Beta Pruning.
    """
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif len(get_empty_cells(board)) == 0:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = None
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = None
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
        return best_score

def play_tic_tac_toe():
    """
    Main function to play the tic-tac-toe game.
    """
    board = [[None, None, None] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    show_board(board)

    while True:
        make_player_move(board)
        show_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins! Game over.")
            break
        elif len(get_empty_cells(board)) == 0:
            print("It's a tie! Game over.")
            break

        make_computer_move(board)
        print("Computer's move:")
        show_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins! Game over.")
            break
        elif len(get_empty_cells(board)) == 0:
            print("It's a tie! Game over.")

play_tic_tac_toe()