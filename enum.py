# from display import PieceDisplay
import numpy as np
OUTFILE = 'heptacubes.txt'

def enumHepta():
	with open(OUTFILE, 'w') as outfile:
		for a in range(27):
			print('*', end='', flush=True)
			for b in range(a + 1, 27):
				for c in range(b + 1, 27):
					for d in range(c + 1, 27):
						for e in range(d + 1, 27):
							for f in range(e + 1, 27):
								for g in range(f + 1, 27):
									indices = [a, b, c, d, e, f, g]
									arr = [(1 if i in indices else 0) for i in range(27)]
									arr = np.array(arr).reshape((3,3,3))
									if check_contiguous(arr) and checkLeftFwdDown(arr) and checkComplete(arr): # is valid
										# export configuration
										outfile.write(''.join(str(i) for i in arr.reshape(27)) + '\n')
		print()

def check_contiguous(arr): # arr is a numpy array
	for x in range(len(arr)):
		for y in range(len(arr[x])):
			for z in range(len(arr[x][y])):
				if arr[x][y][z] and \
					not (x>0 and arr[x-1][y][z] or \
						x<2 and arr[x+1][y][z] or \
						y>0 and arr[x][y-1][z] or \
						y<2 and arr[x][y+1][z] or \
						z>0 and arr[x][y][z-1] or \
						z<2 and arr[x][y][z+1]):
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

def checkComplete(arr):
	# find a block
	ar = arr[:, :, :] # copy so not modifying original array
	ones = np.where(ar==1)
	firstOne = (ones[0][0], ones[1][0], [2][0])
	# fill from there
	q = [firstOne] # queue of (x, y, z) coordinates that have 1's
	counter = 0 # counter of number of ones in chunk
	while q:
		loc = q.pop() # loc is current location
		counter += 1
		ar[loc] = 0
		newIndices = [(loc[0]-1, loc[1], loc[2]), (loc[0], loc[1]-1, loc[2]), (loc[0], loc[1], loc[2]-1), (loc[0]+1, loc[1], loc[2]), (loc[0], loc[1]+1, loc[2]), (loc[0], loc[1], loc[2]+1)]
		for nLoc in newIndices: # potential new locations
			if not 0<=nLoc[0]<=2 or not 0<=nLoc[1]<=2 or not 0<=nLoc[2]<=2: # check if not within 3x3x3 bounding box
				continue
			if ar[nLoc]: # check if has a piece
				q.append(nLoc)
	# check if size ==7
	return counter == 7
	

if __name__=='__main__': 
	# arr = np.array([[[1, 1, 0], [1, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])
	# print(check_contiguous(arr), checkLeftFwdDown(arr))
	arr = np.array([1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]).reshape((3,3,3))
	print(check_contiguous(arr))
	# enumHepta()

# 3x3x3
# 3x3x2
# 3x3x1
# 3x2x2
