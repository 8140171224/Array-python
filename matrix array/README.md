 
# matrix array

##
from numpy import *
##
	arr1 = array([
                [1,2,3,6],
                [4,5,6,3]
            ])

# This can print type of data (int32) arr1
	print(arr1.dtype)

# Count dim on array
	print(arr1.ndim)

# Give row and col (2,3)
	print(arr1.shape)
	
# Give the size of matrix (6)
	print(arr1.size)

##

# convert 2d array in to 1d
     arr2 = arr1.flatten()
	 print(arr2)

##

# 
    arr2 = arr1.flatten()
# Convert the matrix has given (3,4)
    arr4 = arr2.reshape(3,4)
    arr3 = arr2.reshape(2,2,3)
    print(arr3)
    print('')
    print(arr4)

##
##

# Martices (don't need arr1) 
	m = matrix('1 2 3; 6 4 5; 6 7 9')

# print diagonal of matrix	
	print(diagonal(m))
# print max val of matrix	
	print(m.max())
	print(m)

##

# Add matrix and multiply it
     m1 = matrix('1 2 3; 6 4 5; 6 7 9')
     m2 = matrix('1 4 3; 6 2 5; 5 7 9')

     m3 = m1 + m2
     m4 = m1 * m2
     print(m3)
     print(m4)

##
