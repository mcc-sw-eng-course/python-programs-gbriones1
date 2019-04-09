from checkers import Checkers, AIPlayer, HumanPlayer

if __name__ == '__main__':
    checkers = Checkers(AIPlayer(), AIPlayer())
    checkers.start()
    print("Game ended in {} turns".format(checkers.turn+1))
    checkers.render()
    if checkers.winner:
        print("Winner!! Player {}".format(checkers.player_in_turn+1))
    else:
        print("Draw!!")