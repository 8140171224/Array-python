
from array import *


arr = array('i',[])

n = int(input('Enter the len of the array :'))

for i in range(n):
    x = int(input('Enter the next value :'))

    arr.append(x)

print(arr)

#

val = int(input('Enter the value or search index :'))

##

k = 0
for e in arr:
    if e==val:
        print('Index :'k)

    k+=1

#
print(arr.index(val))
