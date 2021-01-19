import numpy as np


def array_practice():
    arr1 = np.array([1, 2, 3, 4, 5])  # np array as list
    print(arr1.dtype)  # shows what data type is stored

    arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # array of arrays
    print(arr2.ndim)  # shows how many dimensions are in the array

    # access different values within array of arrays
    print(arr2[1, 2])   # accesses first array, and then accesses 3rd item

    # three dimensional array
    arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    return arr3


def main():

    arr = array_practice()
    print(arr[1, 1, 2])
    print(arr.ndim)


main()
