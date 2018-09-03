# do it in-place

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    if len(matrix) and len(matrix[0]):

        h = len(matrix)
        w = len(matrix[0])

        h0, w0 = 0, 0

        h0 = 1 if any(matrix[x][0] == 0 for x in range(h)) else 0
        w0 = 1 if any(matrix[0][x] == 0 for x in range(w)) else 0

        if h > 1 and w > 1:

            for i in range(1, h):
                for j in range(1, w):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

            for i in range(1, h):
                if matrix[i][0] == 0:
                    matrix[i] = [0 for x in range(w)]

            for j in range(1, w):
                if matrix[0][j] == 0:
                    for x in range(h):
                        matrix[x][j] = 0

        if h0:
            for x in range(h):
                matrix[x][0] = 0

        if w0:
            matrix[0] = [0 for x in range(w)]