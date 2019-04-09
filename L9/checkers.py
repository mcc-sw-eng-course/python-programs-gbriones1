import random

from boardgame import *

class CheckersPlayer(Player):
    
    def play(self):
        options = self.game.possible_movements()
        if options:
            action = self.recieve_input(options)
            from_move, to_move, to_eat = options[action]
            cell = self.game.board.get_cell(from_move[0], from_move[1])
            new_value = cell.value
            if self.game.player_in_turn == 0:
                if to_move[0] == 0:
                    new_value = "X"
            elif to_move[0] == 7:
                    new_value = "O"
            self.game.board.set_cell(from_move[0], from_move[1], None)
            self.game.board.set_cell(to_move[0], to_move[1], new_value)
            for enemy_pos in to_eat:
                self.game.board.set_cell(enemy_pos[0], enemy_pos[1], None)

    
    def recieve_input(self, options):
        raise NotImplementedError


class HumanPlayer(CheckersPlayer):

    def recieve_input(self, options):
        options_str = ""
        for opt_idx in range(len(options)):
            from_move, to_move, _ = options[opt_idx]
            options_str += "{}) Move: {} to {}\n".format(opt_idx, from_move, to_move)
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

class AIPlayer(CheckersPlayer):

    def recieve_input(self, options):
        return random.randint(0, len(options)-1)

class Checkers(TurnBasedGridBoardGame):

    def __init__(self, player1, player2):
        super(Checkers, self).__init__(8, 8, ("x", "o", "X", "O"), [player1, player2])

    def initialize_board(self):
        for x in range(self.board.x_size):
            for y in range(self.board.y_size):
                if (x < 3 and y % 2 and not x % 2) or (x == 1 and not y % 2):
                    self.board.set_cell(x, y, "o")
                elif (x >= 5 and not y % 2 and x % 2) or (x == 6 and y % 2):
                    self.board.set_cell(x, y, "x")
                if (x % 2 and y % 2) or (not x % 2 and not y % 2):
                    cell = self.board.get_cell(x, y)
                    cell.domain = []


    def has_ended(self):
        if self.evaluate_winner():
            return True
        if not self.possible_movements():
            return True
        return False

    def evaluate_winner(self):
        p1_pieces = 0
        p2_pieces = 0
        for x in range(self.board.x_size):
            for y in range(self.board.y_size):
                cell = self.board.get_cell(x, y)
                if cell.value in ["x","X"]:
                    p1_pieces += 1
                elif cell.value in ["o", "O"]:
                    p2_pieces += 1
        if self.player_in_turn == 0 and not p2_pieces:
            return self.players[self.player_in_turn]
        elif self.player_in_turn == 1 and not p1_pieces:
            return self.players[self.player_in_turn]
        if not self.possible_movements():
            return None
        return None

    def possible_movements(self):
        possible_movements = []
        if self.player_in_turn == 0:
            piece_token = "x"
            piece_queen = "X"
            piece_enemies = ["o", "O"]
        else:
            piece_token = "o"
            piece_queen = "O"
            piece_enemies = ["x", "X"]
        attack_move = []
        for cell in self.board.cells:
            if cell.value == piece_token:
                if self.player_in_turn == 0:
                    if cell.y-1 >= 0:
                        next_j_cell = self.board.get_cell(cell.x-1, cell.y-1)
                        if next_j_cell.value in piece_enemies:
                            if cell.y-2 >= 0 and cell.x-2 >= 0:
                                next_jj_cell = self.board.get_cell(cell.x-2, cell.y-2)
                                if next_jj_cell.value is None:
                                    attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                        elif not attack_move and next_j_cell.value is None:
                            possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                    if cell.y+1 <= 7:
                        next_j_cell = self.board.get_cell(cell.x-1, cell.y+1)
                        if next_j_cell.value in piece_enemies:
                            if cell.y+2 <= 7 and cell.x-2 >= 0:
                                next_jj_cell = self.board.get_cell(cell.x-2, cell.y+2)
                                if next_jj_cell.value is None:
                                    attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                        elif not attack_move and next_j_cell.value is None:
                            possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                else:
                    if cell.y-1 >= 0:
                        next_j_cell = self.board.get_cell(cell.x+1, cell.y-1)
                        if next_j_cell.value in piece_enemies:
                            if cell.y-2 >= 0 and cell.x+2 <= 7:
                                next_jj_cell = self.board.get_cell(cell.x+2, cell.y-2)
                                if next_jj_cell.value is None:
                                    attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                        elif not attack_move and next_j_cell.value is None:
                            possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                    if cell.y+1 <= 7:
                        next_j_cell = self.board.get_cell(cell.x+1, cell.y+1)
                        if next_j_cell.value in piece_enemies:
                            if cell.y+2 <= 7 and cell.x+2 <= 7:
                                next_jj_cell = self.board.get_cell(cell.x+2, cell.y+2)
                                if next_jj_cell.value is None:
                                    attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                        elif not attack_move and next_j_cell.value is None:
                            possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
            if cell.value == piece_queen:
                if cell.y-1 >= 0 and cell.x-1 >=0:
                    next_j_cell = self.board.get_cell(cell.x-1, cell.y-1)
                    if next_j_cell.value in piece_enemies:
                        if cell.y-2 >= 0 and cell.x-2 >= 0:
                            next_jj_cell = self.board.get_cell(cell.x-2, cell.y-2)
                            if next_jj_cell.value is None:
                                attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                    elif not attack_move and next_j_cell.value is None:
                        possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                if cell.y+1 <= 7 and cell.x-1 >=0:
                    next_j_cell = self.board.get_cell(cell.x-1, cell.y+1)
                    if next_j_cell.value in piece_enemies:
                        if cell.y+2 <= 7 and cell.x-2 >= 0:
                            next_jj_cell = self.board.get_cell(cell.x-2, cell.y+2)
                            if next_jj_cell.value is None:
                                attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                    elif not attack_move and next_j_cell.value is None:
                        possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                if cell.y-1 >= 0 and cell.x+1 <= 7:
                    next_j_cell = self.board.get_cell(cell.x+1, cell.y-1)
                    if next_j_cell.value in piece_enemies:
                        if cell.y-2 >= 0 and cell.x+2 <= 7:
                            next_jj_cell = self.board.get_cell(cell.x+2, cell.y-2)
                            if next_jj_cell.value is None:
                                attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                    elif not attack_move and next_j_cell.value is None:
                        possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
                if cell.y+1 <= 7 and cell.x+1 <= 7:
                    next_j_cell = self.board.get_cell(cell.x+1, cell.y+1)
                    if next_j_cell.value in piece_enemies:
                        if cell.y+2 <= 7 and cell.x+2 <= 7:
                            next_jj_cell = self.board.get_cell(cell.x+2, cell.y+2)
                            if next_jj_cell.value is None:
                                attack_move.append([(cell.x, cell.y), (next_jj_cell.x, next_jj_cell.y), [(next_j_cell.x, next_j_cell.y)]])
                    elif not attack_move and next_j_cell.value is None:
                        possible_movements.append([(cell.x, cell.y), (next_j_cell.x, next_j_cell.y), []])
        if attack_move:
            possible_movements = attack_move
        return possible_movements
