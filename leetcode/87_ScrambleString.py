class Solution:
    def __init__(self):
        # maintain a dict to
        self.cache = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if s1 + s2 in self.cache:
            return self.cache[s1 + s2]

        N = len(s1)
        M = len(s2)

        if N != M or sorted(s1) != sorted(s2):
            self.cache[s1 + s2] = False
            return False

        # if the length is in 3, it could always be scrambled
        if N < 4:
            return True
        for i in range(1, N):
            # i is the split point, in case we dont need to swap and it is already the same
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                self.cache[s1 + s2] = True
                return True
            # in case we need to do the swap then two string becomes the same
            if self.isScramble(s1[0:i], s2[-i:]) and self.isScramble(s1[i:], s2[0:-i]):
                self.cache[s1 + s2] = True
                return True
        self.cache[s1 + s2] = False
        return False



# Not done by myself, need to review again and redo.