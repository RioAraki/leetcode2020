import collections

# 1. get all subarrays
# 2. calculate the bitwise or result for each one

# Get TLE, the idea is not efficient enough

def subarrayBitwiseORs(A):
    """
    :type A: List[int]
    :rtype: int
    """


    bitwise = A[:]
    ret = collections.Counter(bitwise)

    # i -> length of the subarray
    for i in range(2, len(A) + 1):
        # j -> starting index of each subarray
        for j in range(len(A) - i + 1):
            bitwise[j] = bitwise[j] | A[j + i - 1]

            ret[bitwise[j]] += 1
            print(ret)

    return len(ret)

# Assume B[i][j] = A[i] | A[i+1] | ... | A[j]
# Hash set cur stores all wise B[0][i], B[1][i], B[2][i], B[i][i].

# {2} | {1} -> {1,2}  | is union
# 2 | 1 -> 3          | is bitwise or

class Solution:
    def subarrayBitwiseORs(self, A):
        res, cur = set(), set()
        for i in A:
            # union current i with all i | element in the cur
            cur = {i | j for j in cur} | {i}

            res |= cur

        return len(res)