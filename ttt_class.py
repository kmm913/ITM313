# import the random function to generate choices for the CPU player
import random

class ttt:

    @staticmethod
    def drawBoard(board):
        print(board[7], board[8], board[9])
        print(board[4], board[5], board[6],)
        print(board[1], board[2], board[3], "\n\n")
    
    @staticmethod
    def setSquare(numPlayers, currentPlayer, board):
        if numPlayers == 2: 
            i = int(input("Please choose a square (1-9): "))
            if currentPlayer == 1:
                board[i] = "X"
            else:
                board[i] = "O"
        elif numPlayers == 1:
            if currentPlayer == 1:
                i = int(input("Please choose a square (1-9): "))
                board[i] = "X"
            else:
                i = random.randint(1,9)                
                while board[i] == "X" or board[i] == "O":
                    i = random.randint(1,9)
                print("The computer chose " + str(i))
                board[i] = "O"

    @staticmethod
    def setNumPlayers():
        numPlayers = int(input("Enter the number of human players (1 or 2): \n"))
        return numPlayers
    
    @staticmethod
    def swapCurrentPlayer(currentPlayer):
        if currentPlayer == 1:
            currentPlayer = 2
        else:
            currentPlayer = 1
        return currentPlayer

    @staticmethod
    def checkForWinner(currentPlayer, board, winning_sets):
        winner = False
        for a, b, c in winning_sets:
            if board[a] == board[b] == board[c]:
                print("Player " + str(currentPlayer) + " wins!")
                winner = True
                break
            elif sum((pos == "X" and pos =="O") for pos in board) == 9:
                print("It's a draw.\n")
                winner = True
                break
        return winner


