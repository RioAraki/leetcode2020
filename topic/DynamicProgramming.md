# Dynamic Programming

## Overlapping subproblems

Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again.

In dynamic programming, computed solutions to subproblems are stored in a **table** so that these don’t have to be recomputed.  Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again. 

### Memoization (top down)
The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

### Tabulation (bottom up)
The tabulated program for a given problem builds a table in bottom up fashion and returns the last entry from table.

Both Tabulated and Memoized store the solutions of subproblems. In Memoized version, table is filled on demand while in Tabulated version, starting from the first entry, all entries are filled one by one. Unlike the Tabulated version, all entries of the lookup table are not necessarily filled in Memoized version. 

## Optimal substructure
A given problems has Optimal Substructure Property if **optimal solution of the given problem can be obtained by using optimal solutions of its subproblems**

## How to solve a DP problem

1. identify if it is a dp problem
	All dynamic programming problems satisfy the overlapping subproblems property and most of the classic dynamic problems also satisfy the optimal substructure property. 

2. decide a state expression with least parameters
	A state can be defined as **the set of parameters that can uniquely identify a certain position or standing in the given problem**. This set of parameters should be as small as possible to reduce state space.

3. formulate state relationship
	Find the relation formula to transfer between different state.

4. do tabulation or memoization
	Since we have decided the state and formulate state relationship, we just pick the most fit data structure and save state memoization data to each slot.

## Tabulation VS Memoizatation
[]()