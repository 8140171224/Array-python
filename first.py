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
