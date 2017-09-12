# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/judge-route-circle/
# Thoughts: set the initial position to 0, keep track of the current position, if current position after move finished
# is 0, then its a circle

class Solution(object):
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
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
# We can figure out how many elements could there be in each level (level1 -> 1; level2 -> 2; level3 -> 4; level4 -> 8)
# We can figure out which spot does the current element in each level -> leftchild = parent*2-1;rightchild = parent*2
# Get the biggest and smallest number in the list
# traverse through the list and find number in each level?

# copy from other user's answer for study purpose

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = [(root, 1, 1)]  # root -> node/ depth -> 1/ position -> 1
        cur_depth = left = ans = 1

        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))

                # a new depth just begins, update the cur_depth and most left position
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos

                # everytime make a compare and find current largest answer
                ans = max(pos - left + 1, ans)
        return ans

############################################################################################
# https://leetcode.com/problems/equal-tree-partition/description/
# Get the sum of the whole tree
# traverse through each element, check if the sum of its left children = everything else or
# sum of right children = everything else

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def sum_of_tree(node):
            left = right = 0
            if node.left:
                left = sum_of_tree(node.left)
            if node.right:
                right = sum_of_tree(node.right)
            return node.val + left + right

        # You cannot return something in the middle, the idea is wrong. You should put the recursive result in an accumulative place

        def check_partition(node):
            if not node:
                return 0
            s = node.val + check_partition(node.left) + check_partition(node.right)
            if node is not root:
                sublist.add(s * 2)
            return s

        sublist = set()
        root_sum = sum_of_tree(root)
        check_partition(root)

        return root_sum in sublist

# Still not good at solving tree related problem -> not good at writing recursion, need more practice

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/split-array-into-consecutive-subsequences/
# Probably workable way, but exceed time limit because the two for loop and sorted function!


    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lists = []
        lengths = []

        for num in nums:
            put_in = False
            for list in lists:
                if not put_in:
                    if num - 1 == list[-1]:
                        put_in = True
                        list.append(num)
            if not put_in:
                lists.append([num])
            lists = sorted(lists, key=len)
            # print lists
            # print sorted(lists, key = len)

        return len(lists[0]) >= 3

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/remove-9/
# go through each number, if 9 is detected, skip it
# time limit exceeded, this way definitely work but need a more efficient solution
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        num = 0

        last = []
        mid = []
        current = []

        while count < n + 1:

            list_num = list(str(num))
            if '9' not in list_num:
                count += 1
            num += 1
            last = mid
            mid = current
            current = [num, count]
        if current[1] == n:
            return current[0]
        elif mid[1] == n:
            return mid[0]
        elif last[1] == n:
            return last[0]

# Better solution, 9 base:
# change n to 9 base
    def newInteger(self, n):
        ans = ''
        while n:
            ans = str(n%9) + ans
            n /= 9
        return int(ans)

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-47/problems/non-decreasing-array/

# Time limit Exceeded
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_list = nums[:]
        for index in range(len(nums_list)):
            nums_list.pop(index)
            if nums_list == sorted(nums_list):
                return True
            nums_list = nums[:]
        return False

# delete each number of the decsending pair and see if the modified list is a non-descending one
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_list1 = nums[:]
        nums_list2 = nums[:]
        count = 0

        for index in range(len(nums)):

            if index + 1 <= len(nums) - 1:
                # print index, index + 1, nums_list[index], nums_list[index+1]
                if nums[index] > nums[index + 1]:
                    nums_list1.pop(index)
                    nums_list2.pop(index + 1)
                    if nums_list1 == sorted(nums_list1) or nums_list2 == sorted(nums_list2):
                        return True
                    return False
        return True
		
############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-47/problems/path-sum-iv/
# recurse from each leaf, go up one level each time and add it to a sum
	def pathSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        last = get_pos(nums[-1],0)
        sum = 0

        def get_pos(num,pos):
            return int(str(num)[pos])

        def is_leaf(num, nums):
            depth = get_pos(num,0)
            pos = get_pos(num,1)
            child_val_left = (depth+1)*100 + (2*pos-1)*10
            child_val_right = (depth+1)*100 + (2*pos)*10
            for element in nums:
                if child_val_left <= element < child_val_left + 10 or child_val_right <= element < child_val_right + 10:
                    return False
            return True

        for num in nums:
            if is_leaf(num, nums):
                print("now in leaf: " + str(num))
                depth = get_pos(num,0)
                pos = get_pos(num,1)
                val = get_pos(num,2)
                next_depth = depth - 1
                next_pos = int((pos+1)/2)
                sum += val
                while depth > 0:
                    depth = next_depth
                    pos = next_pos
                    for num1 in nums:
                        if (depth*100 + pos*10) <= num1 < (depth*100 + pos*10 + 10):
                            val = get_pos(num1,2)
                            next_depth = depth-1
                            next_pos = int((pos+1)/2)
                            sum += val
                            break
        return sum
			
