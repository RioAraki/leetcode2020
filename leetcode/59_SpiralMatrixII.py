def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    if n == 0: return []

    def turn(di):
        return (di[1], -di[0])

    di = (1, 0)
    spiral = 1
    x, y = 0, n - 1
    size = n * n
    count = n
    counter = 0
    ret = [[0 for i in range(n)] for j in range(n)]
    ret[0] = [i for i in range(1, n + 1)]

    while count < size:
        step = n - spiral
        while step != 0:
            count += 1
            x, y = tuple(a + b for a, b in zip((x, y), di))
            ret[x][y] = count
            step -= 1
        counter = 1 - counter
        if not counter % 2:
            spiral += 1
        di = turn(di)
    return ret