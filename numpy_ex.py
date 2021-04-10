import numpy as np

# creating 1d array
a = np.array([1,2,3,4,5])
print(a)
a = np.array([1.0,2,3,4,5], dtype='int32')
print(a)

# creating 2d array
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)

# Get dimension, shape (row-by-column), datatype it stores
a = np.array([[1.0,2.0,3.0,4.0,5.0],[6.0,7.0,8.0,9.0,10.0]])
print(a.ndim)
print(a.shape)
print(a.dtype)

# Get number of elements
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.size)               # 10

# Get size (in bytes) of individual element
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.itemsize)               # output is 8 because by default dtype is 'int64'
a = np.array([[1,2,3,4,5],[6,7,8,9,10]], dtype='int32')
print(a.itemsize)               # output is 4

# Get combined size (in bytes) of all element
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.nbytes)

# Accessing elements [row, col]
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[1,3])           # 9
# specific row
print(a[1,:])           # [6 7 8 9 10]
# specific column
print(a[:,4])           # [5 10]
# using [strt:end:step]
print(a[:,0:4:2])           # [[1 3] [6 8]]
print(a[:,0::2])           # [[ 1  3  5] [ 6  8 10]]

# Modifying elements
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
a[1,3] = 1000
print(a)
a[1,:] = [16,17,18,19,20]
print(a)
a[0,:] = list(range(a[0,:].size))
print(a)
a[1,:] = list(range(10,a[0,:].size+10))
print(a)

# Types of arrays in numpy
# 1D array with number 0
a = np.zeros(5, dtype='int32')
print(a)

# 2x3x4 array with number 0
a = np.zeros((2,3,4), dtype='int32')
print(a)

# 1D array with number 1
a = np.ones(5, dtype='int32')
print(a)

# 2x3 array with number 1
a = np.ones((2,3), dtype='int32')
print(a)

a = np.array([list(np.zeros(10, dtype='int32')), list(np.ones(10, dtype='int32'))])
print(a)

# Identity matrix 6x6
a = np.identity(6)
print(a)

# 3x3 array with number 101 -- full()
a = np.full((3,3), 101)
print(a)

# array having size equal to existing array -- full_like()
existing = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.full_like(existing, 4)
print(a)

# random numbers between 0 & 1
a = np.random.rand(3,4)
print(a)

# random numbers between -5 & 5
a = np.random.randint(-5, 5, size=(3,4))
print(a)

# random numbers in a choice -- [101, 201, 301, 401]
a = np.random.choice([101, 201, 301, 401], size=(6, 6))
print(a)

# Rearranging elements 
a = np.random.randint(1,10,size = (4,6))
b = a.reshape((3,8))
print(a)
print(b)

# Vertically stacking elements
a = np.array([1,2,3,4,5,6])
b = np.vstack((a,a,a,a))
print(b)
# Horizontally stacking elements
c = np.array([[1,2,3,4],[5,6,7,8]])
d = np.hstack((c,c,c,c))
print(d)

# Evenly distribute the values 
# starting, ending, no_of_elements
a = np.linspace(0, 10, 20)
print(a)

# Repeating elements
a = np.repeat(101, 10)
print(a)

# copy() -- to duplicatey the existing numpy array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a
b[1,1] = 100            # changes 'a' also
print(a)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a.copy()
b[1,1] = 100            # wont change 'a'
print(a)

# Mathematical functions
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a+2)
print(a*2)
print(a**2)

# Trigonometric functions
# sin(), cos(), tan() .....
# arcsin(), arccos() ....
a = np.array([[90,2,3],[30,5,6],[60,8,0]])
print(np.sin(a*np.pi/180))
print(np.arcsin(a))

# Statistical functions
# for rows -- axis = 1
# for columns -- axis = 0
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.amin(a))
print(np.amax(a))
print(np.amin(a, axis=0))
print(np.amax(a, axis=0))
print(np.amin(a, axis=1))
print(np.amax(a, axis=1))

print(np.mean(a))
print(np.median(a))
print(np.average(a))

# Sorting an numpy array
a = np.array([[11,2,13],[24,15,6],[27,18,3]])
print(a)
print(np.sort(a))               # row sorting
print(np.sort(a, axis = 0))     # column sorting

# Matrix addition and multiplication
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.ones(a.shape, dtype='int32')
print(a + b)                # Matrix addition
print(np.dot(a,b))          # Matrix multiplication

# importing data from file
data = np.loadtxt('data_for_numpy.txt', dtype='int32', delimiter=',')
print(data)