############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-47/problems/beautiful-arrangement-ii/
# In a pattern 1 n 2 n-1 3 n-2 ...
# Get solution from leetcode discuss
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        l, r, res = 2, n, [1]
        for _ in range(k - 1):
            if len(res) & 1:
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        if len(res) & 1:
            res.extend(range(l, r + 1))
        else:
            res.extend(range(r, l - 1, -1))
        return res

############################################################################################
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Get the number of counts of each number from 1 in the table and find the kth one
# TLE, the answer is not good enough since I tracked the whole thing from 1, I only need to know there the kth answer is, would figure out how to do it later.
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def get_factor(num):
            myList = []
            for i in range(1, int(num ** 0.5 + 1)):
                if num % i == 0:
                    if (i != num/i):
                        myList.append([i, int(num/i)])
                        
                    else:
                        myList.append([i,i])
            return myList 
        
        num = 1
        res = []
        
        while len(res) < k:
            table = get_factor(num)
            count = 0
            # print ("current number: " + str(num) + ", current list: " + str(table))
            for pair in table:
                # if both elements in pair are smaller than m, n -> count 2 times
                if pair[0] <= m and pair[1] <= n:
                    count += 1
                if pair[1] <= m and pair[0] <= n and pair[0] != pair[1]:
                    count += 1
            
            res += count * [num]
            num += 1
            # print ("this number's count: " + str(count))
            # print ("current result list: " + str(res))
            
        return res[k-1]

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-44/problems/two-sum-iv-input-is-a-bst/
# maintain a list while traverse through the tree, if found the needed value in the list return false

     def findTarget(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: bool
            """
            self.flag = False
            supplement = []

            def add_to_list(node):
                if node.val in supplement:

                    self.flag = True
                supplement.append(k - node.val)
                if node.left:
                    add_to_list(node.left)
                if node.right:
                    add_to_list(node.right)
            add_to_list(root)
            return self.flag

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-44/problems/maximum-binary-tree/
# 1. find largest number in the list, divide two subarray
# 2. make it the node value of tree, recursively build left and right child
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def max_in_tree(num_list):
            max = -1
            max_idx = -1
            for index in range(len(num_list)):
                if num_list[index] > max:
                    max_idx = index
                    max = num_list[index]
            return max_idx, num_list[:max_idx], num_list[max_idx + 1:]

        def solve(nums):
            idx, first, second = max_in_tree(nums)
            if idx != -1:
                node = TreeNode(nums[idx])  # TreeNode is defined in leetcode
                node.left, node.right = solve(first), solve(second)
            else:
                node = None
            return node

        return solve(nums)


############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-48/problems/second-minimum-node-in-a-binary-tree/
    def findSecondMinimumValue(self, root):
        """:type root: TreeNode
        :rtype: int
        """

        def compare(node):
            if node.left:
                if node.left.val != node.right.val:
                    if node.left.val == node.val:
                        second_list.append(node.right.val)
                        compare(node.left)
                    else:
                        second_list.append(node.left.val)
                        compare(node.right)
                else:
                    compare(node.left)
                    compare(node.right)

        second_list = []
        compare(root)
        second_list = sorted(second_list)

        if len(second_list):
            return second_list[0]
        else:
            return -1

############################################################################################
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(node, L, R):
            if node.val < L:
                node = trim(node.right, L, R)
            if node.val > R:
                node = trim(node.left, L, R)
            if L <= node.val <= R:
                while node.left and node.left.val < L:
                    node.left = node.left.right
                while node.right and node.right.val > R:
                    node.right = node.right.left
                if node.left:
                    trim(node.left, L, R)
                if node.right:
                    trim(node.right, L, R)
            return node

        return trim(root, L, R)

############################################################################################
# https://leetcode.com/problems/maximum-swap/description/
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        def check_desc(num):
            num_list_des = sorted(num_list, reverse=True)
            for index in range(len(num_list)):
                if num_list[index] != num_list_des[index]:
                    return index
            return -1

        num_list = list(str(num))
        init = check_desc(num)

        if init == -1:
            result = num
        else:
            safe_list = num_list[:init]
            work_list = num_list[init:]

            largest = 0
            l_index = 0
            for index in range(len(work_list)):
                if work_list[index] >= largest:
                    largest = work_list[index]
                    l_index = index
            if l_index != 0:
                work_list[l_index] = work_list[0]
                work_list[0] = largest

            position = 1
            result = 0
            # print work_list
            result_list = safe_list + work_list
            for pos in reversed(result_list):
                result += position * int(pos)
                position = position * 10
        return result

############################################################################################
# https://leetcode.com/problems/bulb-switcher-ii/description/
# Get solution from discussion section
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if m == 1 and n == 2:
            return 3
        if m == 1 or n == 2:
            return 4
        if m == 2:
            return 7
        return 8

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-43/problems/find-duplicate-subtrees/

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-49/problems/longest-continuous-increasing-subsequence/

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        temp = []
        for num in nums:
            # print num
            if len(temp) == 0:
                temp.append(num)
            else:
                if num > temp[-1]:
                    temp.append(num)
                else:
                    if longest < len(temp):
                        longest = len(temp)
                    temp = [num]
        if len(temp) > longest:
            longest = len(temp)
        return longest

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-49/problems/implement-magic-dictionary/
    class MagicDictionary(object):
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.diction = []

        def buildDict(self, dict):
            """
            Build a dictionary through a list of words
            :type dict: List[str]
            :rtype: void
            """
            for word in dict:
                self.diction.append(word)

        def search(self, word):
            """
            Returns if there is any word in the trie that equals to the given word after modifying exactly one character
            :type word: str
            :rtype: bool
            """

            for w in self.diction:
                if len(w) == len(word):
                    counter = 0
                    for index in range(len(w)):
                        if w[index] == word[index]:
                            counter += 1
                    if counter + 1 == len(w):
                        return True
            return False

############################################################################################
# https://leetcode.com/contest/leetcode-weekly-contest-49/problems/cut-off-trees-for-golf-event/
def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        from Queue import PriorityQueue
        
        tree_list = []
        
        # scan the whole forest and sort it by length of tree
        def scan():
            for row_idx in range(len(forest)):
                for tree_idx in range(len(forest[row_idx])):
                    if forest[row_idx][tree_idx] > 1:
                        tree_list.append([forest[row_idx][tree_idx],(row_idx, tree_idx)])
            tree_list.sort(key = lambda ele: ele[0])
        
        # astar search from a beginning point to a ending point
        def astar(start, end):
            unvisit = PriorityQueue() 
            unvisit.put(start, 0)
            came_from = {}
            cost_so_far = {}
            came_from[start] = None # No previous for start
            cost_so_far[start] = 0
            while not unvisit.empty():
                current = unvisit.get()
                if current == end:
                    break
                neighbour = find_neighbour(current)
                for ele in neighbour:
                    new_cost = cost_so_far[current] + next_cost(ele)
                    if ele not in cost_so_far or new_cost < cost_so_far[ele]:
                        cost_so_far[ele] = new_cost
                        priority = new_cost + heuristic(ele, end)
                        unvisit.put(ele, priority)
                        came_from[ele] = current
            return came_from, cost_so_far 
        
        # find the manhatten distance between two position
        def heuristic(a, b):
            (x1, y1) = a
            (x2, y2) = b
            return abs(x1 - x2) + abs(y1 - y2)
        
        # find availble neighbor of a position
        def find_neighbour(pos):
            output = []
            if pos[0] > 0:
                output.append((pos[0]-1, pos[1]))
            if pos[0] < len(forest[0]) -1:
                output.append((pos[0]+1, pos[1]))
            if pos[1] > 0:
                output.append((pos[0], pos[1]-1))
            if pos[1] < len(forest) -1:
                output.append((pos[0], pos[1]+1))
            return output
        
        # find the cost from current to next
        def next_cost(ele):
            if forest[ele[0]][ele[1]] > 0:
                return 1
            # want to return inf actually
            return 99999
                
        
        scan()
        cur = (0,0)
        total_cost = 0
        for pos in tree_list:
            print(str(cur))
            nxt = pos[1]
            path, cost = astar(cur,nxt)
            total_cost += cost
            cur = nxt
        return total_cost
