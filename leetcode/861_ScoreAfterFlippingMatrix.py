# We have a two dimensional matrix A where each value is 0 or 1.
#
# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
#
# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
#
# Return the highest possible score.
#
#
#
# Example 1:
#
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
# Note:
#
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # check every column if sum value before toggle > sum value after toggle
        # check every row if sum value before toggle > after toggle
        sum = 0

        for i in range(len(A)):
            scoreBefore = scoreAfter = 0
            count = 0
            for ele in A[i][::-1]:
                scoreBefore += ele * (2 ** count)
                scoreAfter += (not (ele | 0)) * (2 ** count)
                count += 1
            if scoreAfter > scoreBefore:
                A[i] = list(map(lambda x: not (x | 0), A[i]))

        for i in range(len(A[0])):
            scoreBefore = scoreAfter = 0
            for j in range(len(A)):
                scoreBefore += A[j][i]
                scoreAfter += (not (A[j][i] | 0))
            if scoreAfter > scoreBefore:
                for j in range(len(A)):
                    A[j][i] = not (A[j][i] | 0)

        for i in range(len(A)):
            count = 0
            for j in A[i][::-1]:
                sum += j * (2 ** count)
                count += 1

        return sum

# better solution

def matrixScore(self, A):
    M, N = len(A), len(A[0])
    # the binary score for all largest indices as 1
    # First (largest) index must be 1 or it would be flipped.
    res = (1 << N - 1) * M

    # In each column
    for i in range(1, N):
        # A[j][i] == A[j][0], we use this step to find all indices same as the first one, which would be toggled with the first index.
        cur = sum(A[j][i] == A[j][0] for j in range(M))
        res += max(cur, M - cur) * (1 << N - 1 - i)
    return res