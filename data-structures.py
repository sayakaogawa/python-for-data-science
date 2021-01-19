"""
Data Structures
"""


def part1():
    """Practicing data structures"""
    # define a list
    l = [1, 3, 4.9, "name", 3]

    # define a tuple
    t = (1, 3, 4.9, "name", 3)
    t2 = ('a', 'b')

    # define a set. Remember wont include dups
    s = {1, 3, 4.9, "name", 3}

    # define a dictionary
    d = {23: "two-three", 'B': 43, 'C': 'CCD'}

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

    # make a list of x^2 from 0-9
    l3 = [x ** 2 for x in range(10)]

    # make a set of x^2 from range 2-20, with step 3
    s2 = {x ** 2 for x in range(2, 20, 3)}


def get_data_from_user():
    """ Lets say you are a teacher and you have different student
        records containing id of a student and the marks list in
        each subject where different students have taken different
        number of subjects. All these records are in hard copy.
        You want to enter all the data in the computer and want to
        compute the average marks of each student and display."""

    student_dict = {}

    while True:
        studentID = input("Enter Student ID: ")
        marks_list = input("Enter the marks by comma separated values: ")
        more_students = input("Enter 'yes'/'no' for adding more students: ")

        if studentID in student_dict:
            print(studentID, "is already inserted")
        else:
            # return list of string values of marks stored
            student_dict[studentID] = marks_list.split(',')

        if more_students.lower() == "no":
            return student_dict


def get_avg_marks(dict):
    """
    Takes in student dictionary and finds the average marks for each student
    :param student_dict:
    :return:
    """

    avg_marks_dict = {}

    for x in dict:
        marks_lst = dict[x]
        sum = 0

        for marks in marks_lst:
            sum += int(marks)

        avg_marks_dict[x] = sum/len(marks_lst)

    return avg_marks_dict


def main():

    student_data = get_data_from_user()
    avg_marks = get_avg_marks(student_data)
    for x in avg_marks:
        prin"Student:", x, "Average Marks:", avg_marks[x])


main()
