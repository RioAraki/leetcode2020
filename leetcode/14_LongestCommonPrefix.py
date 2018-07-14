class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        short = min(map(len, strs))
        ret = ""
        for i in range(short):
            for string in strs:
                if len(ret) < i+1:
                    ret += string[i]
                else:
                    if ret[i] != string[i]:
                        return ret[:i]
        return ret

    # Better solution, using enumerate and min(key)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest