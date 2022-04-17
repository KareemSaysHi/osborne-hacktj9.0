import numpy as np
from display import PieceDisplay
from openscad import OpenSCAD
from solver import Solver

class PuzzleSolver():
    def __init__(self):
        pass

    def showPieces(self):
        solver = Solver()
        heptacubes = solver.getHeptacubes()
        display = PieceDisplay(heptacubes)
        display.displayPieces()

    def outputToSCAD(self):
        openscad = OpenSCAD()
        openscad.writeSCAD()


        

if __name__ == "__main__":
    puzzleSolver = PuzzleSolver()
    puzzleSolver.showPieces()



#find all 6 and 7 pieces
#account for rotations

#AT THIS POINT WE KNOW ALL OF THE PIECES THAT WE WANT TO WORK WITH!