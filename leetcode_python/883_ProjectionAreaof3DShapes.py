def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    xy = 0
    yz = 0
    zx = 0
    for row in grid:
        xy += len(list(filter(lambda x: x > 0, row)))
        yz += max(row)

    for col in list(zip(*grid)):
        zx += max(col)

    return xy + yz + zx