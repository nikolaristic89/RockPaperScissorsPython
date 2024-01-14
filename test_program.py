import unittest
from unittest.mock import patch
from game import Game
from players import HumanPlayer, ComputerPlayer
from userinterface import get_user_input

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(HumanPlayer("Human"), ComputerPlayer("Computer"))

    def test_determine_winner_rock_vs_scissors(self):
        result = self.game.determine_winner("Rock", "Scissors")
        self.assertEqual(result, "Human wins!")

    def test_determine_winner_scissors_vs_paper(self):
        result = self.game.determine_winner("Scissors", "Paper")
        self.assertEqual(result, "Human wins!")

    def test_determine_winner_paper_vs_rock(self):
        result = self.game.determine_winner("Paper", "Rock")
        self.assertEqual(result, "Human wins!")

    def test_determine_winner_tie(self):
        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            result = self.game.determine_winner(choice, choice)
            self.assertEqual(result, "It's a tie!")

    @patch('game.get_user_input', return_value="Yes")
    def test_ask_to_start_game_yes(self, mock_input):
        self.assertTrue(Game.ask_to_start_game())

    @patch('game.get_user_input', return_value="No")
    def test_ask_to_start_game_no(self, mock_input):
        self.assertFalse(Game.ask_to_start_game())

    @patch('game.get_user_input', return_value="1")
    def test_create_game_human_vs_computer(self, mock_input):
        game = Game.ask_game_mode()
        self.assertIsInstance(game.player1, HumanPlayer)
        self.assertIsInstance(game.player2, ComputerPlayer)

    @patch('game.get_user_input', return_value="2")
    def test_create_game_computer_vs_computer(self, mock_input):
        game = Game.ask_game_mode()
        self.assertIsInstance(game.player1, ComputerPlayer)
        self.assertIsInstance(game.player2, ComputerPlayer)



if __name__ == '__main__':
    unittest.main()