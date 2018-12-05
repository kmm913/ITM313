# import custom class
from ttt_class import ttt

# declare variables
# The "board" list (array) below holds the board positions/squares. The "[None]" element occupies array position 0. The board is thus set up to mimic a numpad.
board = [None] + list(range(1,10)) 

# the "winning_sets" list (array) below holds the possible winning sets of squares; the checkForWinner function references this list. 
winning_sets = [ 
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
]

numPlayers = 1 #sets default number of players to 1, can be changed before the game starts
currentPlayer = 1 #sets starting player to player 1
winner = False  #flag to declare a winner and end the game loop

#begin game
print("Welcome to Tic Tac Toe\n")
numPlayers = ttt.setNumPlayers() #choose to play against the CPU or another human player
ttt.drawBoard(board)
#loop while players select squares, until there is a winner or no remaining squares (i.e., a draw)
while winner == False:    
    ttt.setSquare(numPlayers, currentPlayer, board)
    ttt.drawBoard(board)
    winner = ttt.checkForWinner(currentPlayer, board, winning_sets)
    currentPlayer = ttt.swapCurrentPlayer(currentPlayer)