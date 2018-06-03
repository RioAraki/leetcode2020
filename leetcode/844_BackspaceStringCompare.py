class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ret1 = ''
        ret2 = ''
        for char in S:
            if char != '#':
                ret1 += char
            else:
                if len(ret1) > 0:
                    ret1 = ret1[:-1]

        for char in T:
            if char != '#':
                ret2 += char
            else:
                if len(ret2) > 0:
                    ret2 = ret2[:-1]

        return ret1 == ret2