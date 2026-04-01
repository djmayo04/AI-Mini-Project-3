import math
import random
import game

class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.utility = 0
        self.visits = 0
        self.untried_moves = state.get_legal_moves()
        

    def is_fully_expanded(self):
        # Return True if every legal move from
        # this state has a corresponding child.
        for move in self.untried_moves:
            corresponding = 0
            for child in self.children:
                if move == child.move:
                    corresponding += 1
            
            if corresponding == 0:
                return False

        return True
            

    def best_child(self, c=1.41):
        # Return the child with the highest UCB1
        # score. Use the formula from Section 5.4.
        best = self.children[0]
        best_utility = best.utility / best.visits
        best_ucb1 = best_utility + c * math.sqrt((math.log(best.parent.visits)) / best.visits)

        for child in self.children:
            avg_utility = child.utility / child.visits
            ucb1 = avg_utility + c * math.sqrt((math.log(child.parent.visits)) / child.visits)
            if ucb1 > best_ucb1:
                best = child
                best_ucb1 = ucb1

        return best
    

    def best_move(self):
        # Return the move leading to the child
        # with the most visits (not the highest
        # win rate).
        most_visits = self.children[0]
        for child in self.children:
            if child.visits > most_visits.visits:
                most_visits = child
        
        return most_visits.move


# -----four steps
def select(node):
    # Starting from the given node, repeatedly
    # choose the best child (by UCB1) until you
    # reach a node that is not fully expanded
    # or that represents a terminal state.
    while not node.state.is_terminal() and node.is_fully_expanded():
        node = node.best_child()
    return node

def expand(node):
    # Choose one of the untried moves, create a
    # new child node for it, and return the child.
    move = random.choice(node.untried_moves)
    node.untried_moves.remove(move)
    # new node
    new_state = node.state.make_move(move)
    child = MCTSNode(new_state, parent=node, move=move)
    node.children.append(child)
    return child

def simulate(state):
    # From the given state, play a random game to
    # completion. At each step, choose a uniformly
    # random legal move. Return the utility.
    current_state = state
    while not current_state.is_terminal():
        legal_moves = current_state.get_legal_moves()
        move = random.choice(legal_moves)
        current_state = current_state.make_move(move)
    return current_state.utility()
    

def backpropagate(node, result):
    # Walk from the given node up to the root.
    # Increment the visit count of every node.
    # Increment the win count only for nodes
    # where the result was favorable for the
    # player who made the move.
    while node is not None:
        node.visits += 1
        node.utility += result * node.state.current_player
        node = node.parent

# -----main
def mcts(state, iterations=1000):
    root = MCTSNode(state)
    for _ in range(iterations):
        # 1. Select
        leaf = select(root)
        # 2. Expand (if not terminal)
        if not leaf.state.is_terminal():
            leaf = expand(leaf)
        # 3. Simulate
        result = simulate(leaf.state)
        # 4. Back-propagate
        backpropagate(leaf, result)
    return root.best_move()



def main():
    game_ = game.TicTacToe()
    move = mcts(game_, iterations=1000)
    print(f"MCTS recommends move: {move}")
    new_state = game_.make_move(move)
    new_state.display()

if __name__ == "__main__":
    main()
    