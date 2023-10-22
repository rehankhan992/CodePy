###################################################################################################
#Matrices to show the position of chess pieces on the board
###################################################################################################
mat = [['BR1', 'BK1', 'BB1', 'BQ', 'BK', 'BB2', 'BK2', 'BR2'],
       ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8'],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

######################################################################################################
# Matrices for the position of squares on the chess board
######################################################################################################

matboard = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
            ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
            ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
            ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
            ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
            ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]


#########################################################################################
# Function to check the exceptions, initial illegal moves and illegal board squares
#########################################################################################
def gamestarts(mvpiece, boardsq, piece_coord):
       chesspieces = ['BR1', 'BK1', 'BB1', 'BQ', 'BK', 'BB2', 'BK2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                      'BP7', 'BP8', 'exit']

       printboard()
       if mvpiece == 'exit' or mvpiece == 'Exit':
              quit()

       if mvpiece not in chesspieces:
              print("Not a Valid chess Piece")

       present = 0
       for i in range(8):
              for j in range(8):
                     if matboard[i][j] == boardsq:
                            present = 1
       if (present == 0):
              print("Square is not present in chessboard, Quitting the program")
              quit()

       currpos = find_in_list_of_list(mat, mvpiece)
       curr_pos = list(currpos)
       print(" Current position of ", mvpiece, " is ", curr_pos)
       desloc = find_des_inlist(matboard, boardsq)
       des_loc = list(desloc)

       if des_loc[0] > 7 or des_loc[1] > 7 or des_loc[0] < 0 or des_loc[1] < 0:
              print("Invalid Destination square (Out of Board),quitting the game")
              quit()
       else:
              print("Destination Position of ", mvpiece, " is: ", des_loc)

       # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       #        FUNCTIONS CALLING TO FIND LOC OF CHESS PIECE
       # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       pieceloc(mvpiece)
       move_piece(mvpiece, des_loc, curr_pos, boardsq, piece_coord)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def find_in_list_of_list(mat, mvpiece):
       for sub_list in mat:
              if mvpiece in sub_list:
                     return (mat.index(sub_list), sub_list.index(mvpiece))
       else:
             print("Piece not on board....Quitting the game")
             quit()


def find_des_inlist(matboard, boardsq):
       for sub_list1 in matboard:
              if boardsq in sub_list1:
                     return (matboard.index(sub_list1), sub_list1.index(boardsq))
       else:
              print("Square not on board....quitting the game")
              quit()

def pieceloc(mvpiece):
       pieceAvb = 0
       for i in range(0, 8):
              for j in range(0, 8):
                     if (mat[i][j] == mvpiece):
                            pieceAvb = 1
#                            print("The piece is currently in the board at Square", matboard[i][j])

       if (pieceAvb == 0):
              print("Chess Piece not available on Board PC AVB", pieceAvb)
              gamestarts()


################################################################################
#     PIECES CALLING BELOW
################################################################################


def move_piece(mvpiece, des_loc, curr_pos, boardsq, piece_coord):
       if (mvpiece == "BR1"):
              brook1(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BK1"):
              bknight1(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BB1"):
              bbishop1(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BK"):
              bking(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BQ"):
              bqueen(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BR2"):
              brook2(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BK2"):
              bknight2(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BB2"):
              bbishop2(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BP1" or mvpiece == "BP2" or mvpiece == "BP3" or mvpiece == "BP4"):
              bpawn(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "BP5" or mvpiece == "BP6" or mvpiece == "BP7" or mvpiece == "BP8"):
              bpawn(des_loc, curr_pos, boardsq, mvpiece, piece_coord)

       elif (mvpiece == "exit"):
              print("ending the game. Thanks")

       else:
              pass


###############################################################################
#    PIECES CALLING ENDS HERE
###############################################################################

def updatemat(curr_pos, des_pos, mvpiece,piece_coord):
       if mvpiece == 'BK1' or mvpiece == 'BK2':
              path_dec = True
       else:
              path_dec = hasclearpath(curr_pos, des_pos, piece_coord)

       if path_dec is False:
              print("Obstruction in path, cannot move")

       else:
              print(" No obstruction, the ", mvpiece, " can move")
              curr_pos = list(curr_pos)
              a = int(curr_pos[0])
              b = int(curr_pos[1])
              c = int(des_pos[0])
              d = int(des_pos[1])
              mat[a][b] = 0
              mat[c][d] = mvpiece
#             print("Curr pos, Des Pos :", curr_pos, des_pos)
#              print("Piece tracker : ", piece_coord)
              piece_coord.append(des_pos)
              piece_coord.remove(curr_pos)
 #             print("After opr tracker : ", piece_coord)
              printboard()


def printboard():
       topbottom = [' *  ', '  A   ', '  B   ', '  C   ', ' D   ', ' E   ', ' F   ', ' G   ', ' H   ', ' *  ']
       sides = ['8', '7', '6', '5', '4', '3', '2', '1']
       #        sides = ['1', '2', '3', '4', '5', '6', '7', '8']
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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     CHESS PIECES CODED BELOW : ROOK,KNIGHT,BISHOP,QUEEN,KING,PAWN
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def brook1(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       legalmove1 = []
       legalmove2 = []
       for i in range(0, 8):
              #      print("lg1: ",i,curr_pos[0])
              #      print("lg2: ",curr_pos[1],i)
              legalmove1.append([curr_pos[0], i])
              legalmove2.append([i, curr_pos[1]])
#       print("Legal Moves are as follows:\n ", legalmove1, legalmove2)
       if des_loc in legalmove1 or des_loc in legalmove2:
              print("The move is in line...will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")
       legalmove1.clear()
       legalmove2.clear()


def brook2(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       legalmove1=[]
       legalmove2=[]
       for i in range(0, 8):
              legalmove1.append([curr_pos[0],i])
              legalmove2.append([i,curr_pos[1]])
       print("Legal Moves are as follows:\n ", legalmove1, legalmove2)
       if des_loc in legalmove1 or des_loc in legalmove2:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")
       legalmove1.clear()
       legalmove2.clear()


def bknight1(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       Xk = [2, 1, -1, -2, -2, -1, 1, 2]
       Yk = [1, 2, 2, 1, -1, -2, -2, -1]
       legalmove1 = []
       for i in range(0, 8):
              xkp = curr_pos[0] + Xk[i]
              Ykp = curr_pos[1] + Yk[i]
              legalmove1.append([xkp, Ykp])

       if des_loc in piece_coord:
              print("The destination position is occupied. Illegal move")
       elif des_loc in legalmove1:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")
       legalmove1.clear()


def bknight2(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       Xk = [2, 1, -1, -2, -2, -1, 1, 2]
       Yk = [1, 2, 2, 1, -1, -2, -2, -1]
       legalmove1 = []
       for i in range(0, 8):
              xkp = curr_pos[0] + Xk[i]
              Ykp = curr_pos[1] + Yk[i]
              legalmove1.append([xkp, Ykp])

       if des_loc in piece_coord:
              print("The destination position is occupied. Illegal move")
       elif des_loc in legalmove1:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")
       legalmove1.clear()


def bbishop1(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       dx = abs(des_loc[0] - curr_pos[0])
       dy = abs(des_loc[1] - curr_pos[1])
       if (dx == dy) and (dx > 0):
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")


def bbishop2(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       dx = abs(des_loc[0] - curr_pos[0])
       dy = abs(des_loc[1] - curr_pos[1])
       if (dx == dy) and (dx > 0):
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")


def bking(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       if abs(des_loc[0] - curr_pos[0]) <= 1 and abs(des_loc[1] - curr_pos[1]) <= 1:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("The Move is illegal .Please try again")


def bqueen(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       #  if col == colN or row == rowN or abs(col - colN) == abs(row - rowN):
       if (curr_pos[1] == des_loc[1] or curr_pos[0] == des_loc[0] or abs(curr_pos[0] - des_loc[0]) == abs(
               curr_pos[1] - des_loc[1])):
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("Illegal Move of queen")


def bpawn(des_loc, curr_pos, boardsq, mvpiece, piece_coord):
       print("curr_pos[0],des_pos[0] : ", curr_pos[0], des_loc[0])
       print("curr_pos[1],des_pos[1] : ", curr_pos[1], des_loc[1])
       #    print("des_loc[0], curr_pos[0], des_loc[1] , curr_pos[1] :", des_loc[0], curr_pos[0], des_loc[1], curr_pos[1])
       if des_loc[0] - curr_pos[0] == 1 and des_loc[1] - curr_pos[1] == 0:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       elif curr_pos[0] == 1 and des_loc[0] - curr_pos[0] == 2:
              print("The move is in line will now check if legal")
              updatemat(curr_pos, des_loc, mvpiece,piece_coord)
       else:
              print("Illegal move of Pawn")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#     CHESS PIECES CODED BELOW
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def hasclearpath(curr_pos, des_pos, piece_coord):
       startcol, startrow = curr_pos[1], curr_pos[0]
       targetcol, targetrow = des_pos[1], des_pos[0]

       if abs(startrow - targetrow) <= 1 and abs(startcol - targetcol) <= 1:
              return True

       else:
              if targetrow > startrow and targetcol == startcol:
                     # Straight down
                     tmpstart = (startrow + 1, startcol)
                     print("tmpstart:", tmpstart)
              elif targetrow < startrow and targetcol == startcol:
                     # Straight up
                     tmpstart = (startrow - 1, startcol)
              elif targetrow == startrow and targetcol > startcol:
                     # Straight right
                     tmpstart = (startrow, startcol + 1)
              elif targetrow == startrow and targetcol < startcol:
                     # Straight left
                     tmpstart = (startrow, startcol - 1)
              elif targetrow > startrow and targetcol > startcol:
                     # Diagonal down
                     tmpstart = (startrow + 1, startcol + 1)
              elif targetrow > startrow and targetcol < startcol:
                     # Diagonal down left
                     tmpstart = (startrow + 1, startcol - 1)
              elif targetrow < startrow and targetcol > startcol:
                     # Diagonal up right
                     tmpstart = (startrow - 1, startcol + 1)
              elif targetrow < startrow and targetcol < startcol:
                     # Diagonal up left
                     tmpstart = (startrow - 1, startcol - 1)

                     # If no pieces in the way, test next square

       print("tmpstart: ", tmpstart)
       print("piece coord: ", piece_coord)
       if (des_pos in piece_coord):
              return False
       elif list(tmpstart) in piece_coord:
              return False
       else:
              hasclearpath(tmpstart, des_pos, piece_coord)
              if (list(tmpstart) > des_pos):
                     return True


# *******************************************************************************
# *******************************************************************************
def tracker():
       piece_coord = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3],
                      [1, 4], [1, 5], [1, 6], [1, 7]]
       input_values(piece_coord)


def input_values(piece_coord):
       printboard()
       mvpiece = input("Enter The Piece you want to move: ").upper()
       boardsq = input("Enter the Square of the board, to move piece: ").upper()
       gamestarts(mvpiece, boardsq, piece_coord)
       decision = input("Do you want to continue: (Y or N) : ")
       if decision == "Y" or decision == 'y':
              input_values(piece_coord)
       else:
              quit()


tracker()


