class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        if needle not in haystack: return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i