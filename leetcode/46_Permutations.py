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


def onePermute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return [[n] + p for i,n in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:])] or [[]]

test = [1,2,3]

print(permute(test))
