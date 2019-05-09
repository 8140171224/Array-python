
# Coping array
# deep copy & shallow copy

# Numpy for extra and many function in array

from numpy import *

# Shallow copy
arr1 = array([1,2,3,4,5])

arr2 = arr1.view()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


# deep copy

arr1 = array([1,2,3,4,5])

arr2 = arr1.copy()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
