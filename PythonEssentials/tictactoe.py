from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # solução fornecida:
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
# 2ª tentativa, parcialmente inspirada na solução apresentada
    while True:
            move = int(input("Enter your move: ")) - 1
            
            if move < 0 or move > 9:
                print("This is not a valid position.")
                continue            
            
            row = move // 3
            col = move % 3
            sign = board[row][col]

            if board[row][col] in ["X", "O"]:
                    print("This position is not free. Try again.")
                    continue
            else:
                board[row][col] = "O"
                break

    # 1ª tentativa de escrever a função.
    # Foi descartada pela dificuldade de leitura do código, por conta da lista de tuplas
    # usada para mapear as posições das casas, o que era desnecessário
    '''
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
    '''            
       

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
 
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_fields.append((row, col))
    
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    # Solução parcialmente fornecida pelo exercício
    player = 0
    if sign == "X":
        player == "Computer"
    elif sign == "O":
        player == "You"

    cross1 = cross2 = True
    for pos in range(3):
        if board[pos][0] == sign and board[pos][1] == sign and board[pos][2] == sign:
            return player
        if board[0][pos] == sign and board[1][pos] == sign and board[2][pos] == sign:
            return player
        if board[pos][pos] != sign:
            cross1 = False
        if board[2 - pos][2 - pos] != sign:
            cross2 = False

    if cross1 or cross2:
	    return player
    else: 
        return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
 	
    #Solução fornecida pelo exercício
    free = make_list_of_free_fields(board) # make a list of free fields
    cnt = len(free)
    if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'
    return


# Gerar um jogo da velha vazio:

board = [ [x, x+1, x+2] for x in range(1, 10, 3)]
print(board[1][1])
board[1][1] = "X"
print(board[1][1])
humanTurn = True

# Precisa corrigir a condição de controle para sair do loop quando houver vitória
while make_list_of_free_fields(board) != []:
    # O board sempre precisa aparecer no começo de cada passagem pelo loop:
    display_board(board)

    if humanTurn:
        enter_move(board) 
        if victory_for(board, "X") == "Computer":
            winner = victory_for(board, "X")
            print(winner)
            break
    else:
        draw_move(board)
        if victory_for(board, "O") == "You":
            winner = victory_for(board, "O")
            print(winner)
            break
    
    humanTurn = not humanTurn		
else:
    print("Game over! Start again!")


    
draw_move(board)
if winner == "Computer":
	print("I won!")
elif winner == "You":
	print("You won")
else:
	print("Tie!")


