from ship import Ship
from board import Board

ROWS = 26 # Alphabets A-Z
COLUMNS = 10 # 0-9 

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board(COLUMNS, ROWS)
        self.ships = [
            Ship('Destroyer 1', 3),
            Ship('Destroyer 2', 3),
            Ship('Cruiser', 5),
            Ship('Battleship', 7),
            Ship('Aircraft Carrier', 9) 
            ]

    def place_ships(self):
        print(f"\n{self.name}, it's your turn to place your ships:")
        for ship in self.ships:
            placed = False
            while not placed:
                try:
                    coordinate = input(f"Enter the coordinate for the {ship.name}'s anchor position (e.g., A6): ").upper()
                    orientation = input(f"Enter the orientation for the {ship.name} (h for horizontal/v for vertical): ").lower()

                    if len(coordinate) != 2 or not coordinate[0].isalpha() or not coordinate[1].isdigit():
                        raise ValueError("Invalid coordinate format. Please enter a coordinate like A6.")
                    
                    if orientation.lower() not in('h','v'):
                        raise ValueError("Invalid input for orientation. Please enter h for horizontal and v for vertical placement.")

                    row = ord(coordinate[0]) - ord('A')
                    col = int(coordinate[1]) 

                    if not (0 <= row < 26 and 0 <= col < 10):
                        raise ValueError("Invalid coordinate. Please try again.")

                    placed = self.board.place_ship(ship, row, col, orientation)
                    if placed:
                        print(f"{ship.name} placed successfully.")
                        self.board.print_board(reveal_ships=True)
                    else:
                        print(f"Invalid placement for {ship.name}. Try again.")
                except ValueError as e:
                    print(f"Error: {e}")


    def take_turn(self, opponent_board):
        while True:
            try:
                print("\nOpponent's board:")
                opponent_board.print_board(reveal_ships=False)  # Only show hits/misses during attack

                coordinate = input(f"{self.name}, enter the coordinate to attack (e.g., A6): ").upper()

                if len(coordinate) != 2 or not coordinate[0].isalpha() or not coordinate[1].isdigit():
                    raise ValueError("Invalid coordinate format. Please enter a coordinate like A6.")

                row = ord(coordinate[0]) - ord('A')  # Convert letter to row index
                col = int(coordinate[1])   # Convert number to column index

                # Ensure the coordinates are within bounds of the opponent's board
                if row < 0 or row >= opponent_board.height or col < 0 or col >= opponent_board.width:
                    raise ValueError("Coordinate out of bounds. Please enter a valid coordinate.")

                # Check if the spot has already been attacked (hit or miss)
                if opponent_board.grid[row][col] == 'X' or opponent_board.grid[row][col] == 'O':
                    raise ValueError("This coordinate has already been attacked. Please choose another one.")

                # Call the attack method with row and column
                if opponent_board.attack(row, col):
                    print(f"{self.name}: Hit!")
                else:
                    print(f"{self.name}: Miss!")
                break
            except ValueError as e:
                print(f"Error: {e}")


