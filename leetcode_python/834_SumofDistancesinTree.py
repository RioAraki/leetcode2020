class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 1. From one point there must be a path to the other point, form a list of list A, each list is all paths from point to other points.
        # 2. Try to find the shortest distance of all by applying BFS:
        # 1. Loop through all input and fill these length 1 pathes in A.
        # 2. try to extend length 1 paths to length 2 to find fill more in A
        # 3. Repeat 3 until all paths are found?

        # create a dictionary shows every point connects to which point
        unit_path = {}  # Error 5: logical, forget to count path reversely
        for unit in edges:
            if unit[0] not in unit_path:
                unit_path[unit[0]] = [unit[1]]  # Error 2: wrong order to assign value in key in dictionary
            else:
                if unit[1] not in unit_path[unit[0]]:
                    unit_path[unit[0]].append(unit[1])
            if unit[1] not in unit_path:
                unit_path[unit[1]] = [unit[0]]
            else:
                if unit[0] not in unit_path[unit[1]]:
                    unit_path[unit[1]].append(unit[0])

        # always make sure first element < second element
        def _safe(lst):  # Error 1: forget to def function
            if lst[0] < lst[1]:
                return [lst[0], lst[1]]
            else:
                return [lst[1], lst[0]]

        # make a 2d list, A[x][y] means the shortest path from x to y, dont set up when x > y
        A = [[0 for x in range(N)] for y in range(N)]

        cur_len = 0  # current length
        path = 0  # total number of path being filled
        prev_len_list = []  # maintain a list of paths in previous length
        cur_len_list = []  # maintain a list of paths in current length

        # if there are n edges, total valid path would be (n-1) + (n-2) + ... + 1 = n(n-1)/2

        while path < (N * (N - 1) / 2):  # Error 3: forget capitalize n  # Error 4: wrong syntax doing calculation
            # print ('in loop, path: ' + str(path) + ', full: ' + str(N*(N-1)/2))
            cur_len += 1  # every loop we check path with length n while n is loop number
            if cur_len == 1:  # initial case, all length 1 path must be the input
                for coor in edges:
                    s = _safe(coor)
                    A[s[0]][s[1]] = cur_len
                    A[s[1]][s[0]] = cur_len
                    path += 1
                prev_len_list = edges

            # Recursively: extend one length path from prev_len_list
            else:
                for coor in prev_len_list:
                    coor = _safe(coor)
                    for p in unit_path[coor[0]]:
                        if coor[1] != p:
                            s = _safe([coor[1], p])
                            if A[s[0]][s[1]] == 0:
                                A[s[0]][s[1]] = cur_len
                                A[s[1]][s[0]] = cur_len
                                path += 1
                                cur_len_list.append([s[0], s[
                                    1]])  # Error6: logical error, we want to append the coordinate, not the value at that coor

                    for p in unit_path[coor[1]]:
                        if coor[0] != p:
                            s = _safe([coor[0], p])
                            if A[s[0]][s[1]] == 0:
                                A[s[0]][s[1]] = cur_len
                                A[s[1]][s[0]] = cur_len
                                path += 1
                                cur_len_list.append([s[0], s[
                                    1]])  # Error6: logical error, we want to append the coordinate, not the value at that coor

                prev_len_list = cur_len_list
                cur_len_list = []

        ret = []
        # print (A)
        for row in A:  # Error 7 : wrong imagination about the structure of A because i
            ret.append(sum(x for x in row))
        return ret

