import random

from boardgame import *

class TicTacToePlayer(Player):
    
    def play(self):
        options = self.game.possible_movements()
        action = self.recieve_input(options)
        new_value = "o"
        if self.game.player_in_turn == 0:
            new_value = "x"
        cell = options[action]
        self.game.board.set_cell(cell.x, cell.y, new_value)
    
    def recieve_input(self, options):
        raise NotImplementedError


class HumanPlayer(TicTacToePlayer):

    def recieve_input(self, options):
        options_str = ""
        for cell_idx in range(len(options)):
            cell = options[cell_idx]
            options_str += "{}) Cell: {} {}\n".format(cell_idx, cell.x, cell.y)
        action = len(options)+1
        while action >= len(options):
            input_value = self.console_input("Player {}. Choose action:\n{}".format(self.game.player_in_turn+1, options_str))
            if input_value.isdigit():
                action = int(input_value)
            if action < 0:
                action = len(options)+1
        return action

    def console_input(self, text):
        return input(text)

class AIPlayer(TicTacToePlayer):

    def recieve_input(self, options):
        return random.randint(0, len(options)-1)

class TicTacToe(TurnBasedGridBoardGame):

    def __init__(self, player1, player2):
        super(TicTacToe, self).__init__(3, 3, ("x", "o"), [player1, player2])

    def has_ended(self):
        if self.evaluate_winner():
            return True
        if not self.possible_movements():
            return True

    def evaluate_winner(self):
        if not self.possible_movements():
            return None
        for x in range(self.board.x_size):
            if self.board.get_cell(x, 0).value == self.board.get_cell(x, 1).value == self.board.get_cell(x, 2).value != None:
                return self.players[self.player_in_turn]
        for y in range(self.board.y_size):
            if self.board.get_cell(0, y).value == self.board.get_cell(1, y).value == self.board.get_cell(2, y).value != None:
                return self.players[self.player_in_turn]
        if self.board.get_cell(0, 0).value == self.board.get_cell(1, 1).value == self.board.get_cell(2, 2).value != None:
            return self.players[self.player_in_turn]
        if self.board.get_cell(0, 2).value == self.board.get_cell(1, 1).value == self.board.get_cell(2, 0).value != None:
            return self.players[self.player_in_turn]
        return None

    def possible_movements(self):
        possible_movements = []
        for cell in self.board.cells:
            if cell.value is None:
                possible_movements.append(cell)
        return possible_movements
