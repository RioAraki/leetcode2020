class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False

        pair = []
        counter = 0
        same = 0
        for i in range(len(A)):
            if same == 0 and A[i] in A[:i] + A[i + 1:]:
                same = 1
            if counter >= 3:
                return False
            if A[i] != B[i]:
                counter += 1
                pair.append((A[i], B[i]))

        if counter == 0 and same == 1:
            return True
        if counter == 2:
            if pair[0][0] == pair[1][1] and pair[0][1] == pair[1][0]:
                return True
        return False

        # Error 1: Corner case: if both strings are the same with two same chars they are buddy string