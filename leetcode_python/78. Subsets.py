# dfs, use variable `idx` to pass the index, and `paths` to pass current subset.

def subsets(self, nums):
    ret = []
    self.dfs(nums, 0, [], ret)
    return ret


def dfs(self, nums, idx, paths, res):
    res.append(paths)
    for i in range(idx, len(nums)):
        self.dfs(nums, i + 1, paths + [nums[i]], res)

# iterative

def iSubsets(self, nums):
    ret = [[]]

    for i in nums:
        ret += [item + [i] for item in ret]
    return ret