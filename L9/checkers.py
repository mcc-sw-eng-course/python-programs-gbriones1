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

    MOVES = {
        "LU": (-1, -1),
        "RU": (-1, +1),
        "LD": (+1, -1),
        "RD": (+1, +1)
    }
    OPP_MOVES = {
        "LU": "RD",
        "RU": "LD",
        "LD": "RU",
        "RD": "LU"
    }

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

    def _get_movement(self, x, y, piece_moves, enemy_tokens, start=None, moved_from=None, path=None):
        if start is None:
            start = (x, y)
        if path is None:
            path = []
        for move in piece_moves:
            to_x = Checkers.MOVES[move][0]
            to_y = Checkers.MOVES[move][1]
            if moved_from != move and 0 <= x+to_x <= 7 and 0 <= y+to_y <= 7:
                next_cell = self.board.get_cell(x+to_x, y+to_y)
                if next_cell.value in enemy_tokens and (next_cell.x, next_cell.y) not in path:
                    if 0 <= x+to_x*2 <= 7 and 0 <= y+to_y*2 <= 7:
                        jump_cell = self.board.get_cell(x+to_x*2, y+to_y*2)
                        if jump_cell.value is None or (jump_cell.x, jump_cell.y) == start:
                            path.append((next_cell.x, next_cell.y))
                            rec_moves = list(self._get_movement(jump_cell.x, jump_cell.y, piece_moves, enemy_tokens, start, moved_from=Checkers.OPP_MOVES[move], path=path))
                            use_rec = False
                            for recursive_move in rec_moves:
                                if recursive_move[1]:
                                    use_rec = True
                                    to_eat = []
                                    for rec_eat in recursive_move[1]:
                                        to_eat.append(rec_eat)
                                    to_eat.append((next_cell.x, next_cell.y))
                                    yield recursive_move[0], to_eat
                            if not use_rec:
                                yield (jump_cell.x, jump_cell.y), [path.pop()]
                elif next_cell.value is None:
                    yield (next_cell.x, next_cell.y), []

    def possible_movements(self):
        possible_movements = []
        if self.player_in_turn == 0:
            piece_token = "x"
            piece_queen = "X"
            piece_enemies = ["o", "O"]
            piece_moves = ["LU", "RU"]
        else:
            piece_token = "o"
            piece_queen = "O"
            piece_enemies = ["x", "X"]
            piece_moves = ["LD", "RD"]
        attack_moves = []
        for cell in self.board.cells:
            possible_moves = piece_moves
            if cell.value == piece_queen:
                possible_moves = Checkers.MOVES.keys()
            if cell.value in [piece_queen, piece_token]:
                for cell_lands, cell_eats in self._get_movement(cell.x, cell.y, possible_moves, piece_enemies):
                    if cell_eats:
                        attack_moves.append([(cell.x, cell.y), cell_lands, cell_eats])
                    elif not attack_moves:
                        possible_movements.append([(cell.x, cell.y), cell_lands, []])
        if attack_moves:
            possible_movements = attack_moves
        return possible_movements
