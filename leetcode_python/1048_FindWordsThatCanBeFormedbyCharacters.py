def countCharacters(words: List[str], chars: str) -> int:
    
    # make chars a counter
    # loop through each char from each word, if at any time it is not met, or the number of char used is more than it, it can not be formed.
    
    cntChar = collections.Counter(chars)
    charSet = set(chars)
    cnt = 0
    for word in words:
        curCnt = cntChar.copy()
        for ch in word:
            if ch in charSet:
                curCnt[ch] -= 1
                if curCnt[ch] < 0:
                    break
            else:
                break
        else:
            cnt += len(word)
    return cnt