class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        mask = ''
        # email type
        if '@' in S:
            name0 = S.lower().split('@')[0]
            name1 = S.lower().split('@')[1]
            mask = name0[0] + '*****' + name0[-1] + '@' + name1
        # phone type
        else:
            replace = ['+', '-', '(', ')', ' ']
            for s in S:
                if s in replace:
                    S = S.replace(s, '')
            # with region number
            if len(S) > 10:
                mask = '+' + '*' * (len(S) - 10) + '-***-***-' + S[-4:]
            else:
                mask = '***-***-' + S[-4:]

        return mask

    # Error 1: logic error, forgot to transfer region code
    # Error 2: logic error, forget space