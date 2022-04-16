import numpy as np
from display import PieceDisplay
from openscad import OpenSCAD


class PuzzleSolver():
    def __init__(self):
        pass

    def showPieces(self):
        piece1 = np.array([[[1, 1, 1], [1, 1, 0]], [[1, 1, 0], [0, 0, 0]]])
        piece2 = np.array([[[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [0, 0, 0]]])
        display = PieceDisplay(np.array([piece1, piece2]))
        display.displayPieces()

    def outputToSCAD(self):
        openscad = OpenSCAD(np.array([[[[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [1, 1, 1], [0, 0, 0]]], [[[1, 1, 1], [1, 1, 0]], [[1, 1, 0], [0, 0, 0]]]]))
        openscad.writeSCAD()


        

if __name__ == "__main__":
    puzzleSolver = PuzzleSolver()
    puzzleSolver.outputToSCAD()