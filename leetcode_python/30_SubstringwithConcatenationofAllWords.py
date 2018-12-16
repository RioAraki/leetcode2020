# example 2 in prob description is wrong

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        n = len(words[0])
        i = 0
        ret = []
        while i < len(s)-len(words)*n+1: # optimization, avoid meaningless check if remaining i is not enough for all word in words
            tmp = words[:] # python copy model, tmp = words copy by reference, tmp = words[:] copy by value
            start = i
            while start+n <= len(s) and s[start:start+n] in tmp: # <= rather than < because last index in [_:last] could be len(s)
                tmp.remove(s[start:start+n])
                start += n
            if len(tmp) == 0:
                ret.append(i)
            i+=1
        return ret


