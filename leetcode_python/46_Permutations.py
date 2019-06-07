
# The + operator creates a new list in python when 2 lists are combined using it, the original object is not modified.
# On the other hand, using methods like extend and append, we add the lists in place, ie, the original object is modified

def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                
                # the following commented line is wrong, return would stop code from running after it reaches it once and would not lead to recursion!!!
                # return dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
                
                dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
        res = []
        dfs(nums, [], res)
        return res

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
