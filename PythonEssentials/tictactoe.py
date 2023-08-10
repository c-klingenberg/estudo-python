board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

board_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print( """ 
            +-------+-------+-------+
            |       |       |       |
            |   1   |   2   |   3   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   4   |   5   |   6   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   7   |   8   |   9   |
            |       |       |       |
            +-------+-------+-------+
            """
            )


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:
        move = int(input("Enter your move: "))
        
        if move > 0 or move < 10:           
            if board[board_positions[move-1][0]][board_positions[move-1][1]] not in ["X", "O"]:
                board[board_positions[move-1][0]][board_positions[move-1][1]] = "O"
                break
            elif board[board_positions[move-1][0]][board_positions[move-1][1]] in ["X", "O"]:
                print("This position is not free.")
        else: 
            print("This is not a valid position.")
            

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
 
    fields = ()
    for positon in range(9):
        if board[board_positions[pos][0]][board_positions[pos][1]] not in ["X", "O"]:
            free_fields = fields + (pos,)
    return free_fields





def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
