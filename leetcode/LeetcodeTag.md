# Leetcode tag
For better categorizing

Redo all tags with **Redo** since I didn't manage to solve the issue without any help.
TODO: Add the general thoughts of solving each problem

# By topic
Linked list: 


1. Two Sum  
   **two pointers**, easy
2. Add two numbers  
   **linked list**, **Redo**, medium  
   Count sum + carry bit as the value of linked list. Carry bit may create one extra node for result.
3. Longest Substring Without Repeating Characters:  
   **two pointers**, medium
4. Median of Two Sorted Arrays  
    **array**,
    Find out the index of median. Set two pointers as the index of two lists, compare both `list[pointer]` find the smaller
    one, increment pointer for that list by 1, until index reaches median
5. Longest Palindrome Substring  
    **string**, **dynamic programming**  
    Write a function to find palindrome: select left and right index, see if string[left-1] == string[right+1], update the index accordingly
    Execute this function n times, n = length of string

    DP:   
        saved data: 2d array, dp[i,j] -> if string[i,j] could form a palindrome (put the length inside)
    
    
        
    

11. Container With Most Water    
    **array**, **two pointers**, easy, **Redo**, **Redone** pass
12. Integer to Roman    
	Each bit in integer would not affect each other to transform to roman, so just transfer it one by one according to the bit

13. Roman to Integer  
	Reverse of **Q12** Integer to roman, increment all roman from left to right excecpt for those input[i] < input[i+1]  (eg: IV,XL), these are for 4s and 9s.

14. Longest Common Prefix  
	**Easy** find the shortest string, iterate every string's char at index i, use enumerate for getting i in one line

15. 3Sum  
	Same as **Q14** 2sum

16. 3Sum Closest  
	Same ide as **Q14** **Q15** 3sum/ 2sum

17. Letter Combinations of a Phone Number  
	**Redo**, use a lot of function programming and itertools (filter, itertools.product) to solve this question in a smart way.

18. 4Sum  
	**Redo**, same as **Q14** **Q15** **Q16** based on 3sum and 2sum. Need to do a lot of corner case check to avoid duplicate items, overloop and TLE

19. Remove Nth Node From End of List  
	**Redo**, **linked list**, should do it in one loop, use recursion to get the position of node that needs to be removed

20. Valid Parentheses  
	one-pass, same to most parentheses problems, use stack to check parentheses matches

21. Merge Two Sorted Linked Lists  
	**Redo**, **linked list**, Recursion on linked list

22. Generate Parentheses  
	**Redo**, **linked list**, use recursion to generate all combinations of parentheses.

23. Merge k Sorted Linked Lists    
	**Redo**, **linked list**, use priority queue to always find the linked list with smallest value

24. Swap Nodes in Pairs  
	**Redo**, **linked list**, understand the pattern of swapping and change the "next" pointer of each node accordingly

25. Swap Nodes in k-group  
	**Redo**, **linked list**, use a counter to find every reverse group, use recursion to do the swap from last group to first group

