"""
Here we will learn about numpy

following lessons were created using NumPy version 1.13.0

Numpy: build on c, and very fast

Panda is for data science build on top of Numpy
"""

import time
import numpy as np

# create numpy array
x = np.random.random(100000000);

# create mean by python
start = time.time()
# sum(x) / len(x)
print(time.time() - start)  # took 8.32 sec to complete

# create mena by numpy
start = time.time()
np.mean(x)
print(time.time() - start)  # took 0.14 sec to complete
# numpy is way tooooo faster


"""
At the core of NumPy is the ndarray, where nd stands for n-dimensional. An ndarray is a multidimensional 
array of elements all of the same type. In other words, an ndarray is a grid that can take on 
many shapes and can hold either numbers or strings. There are several ways to create ndarrays in NumPy.
1. Using regular Python lists
2. Using built-in NumPy functions
We refer to 1D arrays as rank 1 arrays. In general N-Dimensional arrays have rank N. Therefore, 
we refer to a 2D array as a rank 2 array.
"""

#####################################################################################################################
################################ 1. Using regular Python lists ######################################################

x = np.array([0, 1, 3, 5, 7])
# shape is size of array in each dimension
print(x, "   x has dimensions: (shape) ", x.shape)
# type of x is ndarray
print("x is an object of type: ", type(x))
# data type of elements of ndarray can be obtained by dtype attribute
# can handle more data-types than Python lists.
# ndarray can hold only single data type elements in it.
print("The elements in x are of type: ", x.dtype)
print("The array has total number of elements in it :", x.size)

x = np.array([1, 2, "hello"])
print(x, x.shape, type(x), x.dtype, x.size)
# We can see that even though the Python list had mixed data types, the elements in x are all of the same type, namely

# rank 2 ndarray
x = np.array([[1, 2.2, 3], [4, 5, 6], [7, 8.8, 9], [10, 11, 12.12]])
print(x, x.shape, type(x), x.dtype, x.size)
# shape attribute returns the tuple (4,3) telling us that Y is of rank 2 and it has 4 rows and 3 columns.
# The .size attribute tells us that Y has a total of 12 elements.

# This is called upcasting. Since all the elements of an ndarray must be of the same type,
# in this case NumPy upcasts the integers in z to floats in order to avoid losing precision in numerical computations.


# Numpy assigns data type of elements when we input them
#  You can specify the dtype
z = np.array([2, 4.5, 7, 89.99, 6.3], dtype=np.int64)
print(z, type(z), z.dtype)   # The elements in x are of type: int64
# Specifying the data type of the ndarray can be useful in cases when you don't want NumPy to accidentally
# choose the wrong data type, or when you only need certain amount of precision
# in your calculations and you want to save memory.

# you can save np array to file and load it later
np.save("saved_array_to_file", x)
y = np.load("saved_array_to_file.npy")
print("\n\nloaded from file ...", y, y.dtype, y.size, y.shape)



#####################################################################################################################
################################ 2. Using built-in NumPy functions ##################################################
print("\n\n\n\n")
# creates ndarray of given shape (input tuple x*y*z*... dimension)
a = np.zeros((2, 3))
print(a)
# default dtype of elements is float, we can change it by providing dtype
a = np.ones((2, 3, 4), dtype=int)
print(a, a.size, a.dtype, a.shape)

# np.full function will create matrix will all values given by second params (similar to ones, zeros)
# with the same data type as the constant value used to fill in the array.
a = np.full((2, 3), 4.5)
print(a, a.size, a.dtype, a.shape)
# fundamental array in Linear Algebra is the Identity Matrix. An Identity matrix is a square matrix that has
# only 1s in its main diagonal and zeros everywhere else.
# Identity matrix is also diagonal matrix, where values are only on diagonal, and zero elsewhere, a square matrix
b = np.eye(5)  # as identity matrix is always square matrix
print(b, b.size, b.dtype, b.shape)

# diagonal matrix
c = np.diag([10, 20, 30, 40])
print(c, c.size, c.shape, c.dtype)

# to create ndarrays that have evenly spaced values within a given interval.
# similar to range in python (which creates iterable sequence);
# it excludes upper limit from calculation. upper limit is exclusive
x = np.arange(10)
print(x, x.size, x.shape, x.dtype)
x = np.arange(4, 11)
print(x, x.size, x.shape, x.dtype)
x = np.arange(1, 10, 3)  # here step is 3, which means it is distance between two adjacent values in array
print(x, x.size, x.shape, x.dtype)

# non-integer steps are required, it is usually better to use the function np.linspace(start, stop, N=50)
# function returns N evenly spaced numbers over the closed interval, both start and stop inclusive
print("\n\n")
b = np.linspace(0, 10, 5)
print(b, b.size, b.shape, b.dtype)  # size will always be N
# default number of elements in the specified interval will be N= 50.
b = np.linspace(0, 10)
print(b, b.size, b.shape, b.dtype)  # size will always be N

# arange uses step between values, where linspace uses number of elements we want in particular interval
# we can exclude endpoints in linspace by argument endpoint = False
a = np.linspace(2.5, 25, 10)
print(a, a.shape, a.dtype)
a = np.linspace(0, 25, 10)
print(a, a.shape, a.dtype)
a = np.linspace(0, 25, 10, endpoint=False)
print(a, a.shape, a.dtype)


print("\n\n\n")
# we have only used the built-in functions np.arange() and np.linspace() to create rank 1 ndarrays.
# We can create rank 2 array by combining it with reshape()
# np.reshape(ndarray, new_shape) , new_shape should be compatible with ndarray
x = np.arange(20)
y = np.reshape(x, (4, 5))  # second inout is tuple for new shape
print("original ndarray :", x, x.size, x.shape)
print("ndarray after reshape", y, y.size, y.shape)
print("reshape with method ", x.reshape((4, 5)))
print("rank 2 ndarray with linspace ", np.linspace(0, 50, 10, endpoint=False).reshape((5, 2)))


############ Random array ###########

# We create a 2 x 5 ndarray with random floats in the half-open interval [0.0, 1.0).
x = np.random.random((2, 5))
print("radom ndarray ", x, x.dtype, x.size)

# create ndarrays with random integers within a particular interval  np.random.randint(start, stop, size = shape)
# end is exclusive
x = np.random.randint(5, 18, (2, 6))
print("random int [start, stop) rank 2 ndarray ", x, x.dtype, x.size, x.shape)

# In some cases, you may need to create ndarrays with random numbers that satisfy certain statistical properties.
# For example, you may want the random numbers in the ndarray to have an average of 0. NumPy allows you create random
# ndarrays with numbers drawn from various probability distributions.

# The function np.random.normal(mean, standard deviation, size=shape), for example, creates an ndarray with
# the given shape that contains random numbers picked from a normal (Gaussian) distribution
# with the given mean and standard deviation.
x = np.random.normal(0, 0.1, size=(50, 50))
print(x, x.size, x.shape, x.dtype, type(x))
print(x.min(), x.max(), x.mean(), x.std(), "positive and negative number :", (x < 0).sum(), (x > 0).sum(), type((x<0)))
# As we can see, the average of the random numbers in the ndarray is close to zero, both the maximum and minimum
# values in X are symmetric about zero (the average), and we have about the same amount
# of positive and negative numbers.


p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q = np.array(p)
# print("calculation "(p < 5))   gives an error
print("second ", (q < 5))  # return ndarray o true and false

# create a 4 x 4 ndarray that only contains consecutive even numbers from 2 to 32 (inclusive)
x = np.linspace(2, 32, 16, dtype=int).reshape((4, 4))
print(x)
