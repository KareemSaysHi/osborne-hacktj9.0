# Procedureal Picnic Puzzle Production!
## Our HackTJ 9.0 Project, by team Osborne Study Hall

Here is our progress at a web application to procedurally generate linear packing puzzles and automatically produce an stl for convenient 3D printing!  Current features include:

- generating and visualizing all possible heptacubes (a contigenous shape formed by 7 1x1x1 cuboids), of which there are 10941 (our algorithm can be used to find higher orders of polyominos too, allowing us to expand on our project easily)
- reducing this set of heptacubes (and lower order polycubes) to the subset which are able to be linearly removed from our picnic basket packing puzzle, of which there are 211
- visualizing these pieces using matplotlib's voxelplot
- web app interface for selecting a difficulty and size of puzzle, and utilization of the numpy-stl library to convert puzzles in the form of numpy arrays to stls for 3D printing
- optional support for OpenSCAD and the puzzlecad library

Features with heavy development but not fully completed include
- assembly of polyominos into a 3x3x3 cube
- recursive disassembly of linear packing puzzles to determine the minimum sequence of moves needed to solve a puzzle (currently, our program can find a path to disassemble a puzzle completely, but cannot find the shortst path)
- although not implemented currently, we spent a large amount of time exploring an approach to modeling packing puzzles that allowed for pieces to rotate as well as move linearly, and came up with a method to break complex 3D rotations down into a series of cases to check

Features that we would love to implement into the future:
- scalability of puzzles to other packing puzzles shapes (not just these picnic basket puzzles)
- ability to select tolerances for 3D printed parts
- producing a solution guide along with the stl, and possibly a hints document showing the solver certain positions throughout the puzzle
- exploring further the mathematics of polycubes and packing puzzles

Thank you for reading and we hope you enjoy!
