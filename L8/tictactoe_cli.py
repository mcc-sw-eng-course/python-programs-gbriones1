from tictactoe import TicTacToe, AIPlayer

if __name__ == '__main__':
    tictactoe = TicTacToe(AIPlayer(), AIPlayer())
    tictactoe.start()
    print("Game ended in {} turns".format(tictactoe.turn+1))
    tictactoe.render()
    if tictactoe.winner:
        print("Winner!! Player {}".format(tictactoe.player_in_turn+1))
    else:
        print("Draw!!")