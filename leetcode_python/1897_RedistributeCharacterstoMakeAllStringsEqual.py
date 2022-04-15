import collections

def makeEqual(words: List[str]) -> bool:
    # num of each char should divisible by size of words
    size = len(words)
    cnt = collections.Counter()
    for word in words:
        for char in word:
            cnt[char] += 1
    
    for char in cnt:
        # if current total char count divide by size of word has remainder:
        if cnt[char] % size:
            return False
    return True