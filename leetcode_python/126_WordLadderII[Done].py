# 2019-01-08: TLE

def findLadders(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    self.out = []
    dct = collections.defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            dct[word[:i]+"*"+word[i+1:]].append(word)
    
    def transfer(cur,target,used,dct,path):
        
        if cur == target:
            if path not in self.out:
                if len(self.out) == 0:
                    self.out.append(path)
                elif len(path) < len(self.out[0]):
                    self.out = [path]
                elif len(path) == len(self.out[0]):
                    self.out.append(path)
            
        used = used + [cur]
        for i in range(len(cur)):
            neigh = dct.get(cur[:i]+"*"+cur[i+1:], [])
            for nei in neigh:
                if nei not in used:
                    transfer(nei,target,used,dct,path+[nei])
                    
     
        
    transfer(beginWord, endWord,[], dct,[])
    
    
    return[[beginWord]+x for x in self.out]