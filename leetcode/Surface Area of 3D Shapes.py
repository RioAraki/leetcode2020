def surfaceArea(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # accumulate each cube
    # when counting cube's surface area, delete the area that are covered by previous cube.
    ret = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            # surface area, up and bottom count as 1*2, other four sides as height*4
            ret += grid[i][j] * 4 + 2
            if i - 1 >= 0:
                ret -= min(grid[i][j], grid[i - 1][j]) * 2
            if j - 1 >= 0:
                ret -= min(grid[i][j - 1], grid[i][j]) * 2
    return ret


if __name__ == "__main__":
    pass