32. Longest Valid Parentheses  
	**string**, **stack**, **dp**, dp: 1d array, dp[i] records longest valid parentheses end at S[i]

	make sure left ( always > 0. when meet right parenthesis, valid count = valid parenthesis count from previous parenthesis + 2
	We want to recursively fond previous valid parenthesis until it hits beginning of dp.

33. Search in Rotated Sorted Array  
	**Redo**, **binary search**, Set lo and hi, binary search to find the point where rotate begins. Binary search to find where target locates by comparing rotating point and middle index.

34. Find First and Last Position of Element in Sorted Array  
    **Redo**, **binary search**, do binary search two time, first time for start point, second time set mid = (lo+hi)//2+1 for right biased mid to find end point

35. Search Insert Position      
	**binary search**
	for better efficiency, always check if the element checked is exactly at the position we want to insert before doing next step of binary search

	or check all elements bigger than the target you want to insert, though its o(n) compare to binary search's o(log(n))

36. Valid Sudoku  
	**2d array**, **hash table**
	Count each row, column and square, use filter, and set - list compare to exclude dot, and check duplicate

	Or give every position three unique formats corresponding to row, col and square. Use a set to save and check duplicate
	- '4' in row 7 is encoded as "(4)7".
	- '4' in column 7 is encoded as "7(4)".
	- '4' in the top-right block is encoded as "0(4)2".

37. Sudoku Solver  
	**TODO**
	This question is too big, I prefer to do some review on csc384 before solving it

38. Count and Say  
	 **string**
	 write a helper function given the previous input, return the next count and say output.

39. Combination Sum  
	**dp**, **dfs**, **backtrack**
	use 1d array length equal to range(target), saved all combination sums up to the value of each index. Return the dp[-1]

	looks like there are some other ways like dfs, backtracking, will research more.

40. Combination Sum ii  
    **dp**, **dfs**, **backtrack** **TODO: Use backtrack to solve**
    Similar but different from 39, all candidates could be used once this time. Use the recursion way (dfs) to deal with it,
    Most solutions from 39 could also be applied on 40 with little modificationb

41. First Missing Positive  
    **array**， **redo**
    Tricky, **run in O(n) time and uses constant extra space**. The first missing positive must be in range[1, len(nums)+1].
    Loop through the list, if nums[index] != index + 1 (eg: nums[0] != 1), swap nums[nums[index]-1] with nums[index] until
    nums[index] is in its right place or some value not in 1 ~ len(nums) is returned.
    Then loop the list again and check the first element does not equal to index + 1.

42. Trapping Rain Water    
    **array**, **two pointer?**, **redo**
    Check from left to right and right to left, if height > previous, update highest, else: save water += highest - current height.
    Recursively do it until left and right meet together at highest height.
    
43. Multiply Strings
    **string**, **math**
    multiply algorithm implementation

44. Wildcard Matching  
    **dp**, **greedy**, **redo with other method**
    2d array -> `dp[i][j]` means if `s[:i+1]` would match `p[:j+1]`, to deal with `*` is the hardest part.
    Draw out the array and think about different cases about *
    like when it appears at beginning, when it counts as nothing, 1 char or multiple chars.

45. Jump Game II  
    **dp**, **redo with other method**
    dp with number of jumps.  
    1d array, index i maintains max position with i jump, max position = i+nums[i]  
    return i as long as i >= len(nums)-1  

46. Permutation  
    **DFS**, **recursion**, **iteraive**, **redo with other method**  
    put each element from nums in a list, then for each list append one of the rest element from nums, recursively do it
     until there is no number in the nums left, append the result to `return` 
    
47. Permutation II  
    **DFS**, **recursion**, **iteraive**  
    same idea as 46. permutation, use set() to avoid duplicate. 
    However, set does not accept list as key since it is not hashable because list is mutable.
    the idea is to change list to another immutable type and change it back when return it. 
    I choose string, but tuple should also be fine.
    
48. Rotate Image  
    **array**  
    the nature of right turn 90 degree (x,y) = (-y, x).    
    Loop through `range(n//2)` and `range(n-n//2)`, we cannot do `(n//2)` two times cuz it would miss the middle entries  
    Use `~` in python -> 2 complemnt 1 => -2 ; 10 => -11. In this way we can do:  
    ```
    A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
                         ```
49. Group Anagrams  
    **string**, **hash table**  
    create a `defaultdict(list)`, loop through list, set sorted(element in list) as dict's key, append element in dict's value.  
    Return all value in the dict
    
50. Pow(x,n)
    **recursion**, **iteration**, **bit manipulation**, **math**, **binary search**   
    Multiple ways could solve this one, here I would show recursion.  
    return 1 when n is 0.  
    when n is even, we return pow() with x = x*x and n = n//2  
    when n is odd, we return x*pow() with x unchanged, n = n -1  
    when n is negative, we return 1/pow() with x unchanged, n = -n  
    
51. TODO after review 384  
52. TODO after review 384   

53. Maximum Subarray
    **array**, **dp**  
    loop through the list  
    if the next element i > current sum + i,let i = new current sum  
    if the next element i < current sum + i, current sum = current sum + i  
    always record the current highest      
    
54. Spiral Matrix  
    **2d array**  
    Understand the pattern about the spiral turning. Two elements: Direction (turning right), steps.
    
55. Jump game
    **dp**
    Same as Q45
    
56. Merge Intervals  
    **array**  
    Sort the interval, Create return list, put `interval[0]` by default.
    Loop through the interval, if the `entry[0] <  return[-1][0]`,
     we may update `return[-1][1] = max(return[-1][1], entry[1])`.  
    Remember to use the `Interval` class.
    
Q417: 2d array, medium, unsolved
Q829: math, medium
Q830: string, easy
Q831: 2d array, medium
Q16: array, two pointers, medium, **Redo**
Q63 Unique Paths II: 2d array, dp, easy
Q64 Minimum Path Sum: 2d array, dp, easy, same as Q63
Q840 Magic Squares In Grid: 2d array, easy
Q841 Keys and Rooms: 2d array, easy
Q842 Split Array into Fibonacci Sequence: hard, TLE
Q72: DP, string, hard, **Redo**
Q87: DP, string, hard, **Redo**
Q95: DP, BST, hard, **Redo**
Q97: DP, string, medium
Q844: string, easy
Q845： string, medium, **Redo**
Q32: DP, medium, string
Q29: Maths, TLE, bit manipulation, **Redo**
Q94: Tree, recursion, easy
Q144: Tree, recursion, easy
Q145: Tree, recursion, easy
Q848: String, medium, **Redo**
Q849: Array, easy
Q851 Loud and rich: DP, array, medium
Q852 Peak Index in a Mountain Array: array, easy
Q853 Car Fleet: array, hard, **Redo**
Q854 K-Similar Strings: array, hard, dp, **Redo**
Q1 Two Sum: Array, easy
Q2 Add two numbers: Linked list, medium
Q858 Mirror Reflection: Math, hard?, **redo**
Q859 Buddy Strings: string, easy
Q856 Score of Parentheses: string, medium

872. Leaf-similar Trees  
	**Tree**, easy, Write a function to return all leaves, then compare both trees

873. Length of Longest Fibonacci Subsequence  
	**Redo**, medium, could use brute force with optimization or dp with 2d array saved data.


874. Walking Robot Simulation  
	**Redo**, easy, algorithm is easy, but need to smartly implemnet rotation and obstacle.


875. Koko Eating Bananas  
	**Redo**, medium, math?, No very smart algorithm to solve this one. Use binary search to quickly find the value of eat speed, since the search space is relatively small (1, max(piles)) it would be reasonably fast

886. Possible Bipartition  
	**Bipartite**, **graph**, **dfs**, **Redo**
	Draw a graph (each people as key, dislike relation as value), regard people as vertices, dislike relation as edges. Unable to do the partition if we could find cycle with odd edges.

887. Super Egg Drop  
	**Redo**, **DP**, 
	Saved data: 2d array, rows -> eggs; columns -> nums of moves (floors?); value -> num of trials

	Transform equaltion: superEggDrop(N,x) = 1 + max(superEggDrop(N-1, x), superEggDrop(N, K-x))


888. Uncommon Words from Two Sentences  
	String, easy, collections.counter do a lot of jobs. Combine two strings together would make the algo much more efficient

889. Spiral Matrix III  
	**Redo**  
	medium, 2d array, simulate the spiral isnt easy, efficient turn like 874

892. Surface area of 3d shapes  
    **2d array**, **geometry**  
    Count each "pillar"'s surface area, delete the area covered by previous pillar.
    
893. Groups of special-Equivalent Strings    
    **string**   
    Helper function to decide if two strings are special-equivalent, remember that in order to let two strings to be
    special equivalent, you can do **any** number of switches with both odd indices and even indices. In order words,
    if stringA odd == stringB odd and stringA even == stringB even they must be special equivalenet.
    
    Then try to split strings into group.
  
895.Maximum Frequency Stacks   
    **collections**, **stack**, **hash table**   
    The answer uses python's collections library elegantly, so that the answer overall is very concise.
    `collections.counter` is used to count elements and num of elements appeared.    
    `defaultlist(list)` is used as the "stack" with `freq[x]` (number of x appeared) as key. This part is fantastic cuz 
    it matches the requirement of pop the most frequent and closest to the top. 
    `maxf` is used to save the current max number of element appeared.  
    `push` would update `freq` by 1 and `maxf` accordingly. Then append x to m[freq[x]].  
    `pop` would find `maxf`,  pop `m[maxf]` to find the latest number, decrease `maxf` by 1 if the last number in `m[maxf]`
     is being poped  and lastly decrease `freq[maxf]` by 1.