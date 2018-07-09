class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def isPrime(x):
            # only 2 is prime, other even are not
            if x < 2 or x % 2 == 0: return x == 2
            # check all possible factors, no need to check even factor, no need to check factors > sqrt(x)
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0: return False
            return True

        if 8 <= N <= 11: return 11
        # check len(str(N)/2) make sure we start from a number smaller than N but not too small (in a range we not missing y >= N and is a palindrome)
        for x in range(10 ** (len(str(N)) // 2), 10 ** 5):
            # make it a palindrome, by this way we not missing any palindrome
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y): return y
