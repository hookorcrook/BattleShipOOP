import os
from player import Player

GAME_FILE_NAME = 'high_scores.txt'
GAME_FILE = os.path.join(os.curdir,GAME_FILE_NAME)


class Game:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.current_player = self.player1
        self.num_guesses_player1 = 0  # Track guesses for Player 1
        self.num_guesses_player2 = 0  # Track guesses for Player 2

    def start(self):
        # Prompt for player names
        self.player1.name = input("Enter name for Player 1: ")
        self.player2.name = input("Enter name for Player 2: ")

        print("Welcome to Battleship!\n")
        self.player1.place_ships()
        self.player2.place_ships()

        print("Time for Battle!!\n")
        
        while not self.is_game_over():
            self.current_player.take_turn(self.opponent_board())
            if self.current_player == self.player1:
                self.num_guesses_player1 += 1
            else:
                self.num_guesses_player2 += 1

            if self.is_game_over():
                break  # Exit the loop if the game is over

            self.switch_turn()

        # Determine who the winner is
        winner = self.current_player.name
        winner_guesses = self.num_guesses_player1 if self.current_player == self.player1 else self.num_guesses_player2
        print(f"{winner} wins with {winner_guesses} guesses!")

        # Record the game result (winner and guesses)
        self.record_game_result(winner, winner_guesses)
        self.display_high_score()  # Display the high score after the game

    def is_game_over(self):
        return self.current_player.board.is_game_over() or \
               self.opponent_board().is_game_over()

    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def opponent_board(self):
        return self.player2.board if self.current_player == self.player1 else self.player1.board

    def record_game_result(self, winner, winner_guesses):
        # Check if file exists
        if not os.path.exists(GAME_FILE):
            with open(GAME_FILE, 'w') as file:
                file.write("Player 1, Player 2, Winner, Guesses\n")  # Write header if file is empty

        # Record the result of the game
        with open(GAME_FILE, 'a') as file:
            file.write(f"{self.player1.name}, {self.player2.name}, {winner}, {winner_guesses}\n")

    def display_high_score(self):
        # Find the high score (minimum number of guesses for a win)
        if not os.path.exists(GAME_FILE):
            print("No game results yet.")
            return

        min_guesses = float('inf')  # Start with a very large number
        high_score_game = None
        
        with open(GAME_FILE, 'r') as file:
            lines = file.readlines()[1:]  # Skip header row
            for line in lines:
                data = line.strip().split(", ")
                guesses = int(data[3])
                if guesses < min_guesses:
                    min_guesses = guesses
                    high_score_game = data

        if high_score_game:
            print(f"High Score: {high_score_game[2]} won with {min_guesses} guesses.")
        else:
            print("No high score yet.")

if __name__ == "__main__":
    game = Game()
    game.start()