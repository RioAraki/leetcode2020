class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        dct = collections.defaultdict(list)
        stack = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack += 1
            
            elif s[i] == ")":
                dct[stack-1] += dct[stack][::-1]
                dct[stack] = []
                stack -= 1
            
            else:
                dct[stack].append(s[i])
        
        return "".join(dct[0])
            