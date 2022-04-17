from re import L
import numpy as np
import matplotlib.pyplot as plt
import keyboard

class DisassemblerDisplay():
    def __init__(self, disassemblies):
        self.disassemblies = disassemblies
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    def createDisassembleMatrix(self)

    
    def recolor(self, disassembleMatrix):
        disassembleShape = [np.size(disassembleMatrix, 0), np.size(disassembleMatrix, 1), np.size(disassembleMatrix, 2)] #z, y, x
        colors = np.empty([disassembleShape[0], disassembleShape[1], disassembleShape[2]], dtype = object)

        for x in range (0, shape[0]):
            for y in range (0, shape[1]):
                for z in range (0, shape[2]):
                    pass



    def displayDisassemblies(self):
        path = 0
        depth = 0
        plt.ion()
        voxelplot = plt.figure()
        ax = voxelplot.add_subplot((111), projection="3d")

        ax.set_xlim3d([0, 9])
        ax.set_ylim3d([0, 9])
        ax.set_zlim3d([0, 7])

        ax.set_xticks(list(range(0, 9)))
        ax.set_yticks(list(range(0, 9)))
        ax.set_yticks(list(range(0, 7)))

        ax.grid(True)
        ax.set_box_aspect((7, 9, 9))

        update = True

        while True:
            if keyboard.is_pressed("left"):
                path -= 1
                depth = 0
                if path < 0: #don't loop around
                    path = 0
                update = True
            if keyboard.is_pressed("right"):
                path += 1
                depth = 0
                if path >= len(self.disassemblies):
                    path = len(self.disassemblies)-1
                update = True
            if keyboard.is_pressed("up"):
                depth -= 1
                if depth < 0:
                    depth = 0
                update = True
            if keyboard.is_pressed("down"):
                depth += 1
                if depth >= len(self.disassemblies[path]):
                    depth = len(self.disassemblies[path]) - 1
                update = True

            if update:
                disassembleMatrix = self.disassemblies[path][depth]


        ax.set_x
