mat = [['BR1', 'BK1', 'BB1', 'BQ', 'BK', 'BB2', 'BK2', 'BR2'],
       ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8'],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

matboard = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
            ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
            ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
            ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
            ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
            ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]

chesspieces =['BR1', 'BK1', 'BB1', 'BQ', 'BK', 'BB2', 'BK2', 'BR2','BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8', 'exit']
'''count = 0
for i in mat:
    print(mat[count])
    count = count + 1
count = 0

mvpiece = input("Enter The Piece you want to move: ")
boardsq = input("Enter the Square of the board, to move piece: ")

next_loc = []'''
legalmove1 = []
legalmove2 = []


def printboard():
    topbottom = ['    ', '  A   ', '  B   ', '  C   ', ' D   ', ' E   ', ' F   ', ' G   ', ' H   ', '    ']
    sides = ['8', '7', '6', '5', '4', '3', '2', '1']
    tbspacer = ' ' * 6
    rowspacer = ' ' * 5
    cellspacer = ' ' * 4
    empty = ' ' * 3

    print()
    for field in topbottom:
        print("%4s" % field, end='')
    print()

    print(tbspacer + ("_" * 4 + ' ') * 8)

    for row in range(8):
        print(rowspacer + (('|' + cellspacer) * 9))
        print("%4s" % sides[row], ('|'), end='')

        for col in range(8):
            #               if [row, col] not in mat[row][col]:
            if col == 8:
                print(empty + '|', end='')

            else:
                if mat[row][col] == 0:
                    print(" 0 ", ('|'), end='')
                elif mat[row][col] == 'BQ':
                    print(" BQ", ('|'), end='')
                elif mat[row][col] == 'BK':
                    print(" BK", ('|'), end='')
                else:
                    print(mat[row][col], ('|'), end='')

        print("%2s " % sides[row], end='')

        print()
        print(rowspacer + '|' + (("_" * 4 + '|') * 8))

    print()

    for field in topbottom:
        print("%4s" % field, end='')

    print("\n")


def gamestarts():
    mvpiece = input("Enter The Piece you want to move: ")
    boardsq = input("Enter the Square of the board, to move piece: ")
    printboard()
    if mvpiece == 'exit' or mvpiece == 'Exit':
        quit()

    if mvpiece not in chesspieces:
        print("Not a Valid chess Piece, Please try again")
        gamestarts()
    present=0
    for i in range(8):
        for j in range(8):
            if matboard[i][j] == boardsq:
                present=1
    if(present==0):
        print("Square is not present in chessboard, Please try again")
        gamestarts()

    currpos = find_in_list_of_list(mat, mvpiece)
    curr_pos = list(currpos)
    print(" Current position of ",mvpiece," is ",curr_pos)
    desloc = find_des_inlist(matboard, boardsq)
    des_loc = list(desloc)
    if des_loc[0] > 7 or des_loc[1] > 7 or des_loc[0] < 0 or des_loc[1] < 0:
        print("Invalid Destination square (Out of Board)")
        mvpiece = 'exit'
    else:
        print("Destination Position of ", mvpiece, " is: ", des_loc)
    pieceloc(mvpiece)
    move_piece(mvpiece,des_loc,curr_pos)
    updatemat(curr_pos,des_loc,mvpiece)


def find_in_list_of_list(mat, mvpiece):
    for sub_list in mat:
        if mvpiece in sub_list:
            return (mat.index(sub_list), sub_list.index(mvpiece))
    raise ValueError("'{char}' is not in list".format(char=mvpiece))


def find_des_inlist(matboard, boardsq):
    for sub_list1 in matboard:
        if boardsq in sub_list1:
            return (matboard.index(sub_list1), sub_list1.index(boardsq))
    raise ValueError("'{char}' is not in list".format(char=boardsq))



def pieceloc(mvpiece):
    pieceAvb = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (mat[i][j] == mvpiece):
                pieceAvb = 1
                print("The piece is currently in the board at Square", matboard[i][j])


    if (pieceAvb == 0):
        print("Chess Piece not available on Board")


def brook1(des_loc,curr_pos):
    for i in range(0, 8):
        legalmove1.append([i, curr_pos[0]])
        legalmove2.append([curr_pos[1], i])
    print("Legal Moves are as follows:\n ", legalmove1, legalmove2)
    if des_loc in legalmove1 or des_loc in legalmove2:
        print("The move is legal. The rook proceeds")

    #    for i in range(0,8):
    print("Yay it's a Rook")


