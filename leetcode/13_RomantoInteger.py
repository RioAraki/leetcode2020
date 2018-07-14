class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {"M": 1000, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
        ret = 0

        for i, j in zip(range(0, len(s) - 1), range(1, len(s))):
            if dct[s[i]] >= dct[s[j]]:
                ret += dct[s[i]]
            else:
                ret -= dct[s[i]]
        ret += dct[s[-1]]
        return ret