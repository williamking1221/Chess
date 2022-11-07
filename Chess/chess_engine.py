"""
Game info and game state. Determines valid moves too.
"""
class GameState():
    def __init__(self):
        # Board is 8x8 2D array. "--" is blank. First Char = b/w. Second Char = type of piece.
        self.board= [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.white_to_move = True     # Check whose turn is it to move.
        self.move_log = []            # Move log

    def make_move(self, move):
        self.board[move.start_square_row][move.start_square_col] = "--"
        self.board[move.end_square_row][move.end_square_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move

class Move():
    # Rank file notation
    rank_to_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    row_to_rank = {v: k for k, v in rank_to_row.items()}
    file_to_col = {"h": 7, "g": 6, "f": 5, "e": 4, "d": 3, "c": 2, "b": 1, "a": 0}
    col_to_file = {v: k for k, v in file_to_col.items()}

    def __init__(self, start_square, end_square, board):
        self.start_square_row = start_square[0]
        self.start_square_col = start_square[1]
        self.end_square_row = end_square[0]
        self.end_square_col = end_square[1]
        self.piece_moved = board[self.start_square_row][self.start_square_col]
        self.piece_capture = board[self.end_square_row][self.end_square_col]

    # To make into real chess notation
    def get_chess_not(self):
        return self.get_rank_file(self.start_square_row, self.start_square_col) + \
               self.get_rank_file(self.end_square_row, self.end_square_col)

    def get_rank_file(self, r, c):
        return self.col_to_file[c] + self.row_to_rank[r]