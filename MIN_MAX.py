# Define constants for the players
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

# Define constants for game result
DRAW = 0
X_WINS = 1
O_WINS = 2
ONGOING = 3

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

# Function to check if the game is over
def game_over(board):
    for row in board:
        if row.count(EMPTY) == 0 and len(set(row)) == 1:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    if all([cell != EMPTY for row in board for cell in row]):
        return DRAW

    return ONGOING

# Function to evaluate the score of the board for the given player
def evaluate(board, player):
    game_result = game_over(board)
    if game_result == DRAW:
        return 0
    elif game_result == PLAYER_X:
        return 1 if player == PLAYER_X else -1
    elif game_result == PLAYER_O:
        return 1 if player == PLAYER_O else -1
    else:
        return None

# Function to implement Minimax algorithm
def minimax(board, depth, maximizing_player):
    score = evaluate(board, PLAYER_X)
    if score is not None:
        return score

    if maximizing_player:
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_score = min(min_score, score)
        return min_score

# Function to find the best move for the given player
def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    player = PLAYER_X
    while game_over(board) == ONGOING:
        if player == PLAYER_X:
            row, col = find_best_move(board)
        else:
            print_board(board)
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        if board[row][col] == EMPTY:
            board[row][col] = player
            player = PLAYER_X if player == PLAYER_O else PLAYER_O
        else:
            print("Invalid move, try again.")
    print_board(board)
    result = game_over(board)
    if result == DRAW:
        print("It's a draw!")
    elif result == X_WINS:
        print("Player X wins!")
    else:
        print("Player O wins!")

# Start the game
play_game()
