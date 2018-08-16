# Leetcode tag
For better categorizing

Redo all tags with **Redo** since I didn't manage to solve the issue without any help.
TODO: Add the general thoughts of solving each problem

# By topic
Linked list: 


Q1 Two Sum: two pointers, easy
Q2 Add two numbers: linked list, **Redo**, medium
3: Longest Substring Without Repeating Characters: two pointers, medium

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

18. 4Sum:
	**Redo**, same as **Q14** **Q15** **Q16** based on 3sum and 2sum. Need to do a lot of corner case check to avoid duplicate items, overloop and TLE

19. Remove Nth Node From End of List:
	**Redo**, **linked list**, should do it in one loop, use recursion to get the position of node that needs to be removed

20. Valid Parentheses:
	one-pass, same to most parentheses problems, use stack to check parentheses matches

21. Merge Two Sorted Linked Lists:
	**Redo**, **linked list**, Recursion on linked list

22. Generate Parentheses
	**Redo**, **linked list**, use recursion to generate all combinations of parentheses.

23. Merge k Sorted Linked Lists  
	**Redo**, **linked list**, use priority queue to always find the linked list with smallest value

24. Swap Nodes in Pairs:
	**Redo**, **linked list**, understand the pattern of swapping and change the "next" pointer of each node accordingly

25. Swap Nodes in k-group:
	**Redo**, **linked list**, use a counter to find every reverse group, use recursion to do the swap from last group to first group

33. Search in Rotated Sorted Array
	**Redo**, **binary search**, Set lo and hi, binary search to find the point where rotate begins. Binary search to find where target locates by comparing rotating point and middle index.

34. Find First and Last Position of Element in Sorted Array
    **Redo**, **binary search**, do binary search two time, first time for start point, second time set mid = (lo+hi)//2+1 for right biased mid to find end point

Q11: array, two pointers, easy, **Redo**, **Redone** pass
Q417: multidimensional array, medium, unsolved
Q829: math, medium
Q830: string, easy
Q831: multidimensional array, medium
Q16: array, two pointers, medium, **Redo**
Q63 Unique Paths II: multidimensional array, dynamic programming, easy
Q64 Minimum Path Sum: multidimensional array, dynamic programming, easy, same as Q63
Q840 Magic Squares In Grid: multidimensional array, easy
Q841 Keys and Rooms: Multidimensional array, easy
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
	**Redo**, medium, 2d array, simulate the spiral isnt easy, efficient turn like 874

