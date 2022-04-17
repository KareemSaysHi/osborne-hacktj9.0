import numpy as np

class Solver():
    def __init__(self):
        self.heptacubes = []
        self.picnicbasket = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]] #just trust me this is a picnicbasket


    def isOverlapping(self, piece, location):
        pieceInBasket = np.zeros((6, 5, 5)) #put a piece in basket
        for i in range (location[0], location[0]+np.size(piece, 0)): #z
            for j in range (location[1], location[1]+np.size(piece, 1)): #y
                for k in range (location[2], location[2]+np.size(piece, 2)): #x
                    if (i < 6 and j < 5 and k < 5):
                        pieceInBasket[i][j][k] = piece[i-location[0]][j-location[1]][k-location[2]]
        
        #check if piece is overlapping with basket:
        sumArray = np.add(pieceInBasket, self.picnicbasket)
        #print(sumArray)
        if np.size(np.where(sumArray.flatten() == 2)) > 0:
            return True
        else:
            return False

    def readFile(self):
        with open('osborne-hacktj9.0\hexacubes.txt', 'r') as f:
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


    def canPieceGetOutOfBasket(self, piece, location):
        if location[0] > 5:
            return True

        location[0] += 1
        if not self.isOverlapping(piece, location):
            return self.canPieceGetOutOfBasket(piece, location)
        location[0] -= 1
        
        while not self.isOverlapping(piece, location):
            location[1] -= 1
            if location [1] < -1:
                return True

        while not self.isOverlapping(piece, location):
            location[2] -= 1
            if location [2] < -1:
                return True

        counter = 0
        while not self.isOverlapping(piece, location):
            while not self.isOverlapping(piece, location):
                location[0] += 1
                if not self.isOverlapping(piece, location):
                    return self.canPieceGetOutOfBasket(piece, location)
                location[0] -= 1

                location[1] += 1
                counter += 1
                if location[1] > 6:
                    return True
            
            location[1] -= counter
            location[2] += 1
            if location[2] > 6:
                return True

        return False

    def getHeptacubes(self):
        self.readFile()
        #newlist = self.removePadding()
        #self.heptacubes = newlist
        
        return self.heptacubes #should be newlist
