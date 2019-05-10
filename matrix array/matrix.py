# matrix array

from numpy import *

arr1 = array([
                [1,2,3,6],
                [4,5,6,3]
            ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

##

arr2 = arr1.flatten()
print(arr2)

##

arr2 = arr1.flatten()
arr4 = arr2.reshape(3,4)
arr3 = arr2.reshape(2,2,3)
print(arr3)
print('')
print(arr4)

##
##
m = matrix('1 2 3; 6 4 5; 6 7 9')
print(diagonal(m))
print(m.max())
print(m)

##

m1 = matrix('1 2 3; 6 4 5; 6 7 9')
m2 = matrix('1 4 3; 6 2 5; 5 7 9')

m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)

##