def permute(nums, cur = [], ret = []):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # recursion

    ret = []


# The + operator creates a new list in python when 2 lists are combined using it, the original object is not modified.
# On the other hand, using methods like extend and append, we add the lists in place, ie, the original object is modified

    def dfs(nums, ret, path):
        print(ret)
        if not nums:
            ret.append(path)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], ret, path+[nums[i]])
    dfs(nums, ret, [])
    return ret

# dfs with oneline, use enumerate as slicer later
def oneLinePermute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return [[n] + p for i,n in enumerate(nums) for p in permute(nums[:i]+nums[i+1:])] or [[]]

# iterative solution:
def iterPermute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                print(new_perms)
        perms = new_perms
    return perms



test = [1,2,3]

print(iterPermute(test))
