
board = [[0 for i in range(8)] for i in range (8)]
pieces = []
sensor_input = TestCases.output

def interface():
    for row in board:
        for col in row:
            if col != 0:
                if col.getColor() == "B":
                    print(BLUE + col.getSymbol() + RESET, end= "  ")
                else:
                    print(RED + col.getSymbol() + RESET, end = "  ")
            else:
                print(col, end="  ")
        print()

def updateBoard():
    globals()['board'] = [[0 for i in range(8)] for i in range(8)]
    for piece in pieces:
        if not piece.getTaken():
            position = piece.getPosition()
            globals()['board'][position[0]][position[1]] = piece

def col_splitting(arr):
    new_arr = []
    for i in range(8):
        new_arr.append(arr[i*8:i*8+8])

    return new_arr

def flatten_2d(board):
    flat_board = []
    for row in board:
        for col in row:
            flat_board.append(col)

    return flat_board

def difference_list(old, new):
    old = flatten_2d(old)
    new = flatten_2d(new)
    difference_board = [x-y for x,y in zip(old,new)]
    organized_board = col_splitting(difference_board)
    return organized_board

def difference_location(difference_board):
    row_position = 0
    for row in difference_board:
        col_position = 0
        for col in row:
            if col != 0:
                break
            col_position += 1
        if col != 0:
            break
        row_position += 1

    return (row_position, col_position)

def organize_input(inp):
    sensor_input = inp
    length = len(sensor_input)

    if length == 256:
        first = sensor_input[:64]
        first = col_splitting(first)

        second = sensor_input[64:128]
        second = col_splitting(second)

        third = sensor_input[128:192]
        third = col_splitting(third)

        fourth = sensor_input[192:]
        fourth = col_splitting(fourth)

        capturing_piece(first,second,third, fourth)


    if length == 192:
        first = sensor_input[:64]
        first = col_splitting(first)

        second = sensor_input[64:128]
        second = col_splitting(second)

        third = sensor_input[128:]
        third = col_splitting(third)

        moving(first,second,third)

def moving(first, intermediate, final):
    first_change = difference_list(first, intermediate)
    second_change = difference_list(intermediate,final)

    piece_pos = difference_location(first_change)
    move_pos = difference_location(second_change)

    move(piece_pos,move_pos)

def capturing_piece(initial_board, second, third, final_board):
    # print(initial_board,second,third,final_board,sep='\n\n')

    first_change = difference_list(initial_board,second)
    second_change = difference_list(second, third)
    final_change = difference_list(third, final_board)

    first_position = difference_location(first_change)
    second_position = difference_location(second_change)
    final_position = difference_location(final_change)

    # print(first_position,second_position,final_position)

    if second_position == final_position:
        move(first_position, final_position)
    else:
        move(second_position,final_position)

def move(old,new):
    piece = board[old[0]][old[1]]
    piece.setPosition(new)

    if board[new[0]][new[1]] != 0:
        board[new[0]][new[1]].capture()

    updateBoard()

class Piece:
    def __init__(self, symbol, color, position):
        self.symbol = symbol
        self.color = color
        self.position = position
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
