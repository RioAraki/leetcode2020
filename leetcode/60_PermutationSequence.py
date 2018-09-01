def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    # find all permutations, sort them, find the kth one would probably tle.

    # since the int is known, can find the kth permutation directly

    fact = [0 for i in range(n)]
    fact[0] = 1
    for i in range(1, n):
        fact[i] = fact[i - 1] * (i + 1)
    print(fact)
    ret = ""
    num = [i for i in range(1, n + 1)]
    for i in range(n - 1, 0, -1):
        print(k, fact[i - 1])
        if k % fact[i - 1] == 0:
            ret += str(num.pop(k // fact[i - 1] - 1))
        else:
            ret += str(num.pop(k // fact[i - 1]))
        k %= fact[i - 1]
    ret += str(num.pop())
    return int(ret)

# better solution, use recursion and a lot of list comprehension and math
def betterGetPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    return self.helper([x + 1 for x in range(n)], n, k)

def helper(self, nums, n, k):
    if n == 1:
        return str(nums[0])
    i = (k - 1) // math.factorial(n - 1)
    return str(nums[i]) + self.helper(nums[:i] + nums[i + 1:], n - 1, (k - 1) % math.factorial(n - 1) + 1)