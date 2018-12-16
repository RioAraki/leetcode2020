class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # brute force? may tle
        # check each row/ column/ and diagonal

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        count = 0
        for r in range(len(grid[0]) - 2):
            for c in range(len(grid) - 2):

                # check each row, column, and both diagonals all have the same sum.
                if grid[c][r] + grid[c][r + 1] + grid[c][r + 2] == grid[c + 1][r] + grid[c + 1][r + 1] + grid[c + 1][
                    r + 2] == grid[c + 2][r] + grid[c + 2][r + 1] + grid[c + 2][r + 2] == grid[c][r] + grid[c + 1][r] + \
                        grid[c + 2][r] == grid[c][r + 1] + grid[c + 1][r + 1] + grid[c + 2][r + 1] == grid[c][r + 2] + \
                        grid[c + 1][r + 2] + grid[c + 2][r + 2] == grid[c][r] + grid[c + 1][r + 1] + grid[c + 2][
                    r + 2] == grid[c][r + 2] + grid[c + 1][r + 1] + grid[c + 2][r]:

                    # check each grid filled with distinct numbers from 1 to 9
                    if all(x in [grid[c][r], grid[c + 1][r], grid[c + 2][r], grid[c][r + 1], grid[c + 1][r + 1],
                                 grid[c + 2][r + 1],
                                 grid[c][r + 2], grid[c + 1][r + 2], grid[c + 2][r + 2]] for x in
                           [1, 2, 3, 4, 5, 6, 7, 8, 9]):
                        count += 1

        return count

    # Error 1: dumb error: forget to add count as return value
    # Error 2: logic error: mess up the number when trying to check if every subgrid has 1~9