# SOS Game
# by: Rawan Hesham
# ID: 20211040

# player 1 and 2 scores
player_1 = 0
player_2 = 0

# the table with 2D list.
table = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"]]


# function to display who is the winner.
def winner(player1score, player2score):
    if player1score > player2score:
        print()
        print("player 1 is the winner...congratulations :)")
    elif player2score > player1score:
        print()
        print("player 2 is winner...congratulations :)")
    elif player1score == player2score:
        print()
        print("Draw...good job :)")


# function to take the inputs from player 1
def player1_turn():
    global player_1, player_2
    global row, column
    global letter
    print()
    print("player 1 score : ", player_1)
    print("player 2 score : ", player_2)
    print()
    print("...player 1 turn...")
    print()
    for i in table:
        for j in i:
            print(j, end=" ")
        print()
    print()

    # take from player 1 the place he want to put the letter in.
    row, column = map(int, input("Row, Column: ").split())

    # check that the place player 1 entered is empty.
    while table[row - 1][column - 1] != "_" or row > 4 or column > 4:
        row, column = map(int, input("Not valid, enter another Row, Column: ").split())

    # take from player 1 the letter.
    letter = input("Letter (S or O): ").upper()

    # check that the letter player 1 entered is either s or o.
    while str(letter) != 'S' and str(letter) != 'O':
        letter = input("Letter (S or O): ").upper()
    # replace underscore with letter the player 1 entered.
    table[row - 1][column - 1] = letter

    # check SOS for player 1
    if "_" in table[0] or "_" in table[1] or "_" in table[2] or "_" in table[3]:
        checkSOS_player1()
    else:
        winner(player_1,player_2)

def player2_turn():
    global row, column
    global player_1, player_2
    global letter
    print()
    print("player 1 score : ", player_1)
    print("player 2 score : ", player_2)
    print()
    print("...player 2 turn...")
    print()
    for i in table:
        for j in i:
            print(j, end=" ")
        print()
    print()

    # take from player 2 the place he want to put the letter in.
    row, column = map(int, input("Row, Column: ").split())

    # check that the place player 2 entered is empty.
    while table[row - 1][column - 1] != "_" or row > 4 or column > 4:
        row, column = map(int, input("Not valid, enter another Row, Column: ").split())

    # take from player 2 the letter.
    letter = input("Letter (S or O): ").upper()

    # check that the letter player 2 entered is either s or o.
    while str(letter) != 'S' and str(letter) != 'O':
        letter = input("Letter (S or O): ").upper()

    # replace underscore with letter the player 2 entered.
    table[row - 1][column - 1] = letter

    if "_" in table[0] or "_" in table[1] or "_" in table[2] or "_" in table[3]:
        checkSOS_player2()
    else:
        winner(player_1,player_2)


