class Solution:

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        # 1. start with the reverse diagonal, check if both side has a lower(same) height, if yes -> in output
        # 2. when checking diagonal, if one side >= diagonal >= other side, put high side in output
        # 3. follow 2, recursively check if 2's surrounding has higher(same) height, also put that one in output

        def checkNeighbor(x, y, matrix, res, neighbor):
            if (x, y) not in neighbor:
                print('add neighbor: ' + str(x) + ', ' + str(y))
                neighbor.add((x, y))
                res.add((x, y))
                # up
                if x - 1 >= 0:
                    if matrix[x - 1][y] >= matrix[x][y]:
                        checkNeighbor(x - 1, y, matrix, res, neighbor)
                # left
                if y - 1 >= 0:
                    if matrix[x][y - 1] >= matrix[x][y]:
                        checkNeighbor(x, y - 1, matrix, res, neighbor)
                # down
                if x + 1 < h:
                    if matrix[x + 1][y] >= matrix[x][y]:
                        checkNeighbor(x + 1, y, matrix, res, neighbor)
                # right
                if y + 1 < w:
                    if matrix[x][y + 1] >= matrix[x][y]:
                        checkNeighbor(x, y + 1, matrix, res, neighbor)

        def checkBorder(x, y, matrix, res, neighbor):
            print('now checking border: ' + str(x) + ', ' + str(y))
            # -1 -> invalid; 0 -> short 1 -> high or equal
            u, d, l, r = -1, -1, -1, -1  # one flag for each side
            center = matrix[x][y]
            # up
            if x - 1 >= 0:
                u = 0 if matrix[x - 1][y] < center else 1
            # left
            if y - 1 >= 0:
                l = 0 if matrix[x][y - 1] < center else 1
            # down
            if x + 1 < h:  # Error 4: index out of range
                d = 0 if matrix[x + 1][y] < center else 1
                # right
            if y + 1 < w:  # Error 4: index out of range
                r = 0 if matrix[x][y + 1] < center else 1

            res.add((x, y))
            neighbor.add((x, y))

            if u + l != 2:
                if r == 1:
                    checkNeighbor(x, y + 1, matrix, res, neighbor)
                if d == 1:
                    checkNeighbor(x + 1, y, matrix, res, neighbor)
            if r + d != 2:
                if u == 1:
                    checkNeighbor(x - 1, y, matrix, res, neighbor)
                if l == 1:
                    checkNeighbor(x, y - 1, matrix, res, neighbor)

        h = len(matrix)
        if h == 0:
            return []

        res = set()
        w = len(matrix[0])

        # see how the border forms according to different height and width
        counter = w if (w < h) else h
        print(counter)
        neighbor = set()

        for i in range(counter):
            checkBorder(i, w - 1 - i, matrix, res,
                        neighbor)  # Error 4: index out of range because i put w-i rather than w-1-i

        return list(res)

# Error 1: set is not built-in, need to from sets import Set
# Error 2: counter is already a num, shouldnt use len(counter)
# Error 3: didnt put helper function before main function
# Error 5: wrong return value -> # Error 5.5: Set cannot save list
# Error 6: forget = when check neighbor
# Error 7: misunderstand the question, diagonal is regarded as both atlantic and pacific
# Error 8: forgot null check
#### Ultimate error: wrong understand the question, im fucked