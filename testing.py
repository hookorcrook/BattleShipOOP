import unittest
from board import Board
from ship import Ship
from player import Player
from game import Game

class TestBattleship(unittest.TestCase):

    # Test the functionality of placing a ship on the board.
    # It checks if the ship is placed correctly based on the midpoint and orientation.
    def test_board_place_ship(self):
        board = Board(10, 10)
        ship = Ship("Destroyer", 3)
        # Ship placed at midpoint A5, horizontally (A4, A5, A6)
        result = board.place_ship(ship, 5, 0, 'h')  # Midpoint at A5
        self.assertTrue(result)
        self.assertEqual(board.grid[4][0], ship)  # A4
        self.assertEqual(board.grid[5][0], ship)  # A5
        self.assertEqual(board.grid[6][0], ship)  # A6

    # Test the functionality of ship getting sunk when it takes enoug hits
    def test_ship_hit_and_sunk(self):
        ship = Ship("Destroyer", 3)
        self.assertFalse(ship.is_sunk())
        ship.hit()
        self.assertFalse(ship.is_sunk())
        ship.hit()
        self.assertFalse(ship.is_sunk())
        ship.hit()
        self.assertTrue(ship.is_sunk())

    # Test the functionality of attacking a ship on the board.
    # It checks if the attack correctly hits the ship and marks the board appropriately.
    def test_board_attack(self):
        board = Board(10, 10)
        ship = Ship("Destroyer", 3)
        # Ship placed at midpoint A5, horizontally (A4, A5, A6)
        board.place_ship(ship, 5, 0, 'h')  # Midpoint at A5
        # Attack each cell (A4, A5, A6)
        result = board.attack(4, 0)  # A4
        self.assertTrue(result)  # Hit at A4
        result = board.attack(5, 0)  # A5
        self.assertTrue(result)  # Hit at A5
        result = board.attack(6, 0)  # A6
        self.assertTrue(result)  # Hit at A6
        result = board.attack(7, 0)  # Miss
        self.assertFalse(result)  # Miss (outside ship's range)


    def test_player_place_ships(self):
        player = Player("Player 1")
        player.place_ships()
        self.assertEqual(len(player.ships), 1)


    def test_game_over(self):
        game = Game()
        player1 = game.player1
        player2 = game.player2
        player1.board.place_ship(Ship("Destroyer", 3), 4, 0, 'h')  # Midpoint at A5
        player2.board.place_ship(Ship("Destroyer", 3), 4, 0, 'h')  # Midpoint at A5
        player1.board.attack(0, 0)
        player2.board.attack(0, 0)
        self.assertTrue(game.is_game_over())

    # Test high score functionality after completing a game.
    # It checks if the high score is correctly displayed based on the number of guesses.
    def test_high_score(self):
        game = Game()
        # Simulate a game where Player 1 wins
        game.player1.name = "Player 1"
        game.player2.name = "Player 2"
        game.num_guesses_player1 = 5  # Player 1 guesses 5 times
        game.num_guesses_player2 = 8  # Player 2 guesses 8 times
        game.record_game_result("Player 1", 5)  # Record Player 1's win
        game.display_high_score()  # Ensure that the high score is displayed correctly


    # Test that the game correctly handles invalid coordinate format input during attacks.
    # It ensures that errors are raised when an invalid coordinate (e.g., A10) is provided.
    def test_invalid_input(self):
        board = Board(10, 10)
        ship = Ship("Destroyer", 3)

        # Invalid placement test: out of bounds
        result = board.place_ship(ship, 5, 9, 'h')  # Attempt to place ship horizontally out of bounds
        self.assertFalse(result)

        # Invalid attack test: out of bounds
        with self.assertRaises(ValueError):
            board.attack(5, 10)  # Attack out of bounds

        # Invalid attack test: already attacked cell
        board.attack(4, 0)  # Attack A4
        with self.assertRaises(ValueError):
            board.attack(4, 0)  # Re-attack the same cell


if __name__ == '__main__':
    unittest.main()
