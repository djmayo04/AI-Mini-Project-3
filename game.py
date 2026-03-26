import numpy as np
class TicTacToe:
    def __init__(self):
        # Initialize an empty 3x3 board
        
        # Board is a 3x3 list of lists:
        # 0 = empty, 1 = X, -1 = O
        # X always moves first
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def get_legal_moves(self):
        # Return a list of indices (0 through 8)
        # corresponding to the empty squares.
        return [i for i in range(9) if self.board[i // 3][i % 3] == 0]
        pass

    def make_move(self, move):
        # Place the current player's mark at the
        # given index. Return a NEW TicTacToe
        # object; do not modify self.
        new_game = TicTacToe()
        new_game.board = [row[:] for row in self.board] # Deep copy of the board
        new_game.current_player = -self.current_player # Swtching players
        new_game.board[move // 3][move % 3] = self.current_player
        return new_game
        pass

    def is_terminal(self):
        # Return True if the game is over, either
        # because someone has won or because all
        # squares are filled (a draw).
        if self.check_winner() != 0:
            return True
        return all(self.board[i // 3][i % 3] != 0 for i in range(9))
        pass

    def utility(self):
        # Return +1 if X has won, -1 if O has won,
        # or 0 for a draw. Only valid when
        # is_terminal() returns True.
        pass

    def check_winner(self):
        # Return 1 if X has three in a row, -1 if
        # O has three in a row, or 0 otherwise.
        pass

    def display(self):
        # Print the board in a readable 3x3 format.
        # Use 'X' for 1, 'O' for -1, '.' for 0.
        pass
    