from display import PieceDisplay
import numpy as np
OUTFILE = 'heptacubes.txt'

def enumHepta():
	with open(OUTFILE, 'w') as outfile:
		for a in range(27):
			for b in range(a + 1, 27):
				for c in range(b + 1, 27):
					for d in range(c + 1, 27):
						for e in range(d + 1, 27):
							for f in range(e + 1, 27):
								for g in range(f + 1, 27):
									indices = [a, b, c, d, e, f, g]
									arr = [(1 if i in indices else 0) for i in range(27)]
									arr = np.arr(arr).reshape((3,3,3))
									if check_contiguous(arr) and checkLeftFwdDown(arr): # is valid
										# export configuration
										outfile.write(''.join(str(i) for i in arr.reshape(27)) + '\n')

def check_contiguous(arr): # arr is a numpy array
    for x in arr:
        for y in arr[x]:
            for z in arr[x][y]:
                if not (x>0 and arr[x-1][y][z] or x<2 and arr[x+1][y][z] or y>0 and arr[x][y-1][z] or y<2 and arr[x][y+1][z] or z>0 and arr[x][y][z-1] or z<2 and arr[x][y][z+1]):
                    return False
    return True

'''
def check3x3x3(arr): # arr is a numpy array
    for dim in np.nonzero(arr):
        if np.unique(arr, dim) < 3: # this got messed up
            return False
    return True
'''

def checkLeftFwdDown(arr):
	for dim in np.nonzero(arr):
		if np.amin(dim) > 0:
			return False
	return True

# 3x3x3
# 3x3x2
# 3x3x1
# 3x2x2
