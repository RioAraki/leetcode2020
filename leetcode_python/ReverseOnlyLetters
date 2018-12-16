def reverseOnlyLetters(self, S):
    """
    :type S: str
    :rtype: str
    """
    tmp = []
    nums = []
    for i in range(len(S)):
        if S[i].isalpha():
            tmp = tmp+[S[i]]
        else:
            nums.append(i)
    
    ret = ""
    for j in range(len(S)):
        if j not in nums:
            ret += tmp.pop()
        else:
            ret += S[j]
    return ret