board = []
black = ['b_R', 'b_K', 'b_B', 'b_K', 'b_Q', 'b_B1', 'b_K1', 'b_R1']
white = ['w_R', 'w_K', 'w_B', 'w_K', 'w_Q', 'w_B1', 'w_K1', 'w_R1']
black_pawn = ['b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P']
white_pawn = ['w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P']

def boardcreation():
    
    for i in range(0,8):
        if i == 0:
            board.append(black)
        elif i == 1:
            board.append(black_pawn)
        elif i == 6:
            board.append(white_pawn)
        elif i == 7:
            board.append(white)
        else:
            board.append(['_'] * 8)
              
boardcreation()

for x in board:
    print("  ".join(x))

print("Usuary put here a name for your file: ")
usuary = str(input())

f = open( usuary + ".txt", "w")
f.write("Board chess" + '\n')
for x in range(0,8):
    for y in range(0,8):
        
        if y == 7: 
            f.write(str(board[x][y] + '\n'))
        else:
            f.write(str(board[x][y]) + '\t')
    
f.close()

question1 = "Do you want to continue playing?: Y/N "
print(question1)
answer = str(input())
movement = 0
while answer == "Y":
    # answers and questions
    print("What piece do you want to move? (Put the line and column where it is,lines and columns are from 0 to 7):")
    print("Line of the piece:")
    line = int(input())
    print("Column of the piece:")
    column = int(input())
    print("Line of the new position:")
    new_line = int(input())
    print("Column of the new position:")
    new_column = int(input())
    
    movement = movement + 1
    # modification of the board
    
    board[new_line][new_column] = board[line][column]
    board[line][column] = " "
    for x in board:
        print(" ".join(x))
    
    f = open( usuary + ".txt", "a")
    f.write(str(movement) + " movement" + '\n')
    for x in range(0,8):
        for y in range(0,8):
        
            if y == 7: 
                f.write(str(board[x][y] + '\n'))
            else:
                f.write(str(board[x][y]) + '\t')
    
    f.close()
    question1 = "Do you want to continue playing?: Y/N "
    print(question1)
    answer = str(input())
if answer != "Y":
    print("The game have finished")
    f = open( usuary + ".txt", "r")  
    for line in f:
        print(line)
    
    f.close()