def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == []:
        return False
    n = len(matrix[0])
    lo, hi = 0, len(matrix) * n
    while lo < hi:
        mid = (lo + hi) // 2
        # mid // n -> row, mid % n -> col
        x = matrix[mid // n][mid % n]
        if x < target:
            lo = mid + 1
        elif x > target:
            hi = mid
        else:
            return True
    return False