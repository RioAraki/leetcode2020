class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        ret = []
        beg = 0
        cur = S[0]

        for i in range(len(S)):
            if cur != S[i]:
                if i - beg >= 3:  # error 1: variable misuse, misuse of cur, should be beg
                    ret.append([beg, i - 1])
                cur = S[i]
                beg = i

        # error2: logic error, forget to check tail
        # error3: index error, forget to use len - 1 to represent last one in list
        if (len(S) - 1) - beg >= 2:
            ret.append([beg, len(S) - 1])

        return ret