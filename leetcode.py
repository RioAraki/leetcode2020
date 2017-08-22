# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/judge-route-circle/
# Thoughts: set the initial position to 0, keep track of the current position, if current position after move finished
# is 0, then its a circle


def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """

    # Cannot use tuple because it is immutable
    current = [0, 0]

    # each_move = moves.split("") -> cannot go blank
    each_move = list(moves)
    # try to use dictionary to achieve switch case later
    for char in each_move:
        if char == "L":
            current[0] -= 1
        elif char == "R":
            current[0] += 1
        elif char == "U":
            current[1] -= 1
        else:
            current[1] += 1

    # for char in each_move:
    #     current = {
    #       'a': lambda x: x * 5,
    #       'b': lambda x: x + 7,
    #       'c': lambda x: x - 2
    #     }[value](x)

    if current[0] == 0 and current[1] == 0:
        # Captical T and F
        return True
    return False

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/find-k-closest-elements/

# build a new list which records the abs diff of each element and x, also keep track of it's original value and position     O(n)
# sort through its abs diff value     O(log(n))
# pick the first kth value, choose original value which forms a new list            O(n)
# sort the list    O(log(n))

def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    diffList = self.listModify(arr, x)
    result_list = []

    # lambda ->
    # diffList = diffList.sort(key= lambda tup: tup[0])
    diffList.sort(key=lambda tup: tup[0])

    for num in range(k):
        result_list.append(diffList[num][2])
    result_list.sort()

    return result_list

def listModify(self, arr, x):
    result = []
    smallest = 999999999999
    curr_index = 0
    for element in arr:
        new_ele = abs(x - element)
        result.append((new_ele, curr_index, element))
        if new_ele < smallest:
            smallest = new_ele
        curr_index += 1
    return result

#TODO: Use the way in http://bookshadow.com/weblog/2017/08/13/leetcode-find-k-closest-elements/ and resolve the problem!
############################################################################################

# https://leetcode.com/contest/leetcode-weekly-contest-46/problems/image-smoother/
# Stupid solution
def imageSmoother(self, M):
    """
    :type M: List[List[int]]
    :rtype: List[List[int]]
    """

    def check_remove(list, val):
        if val in list:
            list.remove(val)

    # try pass by reference?
    # result_matrix = M
    width, height = len(M), len(M[0])
    result_matrix = [[0 for i in range(width)] for j in range(height)]

    for row in range(width):
        for pixel in range(height):
            sur = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if pixel - 1 < 0:
                check_remove(sur, 1)
                check_remove(sur, 4)
                check_remove(sur, 7)
            if pixel + 1 > height - 1:
                check_remove(sur, 3)
                check_remove(sur, 6)
                check_remove(sur, 9)
            if row - 1 < 0:
                check_remove(sur, 1)
                check_remove(sur, 2)
                check_remove(sur, 3)
            if row + 1 > width - 1:
                check_remove(sur, 7)
                check_remove(sur, 8)
                check_remove(sur, 9)

            result = 0

            for num in sur:
                if num == 1:
                    result += M[row - 1][pixel - 1]
                if num == 2:
                    result += M[row - 1][pixel]
                if num == 3:
                    result += M[row - 1][pixel + 1]
                if num == 4:
                    result += M[row][pixel - 1]
                if num == 5:
                    result += M[row][pixel]
                if num == 6:
                    result += M[row][pixel + 1]
                if num == 7:
                    result += M[row + 1][pixel - 1]
                if num == 8:
                    result += M[row + 1][pixel]
                if num == 9:
                    result += M[row + 1][pixel + 1]

            result_matrix[row][pixel] = int(result / len(sur))
    return result_matrix

############################################################################################
# solution from leetcode user XuenanGuo

def imageSmootherXuenanGuo(self, M):

    # use map to use len function once only
    m,n = map(len, [M, M[0]])

    # smart way to copy the original list by value, avoid points to original variable.
    ans = [[M[i][j] for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            cnt = 1
            # zip to get x y coordinate together, dont need to get 0 0 value since we already included it
            for dx, dy in zip([1, 1, 1, 0, 0, -1, -1, -1], [1, 0, -1, 1, -1, 1, 0, -1]):
                x, y = i+dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    ans[i][j] += M[x][y]
                    cnt += 1
            ans[i][j] /= cnt
    return ans

############################################################################################
# We can figure out how many elements could there be in each level (level1 -> 1; level2 -> 2; level3 -> 4; level4 -> 8)
# We can figure out which spot does the current element in each level -> leftchild = parent*2-1;rightchild = parent*2
# Get the biggest and smallest number in the list
# traverse through the list and find number in each level?