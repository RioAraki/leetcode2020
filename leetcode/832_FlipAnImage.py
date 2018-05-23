def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    height, width = len(A), len(A[0])
    B = [[0 for x in range(height)] for y in range(width)]
    for h in range(len(A)):  # error1: forgot range()
        for w in range(len(A[0])):
            B[h][w] = 1 ^ A[h][abs(width - 1 - w)]
    return B

    # error 2: wrong logic 1 changed to -1 not 0
    # error 3: A is changed which should not be (dont understand python copy model)

    # lesson learnt:
    # Python uses call by object, if you pass immutable arguments like ints, strings or tuples, act like call by value
    # If we pass mutable arguments, they can be changed in place in the function, call by reference.
    # https://www.python-course.eu/passing_arguments.php

# Better solution
# its inplace, not creating new list

def flip_and_invert_image_better(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(len(A)):
        A[i] = [1 - x for x in A[i][::-1]]
    return A

    # Cheese to reverse list by [::-1]