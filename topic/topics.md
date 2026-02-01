# LeetCode Topics & Solutions

A comprehensive guide to data structures, algorithms, and the problems I've solved.

---

## Table of Contents
- [Array & Two Pointers](#array--two-pointers)
- [Sorting & Searching](#sorting--searching)
- [Data Structures](#data-structures)
- [Dynamic Programming](#dynamic-programming)
- [Greedy](#greedy)
- [Graph Algorithms](#graph-algorithms)
- [Math & Bit Manipulation](#math--bit-manipulation)
- [String](#string)
- [Backtracking & Recursion](#backtracking--recursion)

---

## Array & Two Pointers

### Techniques
- Brute force enumeration
- Two pointer (sliding window, fast/slow pointers)
- Prefix sum / Difference array

### Solved Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | Two Sum | Easy | Hash map O(n), Two pointers O(n log n) |
| 11 | Container With Most Water | Medium | Two pointers |
| 15 | 3Sum | Medium | Sort + Two pointers |
| 16 | 3Sum Closest | Medium | Two pointers |
| 18 | 4Sum | Medium | Extend from 3Sum |
| 26 | Remove Duplicates from Sorted Array | Easy | Two pointers |
| 42 | Trapping Rain Water | Hard | Two pointers / Stack |
| 54 | Spiral Matrix | Medium | Simulation |
| 56 | Merge Intervals | Medium | Sort + merge |
| 57 | Insert Interval | Medium | Merge intervals |
| 59 | Spiral Matrix II | Medium | Simulation |
| 66 | Plus One | Easy | Carry bit |
| 73 | Set Matrix Zeroes | Medium | In-place marking |
| 80 | Remove Duplicates from Sorted Array II | Medium | Two pointers |
| 88 | Merge Sorted Array | Easy | Two pointers from end |
| 121 | Best Time to Buy and Sell Stock | Easy | Track min price |
| 122 | Best Time to Buy and Sell Stock II | Easy | Greedy |
| 238 | Product of Array Except Self | Medium | Prefix/suffix products |
| 283 | Move Zeroes | Easy | Two pointers |
| 334 | Increasing Triplet Subsequence | Medium | Track min values |
| 443 | String Compression | Medium | Two pointers |
| 605 | Can Place Flowers | Easy | Greedy check |
| 849 | Maximize Distance to Closest Person | Easy | |
| 881 | Boats to Save People | Medium | Two pointers |
| 896 | Monotonic Array | Easy | |
| 945 | Minimum Increment to Make Array Unique | Medium | |
| 977 | Squares of a Sorted Array | Easy | Two pointers |

**Location:** `leetcode_python/`, `leetcode75/`

---

## Sorting & Searching

### Sorting Algorithms
See detailed implementations in [`topic/sort/`](sort/)

| Algorithm | Time Complexity | Space | Stable | Implementation |
|-----------|----------------|-------|--------|----------------|
| Bubble Sort | O(n²) | O(1) | Yes | [BubbleSort.py](sort/BubbleSort.py) |
| Selection Sort | O(n²) | O(1) | No | [SelectionSort.py](sort/SelectionSort.py) |
| Insertion Sort | O(n²) | O(1) | Yes | [InsertionSort.py](sort/InsertionSort.py) |
| Merge Sort | O(n log n) | O(n) | Yes | [MergeSort.py](sort/MergeSort.py) |
| Quick Sort | O(n log n) avg | O(log n) | No | [QuickSort.py](sort/QuickSort.py) |
| Heap Sort | O(n log n) | O(1) | No | [HeapSort.py](sort/HeapSort.py) |
| Counting Sort | O(n + k) | O(k) | Yes | [CountingSort.py](sort/CountingSort.py) |
| Bucket Sort | O(n + k) | O(n) | Yes | [BucketSort.py](sort/BucketSort.py) |

### Search Algorithms
- **Linear Search:** O(n)
- **Binary Search:** O(log n) - requires sorted array
- **Hash-based Search:** O(1) average

### Binary Search Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 33 | Search in Rotated Sorted Array | Medium | Modified binary search |
| 34 | Find First and Last Position | Medium | Left/right biased binary search |
| 35 | Search Insert Position | Easy | Standard binary search |
| 74 | Search a 2D Matrix | Medium | Treat as 1D array |
| 75 | Sort Colors | Medium | Dutch flag / Counting sort |
| 875 | Koko Eating Bananas | Medium | Binary search on answer |

---

## Data Structures

### Hash Tables
See: [hashtable.md](hashtable.md)

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | Two Sum | Easy | Classic hash map usage |
| 36 | Valid Sudoku | Medium | Hash set for validation |
| 49 | Group Anagrams | Medium | Sorted string as key |
| 76 | Minimum Window Substring | Hard | Sliding window + hash |
| 128 | Longest Consecutive Sequence | Medium | Hash set |
| 895 | Maximum Frequency Stack | Hard | FreqStack with hash maps |

### Linked List

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 2 | Add Two Numbers | Medium | Simulate addition |
| 19 | Remove Nth Node From End | Medium | Two pointers |
| 21 | Merge Two Sorted Lists | Easy | Recursion/iteration |
| 23 | Merge k Sorted Lists | Hard | Priority queue / Divide & conquer |
| 24 | Swap Nodes in Pairs | Medium | |
| 25 | Reverse Nodes in k-Group | Hard | |
| 61 | Rotate List | Medium | Two pointers |
| 82 | Remove Duplicates from Sorted List II | Medium | |
| 83 | Remove Duplicates from Sorted List | Easy | |
| 86 | Partition List | Medium | |
| 92 | Reverse Linked List II | Medium | |
| 109 | Convert Sorted List to BST | Medium | |
| 114 | Flatten Binary Tree to Linked List | Medium | |
| 148 | Sort List | Medium | Merge sort on linked list |
| 876 | Middle of the Linked List | Easy | Fast/slow pointers |
| 1019 | Next Greater Node In Linked List | Medium | Stack |
| 1171 | Remove Zero Sum Consecutive Nodes | Medium | Prefix sum |

### Stack & Queue

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 20 | Valid Parentheses | Easy | Stack matching |
| 32 | Longest Valid Parentheses | Hard | Stack / DP |
| 71 | Simplify Path | Medium | Stack for path |
| 84 | Largest Rectangle in Histogram | Hard | Monotonic stack |
| 155 | Min Stack | Easy | Auxiliary stack |
| 856 | Score of Parentheses | Medium | Stack |
| 895 | Maximum Frequency Stack | Hard | Multiple stacks |
| 1172 | Dinner Plate Stacks | Hard | |

### Trees

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 94 | Binary Tree Inorder Traversal | Easy | Recursion/iteration |
| 95 | Unique Binary Search Trees II | Medium | DP + recursion |
| 96 | Unique Binary Search Trees | Medium | Catalan numbers |
| 98 | Validate Binary Search Tree | Medium | In-order traversal |
| 99 | Recover Binary Search Tree | Hard | |
| 100 | Same Tree | Easy | Recursion |
| 101 | Symmetric Tree | Easy | Recursion |
| 102 | Binary Tree Level Order Traversal | Medium | BFS |
| 103 | Binary Tree Zigzag Level Order | Medium | BFS + reverse |
| 104 | Maximum Depth of Binary Tree | Easy | DFS/BFS |
| 105 | Construct Binary Tree from Preorder and Inorder | Medium | Recursion |
| 106 | Construct Binary Tree from Inorder and Postorder | Medium | Recursion |
| 107 | Binary Tree Level Order Traversal II | Medium | BFS |
| 108 | Convert Sorted Array to BST | Easy | Recursion |
| 109 | Convert Sorted List to BST | Medium | |
| 110 | Balanced Binary Tree | Easy | DFS |
| 111 | Minimum Depth of Binary Tree | Easy | BFS/DFS |
| 112 | Path Sum | Easy | DFS |
| 113 | Path Sum II | Medium | DFS + backtrack |
| 114 | Flatten Binary Tree to Linked List | Medium | |
| 116 | Populating Next Right Pointers | Medium | Level-order |
| 117 | Populating Next Right Pointers II | Medium | |
| 124 | Binary Tree Maximum Path Sum | Hard | DFS |
| 129 | Sum Root to Leaf Numbers | Medium | DFS |
| 144 | Binary Tree Preorder Traversal | Easy | |
| 145 | Binary Tree Postorder Traversal | Easy | |
| 834 | Sum of Distances in Tree | Hard | DFS + DP |
| 863 | All Nodes Distance K in Binary Tree | Medium | BFS |
| 865 | Smallest Subtree with Deepest Nodes | Medium | |
| 872 | Leaf-Similar Trees | Easy | DFS |
| 889 | Construct Binary Tree from Preorder and Postorder | Medium | |
| 894 | All Possible Full Binary Trees | Medium | |
| 897 | Increasing Order Search Tree | Easy | In-order |
| 958 | Check Completeness of Binary Tree | Medium | BFS |
| 1022 | Sum of Root To Leaf Binary Numbers | Easy | |
| 1026 | Maximum Difference Between Node and Ancestor | Medium | |
| 1104 | Path In Zigzag Labelled Binary Tree | Medium | |
| 1110 | Delete Nodes And Return Forest | Medium | |
| 1123 | Lowest Common Ancestor of Deepest Leaves | Medium | |
| 1145 | Binary Tree Coloring Game | Medium | |

### Heaps & Priority Queues

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 23 | Merge k Sorted Lists | Hard | Min heap |
| 857 | Minimum Cost to Hire K Workers | Hard | |
| 871 | Minimum Number of Refueling Stops | Hard | Max heap |

---

## Dynamic Programming

See detailed explanation: [DynamicProgramming.md](DynamicProgramming.md)

### Key Concepts
1. **Overlapping Subproblems** - Same subproblems solved repeatedly
2. **Optimal Substructure** - Optimal solution from optimal subproblems
3. **Memoization (Top-down)** - Recursion + cache
4. **Tabulation (Bottom-up)** - Iterative + table

### Classic DP Problems
See implementations in [`DP_classic/`](../DP_classic/)
- 0-1 Knapsack Problem
- Longest Common Subsequence
- Longest Common Substring

### DP Problems by Pattern

#### 1D DP

| # | Problem | Difficulty | State Definition |
|---|---------|------------|------------------|
| 53 | Maximum Subarray | Easy | `dp[i]` = max sum ending at i |
| 55 | Jump Game | Medium | `dp[i]` = can reach i |
| 70 | Climbing Stairs | Easy | `dp[i]` = ways to reach step i |
| 91 | Decode Ways | Medium | `dp[i]` = ways to decode s[:i] |
| 121 | Best Time to Buy and Sell Stock | Easy | Track min price |
| 123 | Best Time to Buy and Sell Stock III | Hard | State machine |
| 198 | House Robber | Medium | `dp[i]` = max rob up to house i |
| 213 | House Robber II | Medium | Circular array |
| 1137 | N-th Tribonacci Number | Easy | Linear recurrence |

#### 2D DP

| # | Problem | Difficulty | State Definition |
|---|---------|------------|------------------|
| 5 | Longest Palindromic Substring | Medium | `dp[i][j]` = is s[i:j+1] palindrome |
| 10 | Regular Expression Matching | Hard | `dp[i][j]` = s[:i] matches p[:j] |
| 44 | Wildcard Matching | Hard | Pattern matching |
| 62 | Unique Paths | Medium | `dp[i][j]` = paths to (i,j) |
| 63 | Unique Paths II | Medium | With obstacles |
| 64 | Minimum Path Sum | Medium | `dp[i][j]` = min sum to (i,j) |
| 72 | Edit Distance | Hard | `dp[i][j]` = edit distance |
| 87 | Scramble String | Hard | 3D DP |
| 97 | Interleaving String | Medium | |
| 115 | Distinct Subsequences | Hard | |
| 879 | Profitable Schemes | Hard | |
| 887 | Super Egg Drop | Hard | Classic DP |

---

## Greedy

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 45 | Jump Game II | Medium | Greedy jumps |
| 55 | Jump Game | Medium | Track max reach |
| 122 | Best Time to Buy and Sell Stock II | Easy | Collect all profits |
| 605 | Can Place Flowers | Easy | Greedy placement |
| 860 | Lemonade Change | Easy | Greedy change |
| 861 | Score After Flipping Matrix | Medium | |
| 870 | Advantage Shuffle | Medium | Greedy matching |

---

## Graph Algorithms

### Techniques
- **DFS** (Depth-First Search)
- **BFS** (Breadth-First Search)
- **Topological Sort**
- **Union Find / Disjoint Sets**
- **MST** (Minimum Spanning Tree)

### Graph Problems

| # | Problem | Difficulty | Technique |
|---|---------|------------|-----------|
| 126 | Word Ladder II | Hard | BFS + backtrack |
| 127 | Word Ladder | Hard | BFS |
| 133 | Clone Graph | Medium | DFS/BFS |
| 802 | Find Eventual Safe States | Medium | DFS |
| 841 | Keys and Rooms | Medium | DFS/BFS |
| 851 | Loud and Rich | Medium | DFS |
| 886 | Possible Bipartition | Medium | Bipartite check |
| 934 | Shortest Bridge | Medium | BFS |
| 1091 | Shortest Path in Binary Matrix | Medium | BFS |

### Network Flow / Shortest Paths
- Single source shortest paths (Dijkstra, Bellman-Ford)
- All-pairs shortest paths (Floyd-Warshall)
- Maximum flow (Ford-Fulkerson)

---

## Math & Bit Manipulation

### Math Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 7 | Reverse Integer | Easy | Overflow check |
| 9 | Palindrome Number | Easy | |
| 12 | Integer to Roman | Medium | |
| 13 | Roman to Integer | Easy | |
| 29 | Divide Two Integers | Medium | Bit manipulation |
| 43 | Multiply Strings | Medium | String multiplication |
| 50 | Pow(x, n) | Medium | Binary exponentiation |
| 66 | Plus One | Easy | |
| 67 | Add Binary | Easy | |
| 69 | Sqrt(x) | Easy | Newton's method / Binary search |
| 829 | Consecutive Numbers Sum | Hard | |
| 858 | Mirror Reflection | Medium | |
| 866 | Prime Palindrome | Medium | |
| 878 | Nth Magical Number | Hard | |

### Bit Manipulation

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 89 | Gray Code | Medium | |
| 868 | Binary Gap | Easy | |
| 898 | Bitwise ORs of Subarrays | Medium | |
| 1017 | Convert to Base -2 | Medium | |

### Geometry

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 835 | Image Overlap | Medium | |
| 850 | Rectangle Area II | Hard | |
| 883 | Projection Area of 3D Shapes | Easy | |
| 892 | Surface Area of 3D Shapes | Easy | |

---

## String

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding window |
| 5 | Longest Palindromic Substring | Medium | DP / Expand |
| 8 | String to Integer (atoi) | Medium | |
| 14 | Longest Common Prefix | Easy | |
| 17 | Letter Combinations of Phone Number | Medium | Backtrack |
| 22 | Generate Parentheses | Medium | Backtrack |
| 38 | Count and Say | Medium | |
| 49 | Group Anagrams | Medium | Hash |
| 58 | Length of Last Word | Easy | |
| 65 | Valid Number | Hard | FSM |
| 68 | Text Justification | Hard | |
| 71 | Simplify Path | Medium | Stack |
| 125 | Valid Palindrome | Easy | Two pointers |
| 151 | Reverse Words in a String | Medium | |
| 345 | Reverse Vowels of a String | Easy | Two pointers |
| 443 | String Compression | Medium | |
| 830 | Positions of Large Groups | Easy | |
| 831 | Masking Personal Information | Medium | |
| 833 | Find And Replace in String | Medium | |
| 844 | Backspace String Compare | Easy | Stack / Two pointers |
| 848 | Shifting Letters | Medium | |
| 859 | Buddy Strings | Easy | |
| 884 | Uncommon Words from Two Sentences | Easy | Counter |
| 893 | Groups of Special-Equivalent Strings | Medium | |
| 953 | Verifying an Alien Dictionary | Easy | |
| 1071 | Greatest Common Divisor of Strings | Easy | |
| 1221 | Split a String in Balanced Strings | Easy | |

---

## Backtracking & Recursion

### Combination & Permutation Problems

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 17 | Letter Combinations of Phone Number | Medium | |
| 22 | Generate Parentheses | Medium | |
| 31 | Next Permutation | Medium | |
| 39 | Combination Sum | Medium | Can reuse elements |
| 40 | Combination Sum II | Medium | Each element once |
| 46 | Permutations | Medium | DFS |
| 47 | Permutations II | Medium | Handle duplicates |
| 60 | Permutation Sequence | Hard | Math |
| 77 | Combinations | Medium | |
| 78 | Subsets | Medium | |
| 90 | Subsets II | Medium | Handle duplicates |
| 93 | Restore IP Addresses | Medium | |

---

## Statistics

### By Language
| Language | Count | Location |
|----------|-------|----------|
| Python | ~280+ | `leetcode_python/`, `leetcode75/`, `leetcodeChallenge/`, `DP_classic/` |
| Java | 3+ | `leetcode_java/`, `leetcodeChallenge/` |
| C# | 2 | `leetcode_c#/` |

### Problems Marked for Review
Problems with `[REDO]` or `[Re]` tags need revisiting:
- 99 - Recover Binary Search Tree
- 100 - Same Tree
- 109 - Convert Sorted List to BST
- 127 - Word Ladder
- 958 - Check Completeness of Binary Tree
- 959 - Regions Cut By Slashes

---

## Resources

- [LeetCode Problem Tags](LeetcodeTag.md) - Detailed notes on individual problems
- [Dynamic Programming Guide](DynamicProgramming.md) - DP concepts and methodology
- [Sorting Algorithms](sort/Sort%20summary.md) - Sort implementations and comparisons
- [Lessons Learnt](LessonLearnt.md) - Python tips and debugging notes

---

*Last updated: February 2026*
