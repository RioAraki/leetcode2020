# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/judge-route-circle/

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
