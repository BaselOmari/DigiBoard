'''
NOTES:
    Facing a lot of issues with passing by reference, have changed configuration to assigning return values.
'''

''' Notation Coordinates (row, col), thus a1 would be (7,0), 7th row and 0th column (CS Notation)'''
''' Piece symbol:
        p: Pawn
        B: Bishop
        N: Knight
        R: Rook
        Q: Queen
        K: King        
'''

piece_number = 4
row_number = 8
col_number = 8


class Piece:
    def __init__(self, s, c, p):
        self.symbol = s
        self.color = c
        self.position = p
        self.taken = False

    def setPosition(self, new_position):
        self.position = new_position

    def capture(self):
        self.taken = True

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def getSymbol(self):
        return self.symbol

    def getTaken(self):
        return self.taken

'''
updateBOARD FUNCTION
    1. Resets board to 0s
    2. Reads through the pieces stored in the pieces list
    3. If piece is not captured, its position on this board stores this object.
'''
def updateBoard(board_ub,pieces_ub):
    board_ub = [[0 for i in range(col_number)] for i in range(row_number)]
    for piece in pieces_ub:
        if not piece.getTaken():
            position = piece.getPosition()
            board_ub[position[0]][position[1]] = piece
    
    return board_ub,pieces_ub

'''
INPUT ARRANGEMENT FUNCTION:
    1. Takes in Serial read string
    2. Derives Move Number
    3. Decides if move made, was a capture or not and redirects accordingly
        a. If move number == 3: No piece was captured
        b. If move number == 4: Piece was captured
'''
def input_arrangement(board_ia,pieces_ia,board_string):
    moves_num = int(len(board_string)/(col_number*row_number))
    arranged_moves = arrange_moves(board_string,moves_num)

    if moves_num == 3:
        board_ia, pieces_ia = moving(board_ia,pieces_ia,arranged_moves)
    elif moves_num == 4:
        board_ia, pieces_ia = capturing_piece(board_ia,pieces_ia,arranged_moves)
    
    return board_ia, pieces_ia

'''
ARRANGE MOVES FUNCTION + COL_SPLTTING:
    Converts Serial String into List (similar to board-layout) of all moves
    1. Arrange Moves splits string into multiple strings of each move
    2. Col_splitting splits string to array
'''
def arrange_moves(board_string, move_number):
    moves = []
    for i in range(move_number):
        moves.append(col_splitting(board_string[i*(col_number*row_number):(i+1)*(col_number*row_number)]))
    return moves

def col_splitting(arr):
    new_arr = []
    for i in range(row_number):
        row_arr = [int(notation) for notation in arr[i*col_number:i*col_number+col_number]]
        new_arr.append(row_arr)
    return new_arr


'''
DIFFERENCE LIST
    Takes Board image in two consecutive positions and determines location of change
'''
def difference_list(old, new):
    for r in range(row_number):
        for c in range(col_number):
            if (old[r][c] != new[r][c]):
                return (r,c)

'''
MOVING FUNCTION:
    1. Determines, the piece old and new_position using the DIFFERENCE LIST function
    2. Calls move function on these positions
'''
def moving(board_mg,pieces_mg,move_array):
    piece_position = difference_list(move_array[0], move_array[1])
    new_position = difference_list(move_array[1], move_array[2])

    board_mg, pieces_mg = move(board_mg,pieces_mg,piece_position,new_position)
    return board_mg, pieces_mg



'''
CAPTURING PIECE:
    1. Determines, the positions of the left of the two pieces and piece drop using the DIFFERENCE LIST function
    2. Checks which piece was moved by comparing position of lifts and drops.
    3. Calls move fynction on appropriate positions and pieces
'''

def capturing_piece(board_cp,pieces_cp,move_array):
    first_piece_lift = difference_list(move_array[0], move_array[1])
    second_piece_lift = difference_list(move_array[1], move_array[2])
    piece_drop = difference_list(move_array[2], move_array[3])

    if first_piece_lift == piece_drop:
        board_cp, pieces_cp = move(board_cp,pieces_cp,second_piece_lift, piece_drop)
    else:
        board_cp, pieces_cp = move(board_cp,pieces_cp,first_piece_lift, piece_drop)
    
    return board_cp, pieces_cp
    



'''
MOVE FUNCTION:
    - Takes in old position of the piece and the new position the piece moves to
    - If piece moves to a piece where an existing piece is, that piece is captured (Captured variable = True)
'''

def move(board_m,pieces_m,old,new):
    piece_m = board_m[old[0]][old[1]]
    piece_m.setPosition(new)

    if board_m[new[0]][new[1]] != 0:
        board_m[new[0]][new[1]].capture()

    board_m, pieces_m = updateBoard(board_m,pieces_m)

    return board_m, pieces_m


'''
STARTING POSITION:
    1. Initiatializes the appropriate instances of pieces
    2. Sets positions of pieces to appropriate position on the board 
'''
def starting_board(board_sb, pieces_sb):
    board_sb = [[0 for i in range(col_number)] for i in range (row_number)]
    pieces_sb = []

    for x in range(2):
        if x == 0:
            color = 'W'
            row = 7
            p_row = 6
        else:
            color = 'B'
            row = 0
            p_row = 1
        
        # Pawns
        for i in range(8):
            pieces_sb.append(Piece('p', color, (p_row,i)))
        
        # King
        pieces_sb.append(Piece('K',color,(row,4)))

        # Queen
        pieces_sb.append(Piece('Q', color, (row, 3)))

        # Knights
        pieces_sb.append(Piece('N', color, (row, 1)))
        pieces_sb.append(Piece('N', color, (row, 6)))

        # Bishops
        pieces_sb.append(Piece('B', color, (row, 2)))
        pieces_sb.append(Piece('B', color, (row, 5)))

        # Rooks
        pieces_sb.append(Piece('R', color, (row, 0)))
        pieces_sb.append(Piece('R', color, (row, 7)))


    board_sb, pieces_sb = updateBoard(board_sb,pieces_sb)
    return board_sb, pieces_sb

        
'''
PRINT BOARD (for testing purposes):
    Prints board to console
'''
def printBoard(board_pb):
    for row in board_pb:
        for square in row:
            if square == 0:
                print(0, end = ' ')
            else:
                print(square.getSymbol(), end = ' ')
        print()
