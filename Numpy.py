import numpy as np
#Arrays
a = np.array(list(input().split()), float)
print(a[::-1])

#Shape and Reshape
a = np.array(list(map(int, input().split())))
print(np.reshape(a,(3,3)))
