'''
    *****HEAD TO HEAD COMPARISON*****
    - plays multiple games between different agent combinations
    - four matchups, with at least 100 games per matchup
        23. Minimax (X) versus Random (O).
        24. MCTS with 1,000 iterations (X) versus Random (O).
        25. Minimax (X) versus MCTS with 1,000 iterations (O).
        26. MCTS with 1,000 iterations (X) versus Minimax (O). 
'''
#Minimax vs Random, record numbers of wins for X(minimax) and O(random), and number of draws and put it on a table
from game import TicTacToe
from minimax_agent import minimax

def play_game(agent_x, agent_o):
    game = TicTacToe()
    while not game.is_terminal():
        if game.current_player == 1:
            move = agent_x(game)
        else:
            move = agent_o(game)
            game = game.make_move(move)

    return game.utility()


#MTCs with 1000 iterations vs Random, record numbers of wins for X(MCTS) and O(random), and number of draws and put it on a table
def random_agent(state):
    import random
    legal_moves = state.get_legal_moves()
    return random.choice(legal_moves)

def main():
    import mcts_agent as mcts
    num_games = 100
    results = {'Minimax vs Random': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'MCTS vs Random': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'Minimax vs MCTS': {'X wins': 0, 'O wins': 0, 'Draws': 0},
               'MCTS vs Minimax': {'X wins': 0, 'O wins': 0, 'Draws': 0}}

    for _ in range(num_games):
        result = play_game(minimax, random_agent)
        if result == 1:
            results['Minimax vs Random']['X wins'] += 1
        elif result == -1:
            results['Minimax vs Random']['O wins'] += 1
        else:
            results['Minimax vs Random']['Draws'] += 1
    for _ in range(num_games):
        result = play_game(lambda state: mcts(state, iterations=1000), random_agent)
        if result == 1:
            results['MCTS vs Random']['X wins'] += 1
        elif result == -1:
            results['MCTS vs Random']['O wins'] += 1
        else:
            results['MCTS vs Random']['Draws'] += 1
    for _ in range(num_games):
        result = play_game(minimax, lambda state:mcts(state,iterations =1000))
        if result == 1:
            results['Minimax vs MCTS']['X wins'] +=1
        elif result == -1:
            results['Minimax vs MCTS']['O wins'] += 1
        else:
            results['Minimax vs MCTS']['Draws'] += 1
    for _ in range(num_games):
        result = play_game(lambda state: mcts(state, iterations=1000), minimax)
        if result == 1:
            results['MCTS vs Minimax']['X wins'] += 1
        elif result == -1:
            results['MCTS vs Minimax']['O wins'] += 1
        else:
            results['MCTS vs Minimax']['Draws'] += 1

    # Print results in a  table format
    print(f"{'Matchup':20} {'X wins':10} {'O wins':10} {'Draws':10}")
    for matchup, stats in results.items():
        print(f"{matchup:20} {stats['X wins']:10} {stats['O wins']:10} {stats['Draws']:10}")
if __name__ == "__main__":    main()


