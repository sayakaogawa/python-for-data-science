"""
Data Structures
"""


def main():

    # define a list
    l = [1, 3, 4.9, "name", 3]

    # define a tuple
    t = (1, 3, 4.9, "name", 3)
    t2 = ('a', 'b')

    # define a set. Remember wont include dups
    s = {1, 3, 4.9, "name", 3}

    # define a dictionary
    d = {23:"two-three", 'B':43, 'C':'CCD'}

    # append to list
    l = l + ["how", "are", 6, "you"]
    l.append(6.8)

    # concatenate two tuples together
    t3 = t + t2

    # append to set
    s.add(56)

    # append multiple elements to set
    s.update({23, "game"})

    # add new key value pair to dictionary
    d["newKey"] = "newValue"

    # remove element from list or dict
    del l[3]
    del d['C']

    # remove element from set
    s.remove('game')

    # make a copy of list/dict/set
    l2 = l.copy()


main()
