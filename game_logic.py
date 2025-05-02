# game_logic.py

from constants import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE, EMPTY, WINDOW_LENGTH

def winning_move(board, piece):
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all([board[r][c + i] == piece for i in range(4)]):
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all([board[r + i][c] == piece for i in range(4)]):
                return True

    # Check positive diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all([board[r + i][c + i] == piece for i in range(4)]):
                return True

    # Check negative diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all([board[r - i][c + i] == piece for i in range(4)]):
                return True

    return False

def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if board[ROW_COUNT - 1][c] == 0]

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0
