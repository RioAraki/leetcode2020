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