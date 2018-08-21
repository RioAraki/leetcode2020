# compare the counter dict of word in words, pattern, and word+pattern.

from collections import Counter

def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    ret = []
    # try to replace char
    pcount = Counter(list(pattern))
    plist = [x[1] for x in pcount.items()]

    for word in words:
        wordc = Counter(list(word))
        wcount = Counter([x + y for x, y in zip(list(pattern), list(word))])
        if sorted(plist) == sorted([x[1] for x in wordc.items()]) == sorted([x[1] for x in wcount.items()]):
            ret.append(word)
    return ret


if __name__ == "__main__":
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(findAndReplacePattern(words, pattern))