class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        ret = 1

        start = end = 0

        while end + 1 < len(s):
            while s[end + 1] in s[start:end + 1]:
                start += 1
            end += 1
            ret = max(ret, end - start + 1)
        return ret



