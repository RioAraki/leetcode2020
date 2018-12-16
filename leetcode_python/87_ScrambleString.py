# 2018-12-16: Not done by myself, need to review again and redo.
# recursivly compare all combinations of substrings and check if they are isScramble
# if string length <= 4 it is always scramble

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n,m = len(s1), len(s2)
        if n!=m or sorted(s1)!= sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        for i in range(1,n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
               self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False