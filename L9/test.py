from unittest.mock import patch
import unittest

from boardgame import Player, Board, TurnBasedGridBoardGame
from checkers import Checkers, HumanPlayer, CheckersPlayer, AIPlayer

class CheckersTest(unittest.TestCase):

    def test_get_movement(self):
        player1 = Player()
        player2 = Player()
        game = Checkers(player1, player2)
        for cell in game.board.cells:
            cell.value = None
        game.board.set_cell(7,4,"x")
        game.board.set_cell(6,3,"o")
        game.board.set_cell(4,3,"o")
        game.board.set_cell(2,3,"o")
        game.board.set_cell(0,3,"o")
        game.board.set_cell(6,5,"o")
        game.board.set_cell(4,5,"o")
        game.board.set_cell(2,5,"o")
        game.board.set_cell(0,5,"o")
        movements = list(game._get_movement(7,4,["LU", "RU"],["o", "O"]))
        self.assertEqual([((1, 2), [(2, 3), (4, 3), (6, 3)]), ((1, 6), [(2, 5), (4, 3), (6, 3)]), ((1, 2), [(2, 3), (4, 5), (6, 5)]), ((1, 6), [(2, 5), (4, 5), (6, 5)])], movements)
        game.board.set_cell(7,4,None)
        game.board.set_cell(5,6,"X")
        game.board.set_cell(6,1,"o")
        game.board.set_cell(4,1,"o")
        game.board.set_cell(2,1,"o")
        game.board.set_cell(0,1,"o")
        game.board.set_cell(6,7,"o")
        game.board.set_cell(4,7,"o")
        game.board.set_cell(2,7,"o")
        game.board.set_cell(0,7,"o")
        movements = list(game._get_movement(5,6,["LU", "RU", "LD", "RD"],["o", "O"]))
        self.assertEqual([((1, 6), [(2, 5), (4, 3), (4, 1), (2, 1), (2, 3), (4, 5)]), ((7, 0), [(6, 1), (4, 1), (2, 1), (2, 3), (4, 5)]), ((5, 6), [(6, 5), (6, 3), (4, 1), (2, 1), (2, 3), (4, 5)]), ((1, 6), [(2, 5), (4, 5)]), ((7, 4), [(6, 5)])], movements)

    def test_evaluate_winner(self):
        player1 = Player()
        player2 = Player()
        game = Checkers(player1, player2)
        game.player_in_turn = 0
        for cell in game.board.cells:
            if cell.value in ["o", "0"]:
                cell.value = None
        self.assertEqual(player1, game.evaluate_winner())
        game.player_in_turn = 1
        for cell in game.board.cells:
            if cell.value in ["x", "X"]:
                cell.value = None
        self.assertEqual(player2, game.evaluate_winner())

    def test_possible_movements(self):
        player1 = Player()
        player2 = Player()
        game = Checkers(player1, player2)
        for cell in game.board.cells:
            cell.value = None
        game.board.set_cell(2,3,"X")
        game.board.set_cell(2,5,"O")
        game.board.set_cell(4,3,"x")
        game.board.set_cell(4,5,"o")
        game.player_in_turn = 0
        self.assertEqual(6, len(game.possible_movements()))
        game.player_in_turn = 1
        self.assertEqual(6, len(game.possible_movements()))
        game.board.set_cell(3,4,"x")
        game.board.set_cell(2,3,"o")
        game.board.set_cell(2,5,"o")
        game.board.set_cell(4,3,"o")
        game.board.set_cell(4,5,"o")
        game.player_in_turn = 0
        self.assertEqual(2, len(game.possible_movements()))
        game.board.set_cell(3,4,"X")
        self.assertEqual(4, len(game.possible_movements()))
        game.board.set_cell(3,4,"o")
        game.board.set_cell(2,3,"x")
        game.board.set_cell(2,5,"x")
        game.board.set_cell(4,3,"x")
        game.board.set_cell(4,5,"x")
        game.player_in_turn = 1
        self.assertEqual(2, len(game.possible_movements()))
        game.board.set_cell(3,4,"O")
        self.assertEqual(4, len(game.possible_movements()))

    def test_has_ended(self):
        player1 = Player()
        player2 = Player()
        game = Checkers(player1, player2)
        for cell in game.board.cells:
            cell.value = None
        self.assertTrue(game.has_ended())

class CheckersPlayerTest(unittest.TestCase):

    @patch('checkers.CheckersPlayer.recieve_input', return_value=0)
    def test_play(self, input):
        player = CheckersPlayer()
        game = Checkers(player, CheckersPlayer())
        game.player_in_turn = 0
        self.assertTrue(game.board.get_cell(5,0).value == "x")
        player.play()
        self.assertTrue(game.board.get_cell(4,1).value == "x")
        self.assertTrue(game.board.get_cell(5,0).value is None)

class HumanPlayerTest(unittest.TestCase):

    @patch('checkers.HumanPlayer.console_input', return_value='4')
    def test_recieve_input(self, input):
        player = HumanPlayer()
        game = Checkers(player, Player())
        self.assertEqual(player.recieve_input(game.possible_movements()), 4)

class AIPlayerTest(unittest.TestCase):

    def test_recieve_input(self):
        player = AIPlayer()
        game = Checkers(player, Player())
        options = game.possible_movements()
        action = player.recieve_input(options)
        self.assertGreaterEqual(action, 0)
        self.assertLessEqual(action, len(options))


def has_ended(self):
    if self.turn == 2:
        return True
    return False

class BoardGameTest(unittest.TestCase):

    @patch('boardgame.TurnBasedGridBoardGame.has_ended', side_effect=has_ended, autospec=True)
    @patch('boardgame.TurnBasedGridBoardGame.evaluate_winner', return_value=None)
    @patch('boardgame.Player.play', return_value=None)
    def test_start(self, has_ended_mock, evaluate_winner_mock, play_mock):
        player1 = Player()
        game = TurnBasedGridBoardGame(1,1, [], [player1])
        game.start()
        self.assertEqual(game.winner, None)

if __name__ == '__main__':
    unittest.main()