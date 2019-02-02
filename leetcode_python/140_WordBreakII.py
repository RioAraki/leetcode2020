# 2019-02-02: TLE

def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """

    def recur(wordDict, curS, path):
        if len(curS) == 0:
            out.append(path[1:])
        
        # loop through all wordDict, compare each word with curS's first X indexes where X = len(wordDict[i])
        for word in wordDict:
            n = len(word)
            if word == curS[:n]:
                
                recur(wordDict, curS[n:], path+" "+word)
    
    
    out = []
    recur(wordDict, s, "")
    
    return out