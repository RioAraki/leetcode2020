# recursion

def rcombine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if k == 0:
        return [[]]

    return [pre + [i] for i in range(k, n + 1) for pre in rcombine(i - 1, k - 1)]

# iteration
def icombine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    combs = [[]]
    for x in range(k):
        # in the first loop, c is empty, so i would be in range(1, n+1)
        # in the latter loop, i would always be in range(1, c[0]-1)
        combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        print(x, combs)





def dfs(start, end, k, path, res):

    if k == 0:
        # print(path)
        res.append(path)
    else:
        for i in range(start, end+1):
            dfs(i + 1, end, k - 1, path+[i], res)


if __name__ == "__main__":
    res = []
    dfs(1,5,3,[],res)
    print(res)
