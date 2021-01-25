import numpy as np
#import matplotlib.pyplot as plt
import numpy.linalg as la # lin alg linrary in np has a lot of fxns, e.g., eigen values; important for data science
import timeit


def array_descriptor_fxns():
    """
    Looking at different descriptor functions of numpy arrays
    :return:
    """
    arr1 = np.array([1, 2, 3, 4, 5])  # np array as list
    print('dtype:', arr1.dtype)  # shows what data type is stored

    arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # array of arrays
    print('ndim:', arr2.ndim)  # shows how many dimensions are in the array
    print('shape:', arr2.shape)

    # access different values within array of arrays
    print(arr2[1, 2])   # accesses first array, and then accesses 3rd item

    # three dimensional array
    arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    return arr3


def generating_arrays():
    """
    Looking at numpy array functions for generating arrays
    :return:
    """

    # generates a 1D array with values 0-4
    arr1 = np.arange(5)

    # generates a 1D array with values 20-99
    arr2 = np.arange(20, 100)

    # generates a 1D array with values 1-20 with jumps of 2
    arr3 = np.arange(1, 21, 2)

    # np.arange(10) returns array of values 0-9.
    # but the np.random.permutations shuffles the values in random fashion
    arr4 = np.random.permutation(np.arange(10))

    # takes a given array and reshapes it to a matrix that is 2x5
    arr5 = arr4.reshape(2, 5)

    # generates an array with 100 values. Each value is between 0 and 1
    arr6 = np.random.rand(100)
    
    # .randn returns a sample from the 'standard normal' distribution.
    arr7 = np.random.randn(100)

    # to look at the general distribution of the random values, using
    # matplotlib to plot a histogram
    # plt.hist(arr6)
    # plt.hist(arr7)

    return arr1


def array_slicing():
    ' array[start:end:step] '
    a = np.arange(100)
    
    b = a[3:10]
    b[0] = -1200    # this will also update the element in a
    
    c = a[3:10].copy()
    c[0] = 3    # this will not update the element in a
    
    # finding the index of -1200 in a
    idx = np.argwhere(a==-1200)[0][0]   # adding the [][] will get you the idx of the element
    a[idx] = 3      # resetting idx to element 3
    
    # 2D indices
    d = np.round(10*np.random.rand(5,4))
    d[1, 2]     # finds element in row idx 1 (row 2)  and column idx 2 (col 3)
    
    # access rows/columns of 2D 
    d[1,:]  # all col values in 2nd row
    d[:,1]  # all of the row values in 2nd column
    
    # access submatrix
    d[1:3,2:4]  # row 2&3, then of those rows, picks cols 3&4
    
    # transpose matrix
    e = d.T
    
    # generate inverse of a matrix.
    f = np.random.rand(3,3)
    g = la.inv(f)    
    
    # sorting matrices
    'if you have more than a 2d array, axis can be 2+'
    f.sort(axis=0)  # sort based on values in column
    f.sort(axis=1)  # sort based on values in row

    return b
    

def array_masking():
    """ array[index_array] is also known as masking. generates a copy
     different than slicing, which generates a view """
    
    a = np.arange(5)
    b = a[[1, 3, 4]]    # returns index 1, 3, 4
    c = a[[True, False, True, False, True]] # returns index 0, 2, 4
    d = a[a < 4] # this type of boolean array returns all elements that are < 4
    e = a[(a < 4) & (a > 1)] # returns all elements 1 < x < 4]

    """ difference between & vs. and:
        and operator is used when both sides of and is one object and has one true value
        (either true or false)
        & operator is used when left/right side can be arrays and each element of those
        arrays can be true or false
    """
    return e


def array_broadcasting():
    """ allows you to broadcast an integer into a matrix when trying to
    update all elements of an array by the same factor.
    """
    
    a = np.array([[2,3],[5,9]])
    b = a + 5 # adds 5 to each element in the array
    
    c = np.array([[1],[3]])
    d = a + c   # this will add the element '1' from c to each element in the 1st row of a, and 3 for 2nd.

    return a


def universal_functions():
    a = np.round(10*np.random.rand(2,3))    # e.g. of broadcast
    # a = a + 3   # another e.g. of broadcast
    # a = a + (np.arange(2).reshape(2,1))
    
    b = np.round(10*np.random.rand(2, 2))
    
    # values fed to function must be in a tuple
    c = np.hstack((a, b))
    
    # sorting array
    d = np.random.permutation(np.arange(10))
    d = np.sort(d)  # default in ascending order
    d = d[::-1] # now sorted in descending order
    
    # sorting string array.
    e = np.array(["abc", "howareyou", "u785", "13er"])
    e = np.sort(e)  # sorts according to alphanumeric order
    


def main():

    # arr1 = array_descriptor_fxns()
    # arr2 = generating_arrays()
    # arr3 = array_slicing()
    # arr4 = array_masking()
    # arr5 = array_broadcasting()
    # arr6 = universal_functions()
    


main()
