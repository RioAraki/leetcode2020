import collections


def numSmallerByFrequency(queries, words):
    def funcF(string):
        tmp = collections.Counter(string)
        first = sorted(list(tmp.keys()))

        return tmp[first[0]]

    q = [funcF(x) for x in queries]
    w = [funcF(w) for w in words]
    ret = []
    for query in q:
        cnt = 0
        for word in w:
            if query < word:
                cnt += 1
        ret.append(cnt)
    return ret



if __name__ == "__main__":
    queries =["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
    words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
    print(numSmallerByFrequency(queries, words))
