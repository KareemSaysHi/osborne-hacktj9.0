import numpy as np
import matplotlib.pyplot as plt
import keyboard
import time

class PieceDisplay():
    def __init__(self, pieces):
        self.pieces = pieces #4d array


        
    def displayPieces(self):
        counter = 0
        plt.ion()
        voxelplot = plt.figure()
        ax = voxelplot.add_subplot((111), projection='3d') #makes a subplot

        ax.grid(True)
        ax.set_box_aspect((1, 1, 1))

        update = True


        while True:
            if keyboard.is_pressed('left'):
                counter -= 1
                if counter < 0: #wrap the counter around
                    counter += len(self.pieces)
                update = True
            elif keyboard.is_pressed('right'):
                counter += 1
                if counter >= len(self.pieces): #wrap the counter around
                    counter -= len(self.pieces)
                update = True
            
            if update:
                piece_matrix = self.pieces[counter]
                piece_matrix = np.rot90(piece_matrix, 3, axes=(1, 2))
                piece_matrix = np.rot90(piece_matrix, axes=(0, 2))

                ax.voxels(piece_matrix) #makes a voxel plot
                plt.title("Piece " + str(counter+1) + " out of " + str(len(self.pieces)))
                
                ax.set_xlim3d([0, np.size(piece_matrix, 0)])
                ax.set_ylim3d([0, np.size(piece_matrix, 1)])
                ax.set_zlim3d([0, np.size(piece_matrix, 2)])
                ax.set_box_aspect((np.size(piece_matrix, 0), np.size(piece_matrix, 1), np.size(piece_matrix, 2)))

                ax.set_xticks(list(range(0, np.size(piece_matrix, 0) + 1)))
                ax.set_yticks(list(range(0, np.size(piece_matrix, 1) + 1)))
                ax.set_zticks(list(range(0, np.size(piece_matrix, 2) + 1)))

                voxelplot.canvas.draw()
                voxelplot.canvas.flush_events()
                plt.cla()
                update = False