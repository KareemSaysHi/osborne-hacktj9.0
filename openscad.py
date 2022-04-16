import numpy as np

class OpenSCAD():
    def __init__(self, pieces):
        self.pieces = pieces

    def pieceToString(self, piece): #["xxx|xx.|xxx", "xxx|xxx|xxx"]
        pieceStr = '['
        for z in piece:
            pieceStr += '"'
            for y in z:
                for x in y:
                    if x == 1:
                        pieceStr += 'x'
                    else:
                        pieceStr += '.'
                pieceStr += '|'
            
            l = len(pieceStr)
            pieceStr = pieceStr[:l-1]
            pieceStr += '", '

        l = len(pieceStr)
        pieceStr = pieceStr[:l-2]
        pieceStr += ']'
        return pieceStr

    def writeSCAD(self):
        with open('output.scad', 'w') as f:
            f.writelines(["include <puzzlecad.scad>\n", "$burr_scale = 12.75;\n", "$burr_inset = .15;\n", "$burr_bevel = 1;\n", "unit_beveled = false;\n"])
            pieceStrings = "burr_plate(["
            for piece in self.pieces:
                pieceStrings += self.pieceToString(piece)
                pieceStrings += ', '
            l = len(pieceStrings)
            pieceStrings = pieceStrings[:l-2]
            pieceStrings += "]);"
            f.write(pieceStrings)      
        f.close()

#if time, add way to have connectors in order to not have supports or something