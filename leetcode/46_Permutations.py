def permute(nums, cur = [], ret = []):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # recursion

    ret = []


# The + operator creates a new list in python when 2 lists are combined using it, the original object is not modified.
# On the other hand, using methods like extend and append, we add the lists in place, ie, the original object is modified

    def perm(nums, ret, s):
        print(ret)
        if not nums:
            ret.append(s)
        for i in range(len(nums)):
            perm(nums[:i] + nums[i + 1:], ret, s+[nums[i]])
    perm(nums, ret, [])
    return ret

test = [1,2,3]

print(permute(test))