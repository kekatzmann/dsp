from numpy import *

A = array(([1, 2, 3],\
          [2, 7, 4]))

B = array(([1, -1],\
          [0, 1]))

C = array(([5, -1],\
           [9, 1],\
           [6, 0]))

D = array(([3, -2, -1],\
           [1, 2, 3]))

u = array([6, 2, -3, 5])

v = array([3, 5, -1, 4])

w = array(([1],\
           [8],\
           [0],\
           [5]))
a = 6


try:
    print(u + v)
except ValueError:
    print('Not Defined')

try:
    print(u - v)
except ValueError:
    print('Not Defined')

try:
    print(a*u)
except ValueError:
    print('Not Defined')

try:
    print(dot(u, v))
except ValueError:
    print('Not Defined')

try:
    print(linalg.norm(u)) #length (magnitude) of vector u
except ValueError:
    print('Not Defined')


try:
    print(A + C)
except ValueError:
    print('Not Defined')

try:
    print(A - transpose(C)) #transposed C
except ValueError:
    print('Not Defined')

try:
    print(transpose(C) + 3*D)
except ValueError:
    print('Not Defined')

try:
    print(dot(B, A))
except ValueError:
    print('Not Defined')

try:
    print(dot(B, transpose(A)))
except ValueError:
    print('Not Defined')

try:
    print(linalg.matrix_power(B, 4)) #B**4 - matrix needs to be square in order to be powered
except ValueError:
    print('Not Defined')

try:
    print(dot(A, transpose(A)))
except ValueError:
    print('Not Defined')

try:
    print(dot(D, transpose(D)))
except ValueError:
    print('Not Defined')

