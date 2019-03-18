from tictactoe import TicTacToe, TicTacToePlayer

class HumanUIPlayer(TicTacToePlayer):

    def recieve_input(self, options):
        pass

class TicTacToeUI(TicTacToe):

    def render(self):
        print("Dummy")
