class BoardCell(object):

    def __init__(self, x, y, domain=[]):
        self.x = x
        self.y = y
        self.value = None
        self.domain = domain

class Board(object):

    def __init__(self, x_size, y_size, domain):
        self.cells = []
        self.x_size = x_size
        self.y_size = y_size
        self.domain = domain
        for x in range(x_size):
            for y in range(y_size):
                self.cells.append(BoardCell(x, y, domain))

    def get_cell(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def set_cell(self, x, y, value):
        cell = self.get_cell(x, y)
        if value in cell.domain:
            cell.value = value

    def __str__(self):
        rows = ""
        for x in range(self.x_size):
            row = ""
            for y in range(self.y_size):
                value = self.get_cell(x, y).value
                if value is None:
                    value = " "
                row += "{} |".format(value)
            rows += "{}\n".format(row)
        return rows

class TurnBasedGridBoardGame(object):

    def __init__(self, x_size, y_size, domain, players):
        self.board = Board(x_size, y_size, domain)
        self.players = players
        for player in self.players:
            player.game = self
        self.turn = -1
        self.player_in_turn = -1
        self.winner = None
        self.initialize_board()

    def start(self):
        while not self.has_ended():
            self.turn += 1
            self.player_in_turn +=1
            if self.player_in_turn >= len(self.players):
                self.player_in_turn = 0
            self.render()
            self.players[self.player_in_turn].play()
        self.winner = self.evaluate_winner()

    def initialize_board(self):
        pass

    def render(self):
        print(self.board)

    def has_ended(self):
        raise NotImplementedError

    def evaluate_winner(self):
        raise NotImplementedError


class Player(object):

    def __init__(self):
        self.game = None

    def play(self):
        raise NotImplementedError
