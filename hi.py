import numpy as np
list1 = [1,2,3,4,5]
np1 = np.array(([1,2,3,4,5], [1,3,5,7,9]))
print(np1)
#length of array
print(np1.shape)

#range
np2 = np.arange(10)     #it will print 0 to 9
print(np2)

#step
np3 = np.arange(1,11, 2)
print(np3)

#zero array
np4= np.zeros(10)
print(np4)

#2 dimensional array
np5 = np.zeros((2,10))
print(np5)

#convert list to numpy array
list2 = [1,2,3,4,5]
np6 = np.array(list2)
print(np6)
print(np6.dtype)