# function to check SOS for player 1
def checkSOS_player1():
    global player_1
    global row
    global column
    global letter

    if letter == 'O':
        # check if the O in the edges (no possibilties)
        if row == 1 and column == 1 or row == 1 and column == 4 or row == 4 and column == 1 or row == 4 and column == 4:
            print()

        # check vertically (the only possibiltiy) if the raw is 1 or 4
        elif row == 1 or row == 4:
            if table[row - 1][column - 2] + table[row - 1][column - 1] + table[row - 1][column] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check if the row is 2 or 3
        elif row == 2 or row == 3:
            # check horizontally (the only possibilty) if the column is 1 or 4
            if column == 1 or column == 4:
                if table[row - 2][column - 1] + table[row - 1][column - 1] + table[row][column - 1] == "SOS":
                    player_1 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player1_turn()
            # check if the column is 2 or 3 (4 possibilties --> horizontally , vertically , diagonally from left and right.
            elif column == 2 or column == 3:
                # check horizontally.
                if table[row - 2][column - 1] + table[row - 1][column - 1] + table[row][column - 1] == "SOS":
                    player_1 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player1_turn()
                # check vertically
                elif table[row - 1][column - 2] + table[row - 1][column - 1] + table[row - 1][column] == "SOS":
                    player_1 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player1_turn()
                # check diagonally from left
                elif table[row - 2][column - 2] + table[row - 1][column - 1] + table[row][column] == "SOS":
                    player_1 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player1_turn()
                # check diagonally from right
                elif table[row - 2][column] + table[row - 1][column - 1] + table[row][column - 2] == "SOS":
                    player_1 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player1_turn()

    elif letter == 'S':

        # check vertically if column is 1.
        if column == 1:
            if table[row - 1][column - 1] + table[row - 1][column] + table[row - 1][column + 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check vertically if column is 4.
        elif column == 4:
            if table[row - 1][column - 1] + table[row - 1][column - 2] + table[row - 1][column - 3] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check vertically if column is 2
        elif column == 2:
            if table[row - 1][column - 1] + table[row - 1][column] + table[row - 1][column + 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check vertically if column is 3
        elif column == 3:
            if table[row - 1][column - 1] + table[row - 1][column - 2] + table[row - 1][column - 3] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check horizontally
        if row - 3 >= 0:
            if table[row - 3][column - 1] + table[row - 2][column - 1] + table[row - 1][column - 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()
        else:
            if table[row - 1][column - 1] + table[row][column - 1] + table[row + 1][column - 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        # check diagonally
        if row == 1 and column == 3 or row == 1 and column == 4:
            if table[row - 1][column - 1] + table[row][column - 2] + table[row + 1][column - 3] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        elif row == 1 and column == 1 or row == 1 and column == 2:
            if table[row - 1][column - 1] + table[row][column] + table[row + 1][column + 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        elif row == 2 and column == 3 or row == 2 and column == 4:
            if table[row - 1][column - 1] + table[row][column - 2] + table[row + 1][column - 3] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        elif row == 2 and column == 1 or row == 2 and column == 2:
            if table[row - 1][column - 1] + table[row][column] + table[row + 1][column + 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        elif row == 3 and column == 1 or row == 3 and column == 2 or row == 4 and column == 1 or row == 4 and column == 2:
            if table[row - 1][column - 1] + table[row - 2][column] + table[row - 3][column + 1] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()

        elif row == 3 and column == 3 or row == 3 and column == 4 or row == 4 and column == 3 or row == 4 and column == 4:
            if table[row - 1][column - 1] + table[row - 2][column - 2] + table[row - 3][column - 3] == "SOS":
                player_1 += 1
                print()
                print(".....Nice job you have another turn.....")
                player1_turn()



# function to check SOS for player 2
def checkSOS_player2():
    global player_2
    global row, column
    global letter

# if the letter is O
    if letter == 'O':
        # check if the O in the edges (no possibilties)
        if row == 1 and column == 1 or row == 1 and column == 4 or row == 4 and column == 1 or row == 4 and column == 4:
            print()

        # check vertically (the only possibiltiy) if the raw is 1 or 4
        elif row == 1 or row == 4:
            if table[row - 1][column - 2] + table[row - 1][column - 1] + table[row - 1][column] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check if the row is 2 or 3
        elif row == 2 or row == 3:
            # check horizontally (the only possibilty) if the column is 1 or 4
            if column == 1 or column == 4:
                if table[row - 2][column - 1] + table[row - 1][column - 1] + table[row][column - 1] == "SOS":
                    player_2 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player2_turn()
            # check if the column is 2 or 3 (4 possibilties --> horizontally , vertically , diagonally from left and right.
            elif column == 2 or column == 3:
                # check horizontally.
                if table[row - 2][column - 1] + table[row - 1][column - 1] + table[row][column - 1] == "SOS":
                    player_2 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player2_turn()
                # check vertically
                elif table[row - 1][column - 2] + table[row - 1][column - 1] + table[row - 1][column] == "SOS":
                    player_2 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player2_turn()
                # check diagonally from left
                elif table[row - 2][column - 2] + table[row - 1][column - 1] + table[row][column] == "SOS":
                    player_2 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player2_turn()
                # check diagonally from right
                elif table[row - 2][column] + table[row - 1][column - 1] + table[row][column - 2] == "SOS":
                    player_2 += 1
                    print()
                    print(".....Nice job you have another turn.....")
                    player2_turn()
    elif letter == 'S':
        # check vertically if column is 1.
        if column == 1:
            if table[row - 1][column - 1] + table[row - 1][column] + table[row - 1][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check vertically if column is 4.
        if column == 4:
            if table[row - 1][column - 1] + table[row - 1][column - 2] + table[row - 1][column - 3] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check vertically if column is 2
        elif column == 2:
            if table[row - 1][column - 1] + table[row - 1][column] + table[row - 1][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check vertically if column is 3
        elif column == 3:
            if table[row - 1][column - 1] + table[row - 1][column - 2] + table[row - 1][column - 3] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check horizontally
        if row - 3 >= 0:
            if table[row - 3][column - 1] + table[row - 2][column - 1] + table[row - 1][column - 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()
        else:
            if table[row - 1][column - 1] + table[row][column - 1] + table[row + 1][column - 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        # check diagonally
        if row == 1 and column == 3 or row == 1 and column == 4:
            if table[row - 1][column - 1] + table[row][column - 2] + table[row + 1][column - 3] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        if row == 1 and column == 1 or row == 1 and column == 2:
            if table[row - 1][column - 1] + table[row][column] + table[row + 1][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        if row == 2 and column == 3 or row == 2 and column == 4:
            if table[row - 1][column - 1] + table[row][column - 2] + table[row + 1][column - 3] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        if row == 2 and column == 1 or row == 2 and column == 2:
            if table[row - 1][column - 1] + table[row][column] + table[row + 1][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        if row == 3 and column == 1:
            if table[row - 1][column - 1] + table[row - 2][column] + table[row - 3][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()
        if row == 3 and column == 2:
            if table[row - 1][column - 1] + table[row - 2][column] + table[row - 3][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()
        if row == 4 and column == 1:
            if table[row - 1][column - 1] + table[row - 2][column] + table[row - 3][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()
        if row == 4 and column == 2:
            if table[row - 1][column - 1] + table[row - 2][column] + table[row - 3][column + 1] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()

        if row == 3 and column == 3 or row == 3 and column == 4 or row == 4 and column == 3 or row == 4 and column == 4:
            if table[row - 1][column - 1] + table[row - 2][column - 2] + table[row - 3][column - 3] == "SOS":
                player_2 += 1
                print()
                print(".....Nice job you have another turn.....")
                player2_turn()



# the main function of the game which will display the table and let players start playing.
def start_game():
    global player_1
    global player_2
    global row
    global column
    global letter

    print()
    print("welcome to SOS game, hope you to like the game...")
    print("Let's start playing...")

    while "_" in table[0] or "_" in table[1] or "_" in table[2] or "_" in table[3]:
        # player 1 turn.
        player1_turn()

        # player 2 turn
        if "_" in table[0] or "_" in table[1] or "_" in table[2] or "_" in table[3]:
            player2_turn()
        else:
            break

start_game()
