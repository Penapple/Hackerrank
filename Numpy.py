import numpy as np
#Arrays
a = np.array(list(input().split()), float)
print(a[::-1])

#Shape and Reshape
a = np.array(list(map(int, input().split())))
print(np.reshape(a,(3,3)))

#Transpose and Flatten
n, m = map(int, input().split())
a = np.array(list(input().split() for _ in range(n)), int)    #list with for in range generates list in list
print(a.transpose())
print(a.flatten())

#Concatenate
n, m, p = map(int, input().split())

a = np.array(list(input().split() for _ in range(n)), int)
b = np.array(list(input().split() for _ in range(m)), int)
print(np.concatenate((a, b), axis = 0))
