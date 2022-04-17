from time import gmtime
import numpy as np

class Disassembler():
    def __init__(self, pieces, positions):
        self.pieces = pieces
        self.positions = positions #each position is a list of three [z, y, x]

        self.picnicbasket = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]] #just trust me this is a picnicbasket


    def isOverlapping(self, pieces, positions):
        piecesInBasket = np.zeros((6, 5, 5)) #put a piece in basket
        for pieceNum in range (0, len(pieces)):
            for i in range (positions[pieceNum][0], positions[pieceNum][0]+np.size(pieces[pieceNum], 0)): #z
                for j in range (positions[pieceNum][1], positions[pieceNum][1]+np.size(pieces[pieceNum], 1)): #y
                    for k in range (positions[pieceNum][2], positions[pieceNum][2]+np.size(pieces[pieceNum], 2)): #x
                        if (i < 6 and j < 5 and k < 5):
                            piecesInBasket[i][j][k] += pieces[pieceNum][i-positions[pieceNum][0]][j-positions[pieceNum][1]][k-positions[pieceNum][2]]
        
        #check if piece is overlapping with basket:
        sumArray = np.add(piecesInBasket, self.picnicbasket)
        #print(sumArray)
        if np.size(np.where(sumArray.flatten() == 2)) > 0:
            return True
        else:
            return False


    def disassembleThatBoi(self, pieces, positions, reachedStates, depth, movelist):

        for pieceNum in range (0, len(pieces)):
            for i in range(0, 6):
                if i == 0:
                    positions[pieceNum][0] += 1
                elif i == 1:
                    positions[pieceNum][0] -= 1
                elif i == 2:
                    positions[pieceNum][1] += 1
                elif i == 3:
                    positions[pieceNum][1] -= 1
                elif i == 4:
                    positions[pieceNum][2] += 1
                elif i == 5:
                    positions[pieceNum][2] -= 1
                if not self.isOverlapping:
                    if np.size(np.where(reachedStates == positions)) == 0:
                        movelist.append([pieceNum, i])
                        reachedStates.append(positions)
                        self.disassembleThatBoi(pieces, positions, reachedStates, depth, movelist)


