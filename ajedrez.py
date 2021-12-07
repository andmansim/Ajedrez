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

f = open("ajedrez.txt", "w")
for x in range(0,8):
    for y in range(0,8):
        
        if y == 7: 
            f.write(str(board[x][y] + '\n'))
        else:
            f.write(str(board[x][y]) + '\t')
    
f.close()