def brook2(des_loc,curr_pos):
    for i in range(0, 8):
        legalmove1.append([i, curr_pos[0]])
        legalmove2.append([curr_pos[1], i])
    print("Legal Moves are as follows:\n ", legalmove1, legalmove2)
    if des_loc in legalmove1 or des_loc in legalmove2:
        print("The move is legal. The rook proceeds")
    print("Yay it's a brook2")


def bknight1(des_loc,curr_pos):
    Xk = [2, 1, -1, -2, -2, -1, 1, 2]
    Yk = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(0, 8):
        xkp = curr_pos[0] + Xk[i]
        Ykp = curr_pos[1] + Yk[i]
        legalmove1.append([xkp, Ykp])
    if des_loc in legalmove1:
        print("The move is legal. The knight proceeds")
    print("Yay it's a bknight1")


def bknight2(des_loc,curr_pos):
    Xk = [2, 1, -1, -2, -2, -1, 1, 2]
    Yk = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(0, 8):
        xkp = curr_pos[0] + Xk[i]
        Ykp = curr_pos[1] + Yk[i]
        legalmove1.append([xkp, Ykp])
    if des_loc in legalmove1:
        print("The move is legal. The knight proceeds")
    print("Yay it's  bknight2")


def bbishop1(des_loc,curr_pos):
    dx = abs(des_loc[0] - curr_pos[0])
    dy = abs(des_loc[1] - curr_pos[1])
    if (dx == dy) and (dx > 0):
        print("It's a legal move for bishop")
    else:
        print("Illegal move of Bishop")
    print("Yay it's a bbishop1")


def bbishop2(des_loc,curr_pos):
    dx = abs(des_loc[0] - curr_pos[0])
    dy = abs(des_loc[1] - curr_pos[1])
    if (dx == dy) and (dx > 0):
        print("It's a legal move for bishop")
    else:
        print("Illegal move of Bishop")
    print("Yay it's a bbishop2")


def bking(des_loc,curr_pos):
    if des_loc[0] == (curr_pos[0] - 1) and des_loc[1] == (curr_pos[1] + 1):
        print("legal Move of King")
    elif des_loc[0] == curr_pos[0] and des_loc[1] == (curr_pos[1] + 1):
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0] + 1) and des_loc[1] == (curr_pos[1] + 1):
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0] - 1) and des_loc[1] == curr_pos[1]:
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0] + 1) and des_loc[1] == curr_pos[1]:
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0] - 1) and des_loc[1] == (curr_pos[1] - 1):
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0]) and des_loc[1] == (curr_pos[1] - 1):
        print("legal Move of King")
    elif des_loc[0] == (curr_pos[0] + 1) and des_loc[1] == (curr_pos[1] - 1):
        print("legal Move of King")
    else:
        print("Illegal Move of King")


def bqueen(des_loc,curr_pos):
    if (curr_pos[0] == des_loc[0] or curr_pos[1] == des_loc[0] or abs(curr_pos[0] - des_loc[0]) == abs(
            curr_pos[1] - des_loc[1])):
        print("It's a legal move of Queen")
    else:
        print("Illegal Move of queen")
    print("Yay it's a bqueen")


def bpawn(des_loc, curr_pos):
#    print("des_loc[1] - curr_pos[1]: ",(des_loc[1] - curr_pos[1]))
#    print("des_loc[0], curr_pos[0], des_loc[1] , curr_pos[1] :", des_loc[0], curr_pos[0], des_loc[1], curr_pos[1])
    if (des_loc[0] - curr_pos[0] == 1):
        print("It's a legal move")
    else:
        print("Illegal move of Pawn")
    print("Yay it's a bpawn")

def updatemat(curr_pos,des_pos,mvpiece):
    curr_pos=list(curr_pos)
    mat[curr_pos[0],curr_pos[1]] = 0
    mat[des_pos[1],des_pos[0]] = 'mvpiece'
    printboard()



def move_piece(mvpiece,des_loc,curr_pos):
    if (mvpiece == "BR1"):
        brook1(des_loc,curr_pos)
        updatemat(curr_pos,des_loc,mvpiece)

    elif (mvpiece == "BK1"):
        bknight1(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BB1"):
        bbishop1(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BK"):
        bking(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BQ"):
        bqueen(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BR2"):
        brook2(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BK2"):
        bknight2(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BB2"):
        bbishop2(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BP1" or mvpiece == "BP2" or mvpiece == "BP3" or mvpiece == "BP4" ):
        bpawn(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "BP5" or mvpiece == "BP6" or mvpiece == "BP7" or mvpiece == "BP8" ):
        bpawn(des_loc,curr_pos)
        gamestarts()
    elif (mvpiece == "exit"):
        print("ending the game. Thanks")
    else:
        pass

a = gamestarts()
