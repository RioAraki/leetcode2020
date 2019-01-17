# Interview preparation 
My preparation for technical interview

## Algorithms


### CLRS reading notes
[Notes](https://github.com/RioAraki/Interview_prep/blob/master/CLRS/clrs.md)


### Leetcode 

Goal:

- Solve the first 150 questions
- Solve questions with different difficulties based on different topics
- Solve latest released questions routinely

Language:

- Python: easiest, fastest,
- C++: more useful since A lot of jobs I pursue requires C++ skills


[Topics](https://github.com/RioAraki/Interview_prep/blob/master/topic/topics.md)

A lot of solutions are a mix of multiple topics, one question could also have different solutions based on different methods. The following lists are based on my own solution and experience.

- Sorting / search
  - Heap sort  
  - Quick sort  
  - Binary search  

  - Two pointer  
    - 1 - Two Sum  

- Hash tables  
    - 2 - Add Two Numbers  

- Linked list  
  Leetcode provides specific API for linked list data structure, so you do not need to implement a linked list even though it is good to do so. Most linked list refers to singly linked list

  Common trick: use a fast pointer and a slow pointer to get the middle point of linked list
  ```
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  ```

    - 2 - Add Two Numbers
    - 109 - Convert Sorted List to Binary Search Tree
- Stack and Queue

- Tree
  - Tree traverse
  - BST (binary search tree)

  binary search tree  
  Implement an BST:  
    Supported operations:  
    - insertion
    - deletion
    **TODO**

  Questions:
    - 111 - Minimum Depth of Binary Tree


  - AVL tree  

  AVL tree is a **self-balancing Binary Search Tree (BST)** where the **difference between heights of left and right subtrees cannot be more than one for all nodes**.
  
  Its **insertion** and **deletion** operations are the most interesting ones. 

  Implement an AVL tree:
    Supported operations:
    - left rotate / right rotate
    - check if balanced
    - insertion
    - deletion

    **TODO**

  Questions:
    - 108 - Convert Sorted Array to Binary Search Tree
    - 109 - Convert Sorted List to Binary Search Tree (good for understand property and operations of AVL tree like insertion)
    - 110 - Balanced Binary Tree (implementation of check balanced operations)
  - B trees
  - Heaps

- Recursion

- Greedy

- Divide and conquer 

- Dynamic programming 



   
- Graph  
  A lot of methods from graph theory like BFS and DFS can be applied widely in various questions. 

  - BFS (breath first search)
  - DFS (depth first search)
  - MST (Medium spanning tree)
  - Disjoint sets

- Network flow
  - Single source shortest paths
  - All-pairs shortest paths
  - Maximum flow
  
- Linear programming

- Maths
  - Geometry
  - Bit manipulation

Related questions:

1 - two sums  
15 - 3Sum  
16 - 3Sum Closest  
18 - 4Sum  

12 - Integer to Roman  
13 - Roman to integer

121 - Best Time to Buy and Sell Stock  
122 - Best Time to Buy and Sell Stock II    
123 - Best Time to Buy and Sell Stock III    


### Trivial

28 - implement Strstr(): KMP algorithm O(m+n)

## Language


### Python  
Basic




### C++


