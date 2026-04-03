import random 

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

    def make_move(self, move):
        # Place the current player's mark at the
        # given index. Return a NEW TicTacToe
        # object; do not modify self.        
        new_game = TicTacToe()
        new_game.board = [row[:] for row in self.board] # Deep copy of the board
        new_game.current_player = self.current_player 

        # illegal moves are not played
        if move not in self.get_legal_moves() or move < 0 or move > 8:
            print("Invalid move.")
            return new_game
        
        new_game.current_player = -self.current_player # Switching players
        new_game.board[move // 3][move % 3] = self.current_player
        return new_game
        

    def is_terminal(self):
        # Return True if the game is over, either
        # because someone has won or because all
        # squares are filled (a draw).
        if self.check_winner() != 0:
            return True
        return all(self.board[i // 3][i % 3] != 0 for i in range(9))
        

    def utility(self):
        # Return +1 if X has won, -1 if O has won,
        # or 0 for a draw. Only valid when
        # is_terminal() returns True.
        winner = self.check_winner()
        if winner == 1:
            return 1
        elif winner == -1:
            return -1
        else:
            return 0
        

    def check_winner(self):
        # Return 1 if X has three in a row, -1 if
        # O has three in a row, or 0 otherwise.
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != 0:
                return self.board[0][j]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        return 0
    

    def display(self):
        # Print the board in a readable 3x3 format.
        # Use 'X' for 1, 'O' for -1, '.' for 0.
        symbols = {1: 'X', -1: 'O', 0: '.'}
        for row in self.board:
            print(' '.join(symbols[cell] for cell in row))


def new_move(game:TicTacToe, move):
    print(f"{game.current_player}'s MOVE")
    new_game = game.make_move(move)

    print("New Board: ")
    new_game.display()
    print(f"Is terminal: {new_game.is_terminal()}")
    print(f"Current player: {new_game.current_player}")
    print(f"Legal Moves: {new_game.get_legal_moves()}")

    return new_game

def random_agent(state):
    legal_moves = state.get_legal_moves()
    return random.choice(legal_moves)


def main():
    game = TicTacToe()
    
    move0 = new_move(game, 8)
    move1 = new_move(move0, 8)
    move2 = new_move(move1, 9)
    move3 = new_move(move2, 0)
    move4 = new_move(move3, 5)
    move5 = new_move(move4, 3)
    move6 = new_move(move5, 2)


if __name__ == "__main__":
    main()
        
    