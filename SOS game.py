# design board game
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", "-",
         ]
S = "S"
O = "O"
winner = None
gameRunning = True
player1Points = 0
player2Points = 0
i = 0
boardCounter = 0


# print the game board
def printBoard(board):
    print("player1Points= ", player1Points)
    print("player2Points= ", player2Points)
    print(board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23] + " | " + board[24])
    print("------------------")
    print(board[29] + " | " + board[30] + " | " + board[31] + " | " + board[32] + " | " + board[33])
    print("------------------")
    print(board[38] + " | " + board[39] + " | " + board[40] + " | " + board[41] + " | " + board[42])
    print("------------------")
    print(board[47] + " | " + board[48] + " | " + board[49] + " | " + board[50] + " | " + board[51])
    print("------------------")
    print(board[56] + " | " + board[57] + " | " + board[58] + " | " + board[59] + " | " + board[60])


# player's turn
def swichPlayer():
    global i
    if i % 2 == 0:
        print("player1 turn")

    elif i % 2 == 1:
        print("player2 turn")


# take player input
def playerInput(board):
    global inp, i, inp1, boardCounter
    inp1 = str(input("choose S or O:")).strip().capitalize()
    if inp1 == S or inp1 == O:
        while True:
            try:
                inp = int(input("enter a number 1-25:"))
                if str(inp).isdigit():
                    break
            except:
                print(" input must be integer between 1 and 25 ")

        if 1 <= inp <= 25:
            if inp1 == "S":
                if board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] == "-":
                    board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] = S
                else:
                    print("spot already chosen")
                    return playerInput(board)
                    i -= 1
                    boardCounter -= 1

            elif inp1 == "O":
                if board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] == "-":
                    board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] = O

                else:
                    print("spot already chosen")
                    return playerInput(board)
                    i -= 1
                    boardCounter -= 1


        else:
            print("wrong input, number must be <= 25 or >= 1")
            return playerInput(board)
            i -= 1
            boardCounter -= 1
    else:
        print("wrong input, please choose S or O only!")
        return playerInput(board)
        i -= 1
        boardCounter -= 1


# check points
def Check(board):
    global winner, player2Points, player1Points, i, inp, inp1
    count = 0
    if inp1 == S or inp1 == O:
        if 1 <= inp <= 25:
            if board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] == O:  # check points if input is O
                # Horizontal check
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 1] == board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 1] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Vertical check
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 9] == board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 9] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Positive Slope check
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 8] == board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 8] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Negative slope check
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 10] == board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 10] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass




            elif board[inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9] == S:  # check points if the input is S
                # Horizontal check (right)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 1] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 2] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Horizontal check (left)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 1] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 2] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Vertical check (up)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 9] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 18] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Vertical check (down)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 9] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 18] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Positive slope check (up)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 8] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 16] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Positive slope check (down)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 8] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 16] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Negative slope check (up)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 10] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) - 20] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1
                except:
                    pass
                # Negative slope check (down)
                try:
                    if board[(inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 10] == O and board[
                        (inp - (5 * ((inp - 1) // 5)) + 19 + ((inp - 1) // 5) * 9) + 20] == S:
                        if i % 2 == 0:
                            player1Points += 1
                            i = 0
                        elif i % 2 == 1:
                            player2Points += 1
                            i = 1
                        count += 1

                except:
                    pass
            if count >= 1:
                i += 1


# check win or tie
def Win():
    global boardCounter
    if boardCounter == 24:
        if player1Points > player2Points:
            print("Player 1 wins")
            exit()
        elif player2Points > player1Points:
            print("player 2 wins")
            exit()
        else:
            print("it is a tie, restart the game")
            exit()


while gameRunning:
    swichPlayer()
    printBoard(board)
    playerInput(board)
    Check(board)
    Win()
    boardCounter += 1
    i += 1
