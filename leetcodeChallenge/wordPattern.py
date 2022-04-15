def wordPattern(self, pattern: str, string: str) -> bool:
        
    wordList = string.split(" ")
    patternList = [ch for ch in pattern]
    dct = collections.defaultdict(set)
    if len(wordList) != len(patternList):
        return False
    for i in range(len(wordList)):
        dct[patternList[i]].add(wordList[i])
        if len(dct[patternList[i]]) > 1:
            return False
    # print ([next(iter(item[1])) for item in dct.items()])
    # print ([key for key in dct.keys()])
    if len(set([next(iter(item[1])) for item in dct.items()])) != len([key for key in dct.keys()]): return False
    return True