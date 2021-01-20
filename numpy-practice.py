import numpy as np
import matplotlib.pyplot as plt


def array_part1():
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


def array_part2():
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

    # to look at the general distribution of the random values, using
    # matplotlib to plot a histogram
    print(plt.hist(arr6))

    return arr1


def main():

    # arr = array_part1()
    arr2 = array_part2()


main()
