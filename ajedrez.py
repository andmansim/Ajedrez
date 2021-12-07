from typing import BinaryIO


f = open("ajedrez.txt", "w")
"""
White pieces:		
King	♔	&#x2654;
Queen	♕	&#x2655;
Rook = torre	♖	&#x2656;
Bishop = alfil	♗	&#x2657;
Knight = caballo ♘	&#x2658;
Pawn = peón	♙	&#x2659;
Black pieces:		
King = b_K	♚	&#x265a;
Queen = b_Q	♛	&#x265b;
Rook= b_R	♜	&#x265c;
Bishop= b_B	♝	&#x265d;
Knight= b_K	♞	&#x265e;
Pawn= b_P	♟	&#x265f;
"""
board = []
black = ['b_R', 'b_K', 'b_B', 'b_K', 'b_Q', 'b_B1', 'b_K1', 'b_R1']
white = ['w_R', 'w_K', 'w_B', 'w_K', 'w_Q', 'w_B1', 'w_K1', 'w_R1']
black_pawn = ['b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P', 'b_P']
white_pawn = ['w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P', 'w_P']

def boardcreation():
    
    for i in range(0,8):
        if i == 0:
            board.append(black)
        if i == 1:
            board.append(black_pawn)
        if i == 6:
            board.append(white_pawn)
        if i == 7:
            board.append(white)
        else:
            board.append(['a'] * 8)
            
                
    
boardcreation()
for x in board:
    print(" ".join(x))
