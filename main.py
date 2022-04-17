from dis import disassemble
import numpy as np
from display import PieceDisplay
from openscad import OpenSCAD
from solver import Solver
from disassembler import Disassembler

class PuzzleSolver():
    def __init__(self):
        pass

    def disassemble(self):
        piece1 = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
        piece2 = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
        piece3 = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
        position1 = [1, 1, 1]
        position2 = [2, 1, 1]
        position3 = [3, 1, 1]
        
        disassembler = Disassembler(np.array([piece1, piece2, piece3]), [position1, position2, position3])
        solutions = disassembler.disassembleThatBoi(disassembler.pieces, disassembler.positions, [], 0, [], [])
        minlength = 100
        myfavoritesolution = 0
        #for solution in solutions:
            #print(len(solution))


    def showPieces(self):
        solver = Solver()
        heptacubes = solver.getHeptacubes()
        usableHeptacubes = []
        for heptacube in heptacubes:
            if solver.canPieceGetOutOfBasket(heptacube, [1, 1, 1]):
                usableHeptacubes.append(heptacube)

        print(usableHeptacubes)
        with open('usableHexacubes.txt', 'w') as f:
            for h in usableHeptacubes:
                f.write(''.join(str(h.reshape(27))) + '\n')

        display = PieceDisplay(usableHeptacubes)
        display.displayPieces()

    def outputToSCAD(self):
        openscad = OpenSCAD()
        openscad.writeSCAD()

if __name__ == "__main__":
    puzzleSolver = PuzzleSolver()
    puzzleSolver.disassemble()



#find all 6 and 7 pieces
#account for rotations

#AT THIS POINT WE KNOW ALL OF THE PIECES THAT WE WANT TO WORK WITH!