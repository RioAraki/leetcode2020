# collections is an easy way to check amounts of char appeared in string which is best fit in this question
# check all power of 2's chars and find if any matches N

import collections

class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(32))

# Not my own work