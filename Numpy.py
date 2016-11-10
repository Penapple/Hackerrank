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

#Zeros and Ones
N = tuple(map(int, input().split()))
print(np.zeros(N, int))         #zeros/ones (num, shape, shape) or (shape, shape)
print(np.ones(N, int))

#Eye and Identity
import numpy as np
n, m = map(int, input().split())
print(np.eye(n, m))

#Array Mathematics
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
#--- Or use command below just in one row ---
#a, b = (np.array([input().split() for _ in range(n)], int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')

#Floor, Ceil and Rint
a = np.array(list(input().split()), float)
print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')

#Sum and Prod
n, m = map(int, input().split())
a = np.array(list(input().split() for _ in range(n)), int)
b = np.sum(a, axis=0)
c = np.prod(b)
print(c)
