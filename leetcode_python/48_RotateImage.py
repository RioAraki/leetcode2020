
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    # the original idea is ok, but did not catch the core of rotation
    # miss the row and column in the middle without round up
    # n // 2 would round down e.g. 7 // 2 would be 3, where as 7 - (7 // 2) is 4 which would include the middle of the row for odd sized rows.

    # the nature of right turn 90 degree (x,y) = (-y, x)
    # ~ in python -> 2 complemnt 1 => -2 ; 10 => -11

    n = len(matrix)
    for i in range(n // 2):
        # tricky here
        for j in range(n - n//2):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]



#     if n % 2 == 1:
#         mid = n // 2
#         for i in range(mid+1):
#             for j in range(mid+1):
#                 matrix[mid - i][mid + j], matrix[mid + i][mid + j], matrix[mid + i][mid - j], matrix[mid-i][mid-j] =\
#                 matrix[mid-i][mid-j], matrix[mid-i][mid+j], matrix[mid+i][mid+j], matrix[mid+i][mid-j]
#     else:
#         mid = n // 2 - 0.5
#         for i in range(mid+1):
#             for j in range(mid+1):
#                 i, j = i-0.5, j-0.5
#                 matrix[int(mid - i)][int(mid + j)], matrix[int(mid + i)][int(mid + j)],\
#                 matrix[int(mid + i)][int(mid - j)], matrix[int(mid-i)][int(mid-j)] =\
#                 matrix[int(mid-i)][int(mid-j)], matrix[int(mid-i)][int(mid+j)],\
#                 matrix[int(mid+i)][int(mid+j)], matrix[int(mid+i)][int(mid-j)]
#
#     return matrix
# test = [[1,2,3],[4,5,6],[7,8,9]]
# print(rotate(test))