from unittest.mock import patch
import unittest

from boardgame import Player, Board
from tictactoe import TicTacToe, HumanPlayer, TicTacToePlayer, AIPlayer

class TicTacToeGame(unittest.TestCase):

    def test_evaluate_winner_row(self):
        player1 = Player()
        game = TicTacToe(player1, Player())
        game.player_in_turn = 0
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(0, 1, "x")
        game.board.set_cell(0, 2, "x")
        self.assertEqual(player1, game.evaluate_winner())

    def test_evaluate_winner_col(self):
        player1 = Player()
        game = TicTacToe(player1, Player())
        game.player_in_turn = 0
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(1, 0, "x")
        game.board.set_cell(2, 0, "x")
        self.assertEqual(player1, game.evaluate_winner())

    def test_evaluate_winner_diag1(self):
        player1 = Player()
        game = TicTacToe(player1, Player())
        game.player_in_turn = 0
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(1, 1, "x")
        game.board.set_cell(2, 2, "x")
        self.assertEqual(player1, game.evaluate_winner())

    def test_evaluate_winner_diag2(self):
        player1 = Player()
        game = TicTacToe(player1, Player())
        game.player_in_turn = 0
        game.board.set_cell(0, 2, "x")
        game.board.set_cell(1, 1, "x")
        game.board.set_cell(2, 0, "x")
        self.assertEqual(player1, game.evaluate_winner())

    def test_has_ended(self):
        game = TicTacToe(Player(), Player())
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(0, 1, "o")
        game.board.set_cell(0, 2, "x")
        game.board.set_cell(1, 0, "x")
        game.board.set_cell(1, 1, "x")
        game.board.set_cell(1, 2, "o")
        game.board.set_cell(2, 0, "o")
        game.board.set_cell(2, 1, "x")
        game.board.set_cell(2, 2, "o")
        self.assertTrue(game.has_ended())

    def test_has_not_ended(self):
        game = TicTacToe(Player(), Player())
        game.board.set_cell(2, 0, "x")
        game.board.set_cell(2, 1, "x")
        game.board.set_cell(2, 2, "o")
        self.assertFalse(game.has_ended())

    def test_has_ended_winner(self):
        game = TicTacToe(Player(), Player())
        game.board.set_cell(2, 0, "x")
        game.board.set_cell(2, 1, "x")
        game.board.set_cell(2, 2, "x")
        self.assertTrue(game.has_ended())

    def test_possible_movements(self):
        game = TicTacToe(Player(), Player())
        self.assertEqual(len(game.possible_movements()), 9)

    def test_some_possible_movements(self):
        game = TicTacToe(Player(), Player())
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(0, 1, "o")
        game.board.set_cell(0, 2, "x")
        self.assertEqual(len(game.possible_movements()), 6)

    def test_no_possible_movements(self):
        game = TicTacToe(Player(), Player())
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(0, 1, "o")
        game.board.set_cell(0, 2, "x")
        game.board.set_cell(1, 0, "x")
        game.board.set_cell(1, 1, "x")
        game.board.set_cell(1, 2, "o")
        game.board.set_cell(2, 0, "o")
        game.board.set_cell(2, 1, "x")
        game.board.set_cell(2, 2, "o")
        self.assertEqual(len(game.possible_movements()), 0)

class HumanPlayerTest(unittest.TestCase):

    @patch('tictactoe.HumanPlayer.console_input', return_value='4')
    def test_recieve_input(self, input):
        player = HumanPlayer()
        game = TicTacToe(player, Player())
        self.assertEqual(player.recieve_input(game.possible_movements()), 4)

class AIPlayerTest(unittest.TestCase):

    def test_recieve_input(self):
        player = AIPlayer()
        game = TicTacToe(player, Player())
        options = game.possible_movements()
        action = player.recieve_input(options)
        self.assertGreaterEqual(action, 0)
        self.assertLessEqual(action, len(options))



class TicTacToePlayerTest(unittest.TestCase):

    @patch('tictactoe.TicTacToePlayer.recieve_input', return_value=0)
    def test_play(self, input):
        player = TicTacToePlayer()
        game = TicTacToe(player, TicTacToePlayer())
        game.board.set_cell(0, 0, "x")
        game.board.set_cell(0, 1, "o")
        game.board.set_cell(0, 2, "x")
        game.player_in_turn = 0
        player.play()
        self.assertTrue(game.board.get_cell(1,0).value, "x")

    def test_recieve_input(self):
        player = TicTacToePlayer()
        self.assertRaises(NotImplementedError, player.recieve_input, options=[])


if __name__ == '__main__':
    unittest.main()