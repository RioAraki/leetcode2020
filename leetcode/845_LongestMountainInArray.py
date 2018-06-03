class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A == []:
            return 0

        dp1 = [0 for x in range(len(A))]
        dp2 = [0 for x in range(len(A))]
        dp1[0], dp2[0] = 1, 1
        revA = A[::-1]

        for i in range(1, len(A)):
            maxval1 = 0
            maxval2 = 0

            for j in range(i):
                if A[i] > A[j]:
                    maxval1 = max(maxval1, dp1[j])
                if revA[i] > revA[j]:
                    maxval2 = max(maxval2, dp2[j])

            dp1[i] = maxval1 + 1
            dp2[i] = maxval2 + 1

        if max(dp1) == 1 or max(dp1) == len(A):
            return 0

        return max(dp1[i] + dp2[i] for i in range(len(A))) - 1

    # Error 1: corner case:  case []
    # Error 2: corner case: forget to consider the case which all nums in list are increasing/ decreasing
    # Error 3: TLE
    # Error 4: misunderstanding: the mountain must be connected!

# Better solution
class Solution:
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i-1] < A[i] or A[i-1] == A[i]:
                up = down = 0
            up += A[i-1] < A[i]
            down += A[i-1] > A[i]
            if up and down:
                res = max(res, up+down+1)
        return res 