def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return []

    w, h = len(matrix[0]), len(matrix)
    di = (1, 0)
    cur = (0, w - 1)
    # the first row would always be visited first
    ret = matrix[0]

    def turn(dir):
        return (dir[1], -dir[0])

    spiral = 1
    counter = 0
    while len(ret) < w * h:
        if not di[0]:
            step = w - spiral
        elif not di[1]:
            step = h - spiral

        while step != 0:
            x, y = tuple(a + b for a, b in zip(cur, di))
            ret.append(matrix[x][y])
            cur = (x, y)
            step -= 1
        counter = 1 - counter
        if not counter % 2:
            spiral += 1
        di = turn(di)
    return ret