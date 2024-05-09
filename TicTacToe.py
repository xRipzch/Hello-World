import random

print("Welcome to Tic Tac Toe!")
name = input("Hello, please state your name: ")
print("Hello", name)
print("_________________________________________________")


possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printBoard():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end = " ")
        for j in range(cols):
            print("", gameBoard[i][j], end = " |")
    print("\n+---+---+---+")        

def modifyArray(num, turn):
    num -= 1
    if (num == 0):
        gameBoard[0][0] = turn
    elif (num == 1):
        gameBoard[0][1] = turn
    elif (num == 2):
        gameBoard[0][2] = turn
    elif (num == 3):
        gameBoard[1][0] = turn
    elif (num == 4):
        gameBoard[1][1] = turn
    elif (num == 5):
        gameBoard[1][2] = turn
    elif (num == 6):
        gameBoard[2][0] = turn
    elif (num == 7):
        gameBoard[2][1] = turn
    elif (num == 8):
        gameBoard[2][2] = turn


def checkForWinner(gameBoard):
    # Check for 'X' winning
    if (
        (gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X') or
        (gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X') or
        (gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X') or
        (gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X') or
        (gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X') or
        (gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X') or
        (gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X') or
        (gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X')
    ):
        print("X has won!")
        return "X"
    # Check for 'O' winning
    elif (
        (gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O') or
        (gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O') or
        (gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O') or
        (gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O') or
        (gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O') or
        (gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O') or
        (gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O') or
        (gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O')
    ):
        print("O has won!")
        return "O"
    else:
        return "N"
    
winner = checkForWinner(gameBoard)
if winner == "N":
    print("No winner yet.")
leaveLoop = False
turnCounter = 0

while (leaveLoop == False):
    ## Player's turn
    if(turnCounter % 2 == 1):
        printBoard()
        numberPicked = int(input("\nPlease pick a number: "))
        if (numberPicked >= 1 or numberPicked <= 9):
            modifyArray(numberPicked, "X")
            possibleNumbers.remove(numberPicked)
            winner = checkForWinner(gameBoard)
            if winner != "N":
                print("Player X has won!")
                leaveLoop = True
        else:
            print("Invalid number. Please try again.")
        turnCounter += 1
    ## Computers turn
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers)
            print("\n Cpu choice: ", cpuChoice)
            if (cpuChoice in possibleNumbers):
                modifyArray(cpuChoice, "O")
                possibleNumbers.remove(cpuChoice)
                winner = checkForWinner(gameBoard)
                if winner != "N":
                    print("Player O has won!")
                    leaveLoop = True
                turnCounter += 1
                breakA