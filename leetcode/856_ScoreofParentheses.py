class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        val = [0 for x in range(len(S))]
        match = [0 for x in range(len(S))]

        for i in range(len(S)):
            if S[i] == ')':
                if S[i - 1] == '(':
                    match[i] = match[i - 1] = 1
                    val[i] = val[i - 2] + 1
                else:
                    j = i - 1
                    while match[j] != 0:
                        j -= 1
                    val[i] = val[j - 1] + 2 * val[i - 1]
                    match[i] = match[j] = 1
        return val[-1]