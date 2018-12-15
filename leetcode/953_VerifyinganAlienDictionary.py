# pass 2018-12-08
# similar idea as the standard solution

# The words are sorted lexicographically if and only if adjacent words are. 

def isAlienSorted(self, words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    # check each connected pairs see if they are sorted

    
    dct = collections.defaultdict(int)
    for i in range(len(order)):
        dct[order[i]] = i 
    
    base = -1
    for i in range(len(words)):
        if dct[words[i][0]] > base:
            base = dct[words[i][0]]
        elif dct[words[i][0]] < base:
            return False
        else:
            tmp = 1
            while (1):
                if len(words[i-1]) > tmp and len(words[i]) > tmp:
                    if  dct[words[i-1][tmp]] < dct[words[i][tmp]]:
                        break
                    elif dct[words[i-1][tmp]] > dct[words[i][tmp]]:
                        return False
                    else:
                        tmp += 1
                elif len(words[i]) <= tmp and len(words[i-1]) > tmp:
                    return False
                else:
                    break # this tuple are sorted
    return True


# better 2018-12-08