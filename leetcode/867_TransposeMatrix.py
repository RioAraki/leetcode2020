class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        ret = [[0 for x in range(len(A))] for y in range(len(A[0]))]

        for i in range(len(A[0])):
            for j in range(len(A)):
                ret[i][j] = A[j][i]

        return ret