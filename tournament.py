#Minimax vs Random, record numbers of wins for X(minimax) and O(random), and number of draws and put it on a table
from game import TicTacToe
from minimax_agent_ab import minimax
import random
import mcts_agent


def play_game(agent_x, agent_o):
    games = TicTacToe()
    while not games.is_terminal():
        if games.current_player == 1:
            move = agent_x(games)
            games = games.make_move(move)
        else:
            move = agent_o(games)
            games = games.make_move(move)

    return games.utility()


#MTCs with 1000 iterations vs Random, record numbers of wins for X(MCTS) and O(random), and number of draws and put it on a table
def random_agent(state):
    legal_moves = state.get_legal_moves()
    return random.choice(legal_moves)


def main():
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
        result = play_game(mcts_agent.mcts, random_agent)
        if result == 1:
            results['MCTS vs Random']['X wins'] += 1
        elif result == -1:
            results['MCTS vs Random']['O wins'] += 1
        else:
            results['MCTS vs Random']['Draws'] += 1

    for _ in range(num_games):
        result = play_game(minimax, mcts_agent.mcts)
        if result == 1:
            results['Minimax vs MCTS']['X wins'] +=1
        elif result == -1:
            results['Minimax vs MCTS']['O wins'] += 1
        else:
            results['Minimax vs MCTS']['Draws'] += 1

    for _ in range(num_games):
        result = play_game(mcts_agent.mcts, minimax)
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
import time
    def measure_time(agent, num_moves=100):
        total_time = 0
        for _ in range(num_moves):
            start_time = time.time()
            move = agent(TicTacToe())
            total_time += time.time() - start_time
        return total_time / num_moves
    print("\nAverage time per move:")
    print(f"Minimax: {measure_time(minimax):.4f} seconds")
    print(f"MCTS: {measure_time(lambda state: mcts(state, iterations = 1000)):.4f} seconds")
    print(f"Random: {measure_time(random_agent):.4f} seconds")


if __name__ == "__main__":    main()


'''
    *****HEAD TO HEAD COMPARISON*****
    - plays multiple games between different agent combinations
    - four matchups, with at least 100 games per matchup
        23. Minimax (X) versus Random (O).
        24. MCTS with 1,000 iterations (X) versus Random (O).
        25. Minimax (X) versus MCTS with 1,000 iterations (O).
        26. MCTS with 1,000 iterations (X) versus Minimax (O). 
'''
