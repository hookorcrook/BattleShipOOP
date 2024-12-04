"Battleship!".

The game begins will each player having a board with NxM grid locations on it and a number of ship pieces to place.
The ships are placed by each player in secret onto the board.  Each player never sees the others board during the game.
Each ship spans several grid spaces and can only be placed on the board either within a column or within a row.
The number of grid spaces on the board a ship spans is the number of hits on it required to sink the ship.
Diagonal placement of a ship is not allowed!
Once the ship pieces are placed by each player the game begins.
Each player is allowed to select a location on the board as a guess for the location of an enemy ship. 
Each guess is recorded as a hit or miss is noted via an 'X' or 'O' marker at the grid location guessed.
Each player gets a turn to guess alternating from player 1 to player 2....
Each player builds up a "mapping" of the board with misses and hits in an attempt to locate and destroy all of the other players ships.
The game continues until all of the ships for one of the players have received their maximum number of hits.
The surviving player is the winner.
Your application will allow the game to be played on a single PC shared by the two players.
This will require you to carefully consider the turn hand off from one player to another.
A high score and all of the results of prior games should be kept via a file (Players and who won).  The format of this file is up to you.
A high score will be the minimum number of guesses made by a player during a game to win.
Your application should start off by recording the name of each Player.
Then the application should allow each player independently and secretly to place their pieces.
Our board will be composed of 26 rows (A-Z) and 10 columns (0-9).
Again, each player has a board that is used to capture their ship locations as well as the guesses of the opposing player.
Our game will contain 5 ships.

1.  2 Destroyers occupying 3 spaces (3 hits to sink)
2.  1 Cruiser occupying 5 spaces (5 hits to sink)
3.  1 Battleship occupying 7 spaces (7 hits to sink)
4.  1 Aircraft Carrier 9 spaces (9 hits to sink)

The placement of a ship onto the board will be via the middle space of the ship.
Since all of our ships have odd space spans this provides an unambiguous placement point. 
For example for a Destroyer if we place it within row A at column 5 it will occupy the following spaces A4, A5,A6.
The placement of a ship should request from the user the alignment of (horizontal or vertical) the ship and where to place it.
Error checking must be done to ensure the ship is placed correctly and/or within the board completely. 
If a ship is miss placed, then the user should be asked to replace it.
Each player should be asked to enter their ship placements in secret.
In addition, when a player completely places their ships the placement should be provided to them with a confirmation that this is the board they would like to play with.
Ship replacement should be supported if a player wants to change their ship placement (either for all or a selected ship).
When the players are complete placing their associated ships, a question should be asked if they would like to begin play.
Play should begin with player 1.
Each player will be given a chance to guess a position.  
The active player (guessing player) and their associated guess board (see below) should be displayed during their guess period.
The guess board should be represented with a formatted output like the following clearly indicating the active player along with the row, columns, hits and misses.

Player 1 Turn
         1 2 3 4 5 6 7 8 9
A.     0XX
B
C
D


With an '0" representing a miss and 'X' representing a hit from prior guesses.
The player will enter their guess as row, column for example A,1.
This input will be error checked and the user asked for reentry if required (incorrect format or already guessed).
The guess will be checked to see if a ship was hit and the result will be displayed as, "MISS", "HIT", "SHIP SUNK".
"SHIP SUNK will be displayed if and only if a ship receives its maximum number of hits.  This will take the sunk ship out of action for the opposing player.
Play will continue alternating players until all of the ships of one player are knocked out (receive their maximum number of hits).
The winning player will be displayed along with each players guess board with the location of ships not hit noted with the character 'S'.
The game statistics will be saved to a file as a record (number of turns, number of remaining ships for the winning player along with the winning player name).
In addition, when a game is started the existing high score will be displayed.  The high score will be the game in which the winning player has the lowest number of guesses.

