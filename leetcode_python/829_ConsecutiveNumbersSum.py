import math


class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N == 1:
            return 1

        if N == 2:
            return 1

        out = 0
        for i in range(1, int(math.sqrt(2 * N)) + 1):
            if i % 2 == 0 and N % i == i / 2 and (N / i - i / 2) > 0:
                out += 1
            elif i % 2 == 1 and N % i == 0 and (N / i - (i - 1) / 2) > 0:
                out += 1
        return out

    # Error 1: logic error,  of range function, range(x,y) contains x does not contain y