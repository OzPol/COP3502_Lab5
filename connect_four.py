#This block defines a function to print the board
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print()



#This block defines a function to initialize the board with empty spaces
def initialize_board(num_rows, num_cols):
    #Initializes the board with empty spaces.
    return [["-" for _ in range(num_cols)] for _ in range(num_rows)]



#This block defines a function to insert a chip into the specified column
def insert_chip(board, col, chip_type):
    # Starts at the bottom of the board and works up until an empty space is found
    row = len(board) - 1
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == "-":
            board[i][col] = chip_type
            row = i
            break
    return row

#This block define a function to check if the specified chip type has won the game
def check_if_winner (board, col, row, chip_type):
    # check horizontally
    count = 0
    for j in range (len(board[0])):
        if board[row][j] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # check vertically
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # no winner yet
    return False



# This block defines a function to check if the specified chip kind won the game
def draw_game_yes(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '-':
                return False
    return True


#Main Loop for the game
if __name__ == "__main__":
    # Prompt the user for an imput to get board dimensions 
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    
    board = initialize_board(num_rows, num_cols)    #initializes the board
    print_board(board)          # prints the empty board

    #defines the player tokens/chip types
    print("Player 1: x ")
    print("Player 2: o\n")

    player1_token = "x"
    player2_token = "o"


    #game play
    draw_game = False
    while not draw_game:
        res = False
    
        #Player1's turn
        print("Player 1: Which column would you like to choose?")
        col = int(input())
        row = insert_chip(board, col, player1_token)
        print_board(board)

        #check to see if player 1 won the game
        res = check_if_winner(board, col, row, player1_token)
        if res:
            print("\nPlayer 1 won the game!")
            break

        #check if no winner/draw
        draw_game = draw_game_yes(board)
        if draw_game:
            print("\nDraw. Nobody wins.")
            break

        #Player 2's turn
        print("Player 2: Which column would you like to choose?")
        col = int(input())
        row = insert_chip(board, col, player2_token)
        print_board(board)

        #check to see if player 2 won the game
        res = check_if_winner(board, col, row, player2_token)
        if res:
            print("\nPlayer 2 won the game!")
            break
        
        
        #check if no winner/draw
        draw_game = draw_game_yes(board)
        if draw_game:
            print("\nDraw. Nobody wins.")
            break

