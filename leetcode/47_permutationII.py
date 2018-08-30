import collections

# same idea as 46. permutation, use set() to avoid duplicate
# however, set does not accept list as key since it is not hashable because list is mutable
# the idea is to change list to another immutable type and change it back when return it
# I choose string, but tuple should also be fine

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = set()

    def dfs(nums, ret, path):
        if not nums:
            strPath = ",".join(map(lambda x: str(x), path))
            ret.add(strPath)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], ret, path + [nums[i]])

    dfs(nums, ret, [])

    return [[int(x) for x in y.split(",")] for y in ret]