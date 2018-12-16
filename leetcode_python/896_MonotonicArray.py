# Compare two elements one by one leads to O(N), or sort the list forward and backward leads to O(nlogn)

def isMonotonic(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    return A == sorted(A) or A == sorted(A)[::-1]

def betterIsMonotonic(self, A):
    return all(i >= j for i, j in zip(A, A[1:])) or all(i <= j for i, j in zip(A, A[1:]))