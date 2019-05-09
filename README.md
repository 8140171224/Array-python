   
##   from numpy import *


# add 5 to each element
    arr = array([1,2,3,4,5])

    arr = arr + 5

    print(arr)

# Adding to array
    arr1 = array([1,2,3,4,5])

    arr2 = array([6,2,3,4,5])

    arr3 = arr1 + arr2

    print(arr3)

# Sin of the array
    arr1 = array([1,2,3,4,5])
    print(sin(arr1))

# Cos of the array
    arr1 = array([1,2,3,4,5])
    print(cos(arr1))

# Log of the array
    arr1 = array([1,2,3,4,5])
    print(log(arr1))

# Sqrt of the array
    arr1 = array([1,2,3,4,5])
    print(sqrt(arr1))

# Sum of the array
    arr1 = array([1,2,3,4,5])
    print(sum(arr1))

# To find min value
    arr1 = array([1,2,3,4,5])
    print(min(arr1))

# To find max value
    arr1 = array([1,2,3,4,5])
    print(max(arr1))

# concatenate array
    arr1 = array([1,2,3,4,5])
    arr2 = array([6,2,9,4,5])

    print(concatenate([arr1,arr2]))


# Array-python-example

# importing all function from array
    from array import *

# An empty array for adding user input
    arr = array('i',[])
 
# Getting input in interger from user for len of array
    n = int(input('Enter the len of the array :'))
 
 # for loop for adding interger val in empty array
    for i in range(n):
    x = int(input('Enter the next value :'))
    arr.append(x)
# print(arr) user inputed array
    print(arr)

# val for searching 
    val = int(input('Enter the value or search index :'))

# Manual way to find index
  k = 0
  for e in arr:
      if e==val:
          print('Index :'k)

      k+=1

# inbuild function to print index
    print(arr.index(val))
