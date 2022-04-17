import numpy as np

class Solver():
    def __init__(self):
        self.heptacubes = []
        self.picnicbasket = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]] #just trust me this is a picnicbasket


    def pieceToPieceInBasket(self, piece):
        pieceInBasket = np.zeros(9, 9, 9)
        for i in range (1, 1+np.size(piece, 0)): #z
            for j in range (3, 3+np.size(piece, 1)): #y
                for k in range (3, 3+np.size(piece, 2)): #x
                    pieceInBasket[i][j][k] = piece[i-1][j-3][k-3]

    def isOverlappingWithBasket(self, pieceInBasket):
        if np.array_equal(np.logical_and(pieceInBasket, self.picnicbasket),
        ) 

    def readFile(self):
        with open('osborne-hacktj9.0\heptacubes.txt', 'r') as f:
            heptacubesList = f.readlines()
            for heptacube in heptacubesList:
                helperArray = []
                heptacube = heptacube.strip()
                for number in heptacube:
                    helperArray.append(int(number))
                helperArray = np.array(helperArray)
                helperArray = np.reshape(helperArray, (3,3,3))
                self.heptacubes.append(helperArray)

    def removePadding(self):
        newlist = []
        for heptacube in self.heptacubes:
            for n in range (0, 8): #4 rotations
                
                #print("here is the rotated heptacube")
                #print(heptacube)

                for i in range (0, np.size(heptacube, 0)):
                    if i < np.size(heptacube, 0):
                        #print("this is the thing i is going up to ")
                        #print(np.size(heptacube, 0))
                        #print("this is the heptacube")
                        #print(heptacube)
                        #print("and this is np zeros")
                        #print(np.zeros((np.size(heptacube, 1), np.size(heptacube, 2))))
                        
                        if np.array_equal(heptacube[i], np.zeros((np.size(heptacube, 1), np.size(heptacube, 2)))):
                            heptacube = np.delete(heptacube, i, axis=0)
                            #print("deleted something")
                            #print(heptacube)
                    heptacube = np.rot90(heptacube, axes=(0, 2))
                    #print("rotated")
                
            heptacube = np.rot90(heptacube, axes=(1, 2))

            for n in range (0, 8): #8 rotations
                if n % 2 == 1:
                    for i in range (0, np.size(heptacube, 0)):
                        if i < np.size(heptacube, 0):
                            if np.array_equal(heptacube[i], np.zeros((np.size(heptacube, 1), np.size(heptacube, 2)))):
                                heptacube = np.delete(heptacube, i, axis=0)
                                #print("deleted something")
                                #print(heptacube)
                heptacube = np.rot90(heptacube, axes=(0, 2))

            
            newlist.append(heptacube)
            heptacube = np.rot90(heptacube, 3, (1, 2))

        return newlist


    def canPieceGetOutOfBasket(piece):

            

    def getHeptacubes(self):
        self.readFile()
        newlist = self.removePadding()
        self.heptacubes = newlist
        return newlist
