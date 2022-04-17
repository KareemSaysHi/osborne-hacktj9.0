from time import gmtime
from turtle import position
import numpy as np
import copy
import sys

from sympy import false

class Disassembler():
    def __init__(self, pieces, positions):
        self.pieces = pieces
        self.positions = positions #each position is a list of three [z, y, x]

        self.picnicbasket = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]] #just trust me this is a picnicbasket


    def isOverlapping(self, pieces, positions, printstatements=False):
        piecesInBasket = np.zeros((6, 5, 5)) #put a piece in basket
        for pieceNum in range (0, len(pieces)):
            for i in range (positions[pieceNum][0], positions[pieceNum][0]+np.size(pieces[pieceNum], 0)): #z
                for j in range (positions[pieceNum][1], positions[pieceNum][1]+np.size(pieces[pieceNum], 1)): #y
                    for k in range (positions[pieceNum][2], positions[pieceNum][2]+np.size(pieces[pieceNum], 2)): #x
                        if (i < 6 and j < 5 and k < 5):
                            piecesInBasket[i][j][k] += pieces[pieceNum][i-positions[pieceNum][0]][j-positions[pieceNum][1]][k-positions[pieceNum][2]]
        
        #check if piece is overlapping with basket:
        sumArray = np.add(piecesInBasket, self.picnicbasket)
        if printstatements:
            print(sumArray)
        #print(sumArray)
        if np.size(np.where(sumArray.flatten() == 2)) > 0:
            return True
        else:
            return False

    def isPieceRemoved(self, pieceNum, positions):
                if positions[pieceNum][0] > 6 or positions[pieceNum][1] < -1 or positions[pieceNum][1] > 4 or positions[pieceNum][2] < -1 or positions[pieceNum][2] > 4:
                    return True
                return False

    def weveAlreadyReachedThisPosition(self, positions, reachedStates):
        for state in reachedStates:
            if np.array_equal(positions, state):
                return True
        return False


    def disassembleThatBoi(self, pieces, positions, reachedStates, depth, movelist, solutions):
        printstatements=False
        if depth == 2:
            printstatements = True

        pieceNum = 0
        while pieceNum < len(pieces):
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

                if printstatements:
                    print("LOOK AT ME IM PRINTING STUFF")
                    print(movelist)
                    print("LOOK WHAT I VALUE I AM ON")
                    print(i)
                    print("LOOK AT WHAT PIECE I'M LOOKING AT!")
                    print(pieceNum)
                    print("NOW WHY AM I NOT WORKING")
                if not self.weveAlreadyReachedThisPosition(positions, reachedStates):
                    if not self.isOverlapping(pieces, positions, printstatements=True): #if move is new and valid
                        if printstatements:
                            print("I AM A VALID MOVE")
                        movelist.append([pieceNum, i])

                        reachedStates.append(copy.deepcopy(positions))
                        #print(reachedStates)

                        if self.isPieceRemoved(pieceNum, positions):
                            positions = np.delete(positions, pieceNum, axis=0)
                            pieces = np.delete(pieces, pieceNum, axis=0)
                            #print(depth)

                            if len(pieces) == 1: #we found a complete solution!
                                return movelist
                        
                        foundSolutions = self.disassembleThatBoi(pieces, positions, reachedStates, depth+1, movelist, solutions)

                        if len(foundSolutions) > 0:
                            solutions.append(foundSolutions)

                        movelist.pop(-1)

                if i == 0:
                    positions[pieceNum][0] += -1 #reverting all of the moves
                elif i == 1:
                    positions[pieceNum][0] -= -1
                elif i == 2:
                    positions[pieceNum][1] += -1
                elif i == 3:
                    positions[pieceNum][1] -= -1
                elif i == 4:
                    positions[pieceNum][2] += -1
                elif i == 5:
                    positions[pieceNum][2] -= -1   
            pieceNum += 1

        if len(solutions) > 0:
            return solutions
        else:
            return []
                

                        


