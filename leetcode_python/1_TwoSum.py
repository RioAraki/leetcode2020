# 1. list is not sorted
# 2. this would cause index problem when using two pointer method which is the most efficient

# 2018-07 1152ms
# O(n^2)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                for j in range(i + 1, len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i, j]


                        # index error: range(i+1, len(nums)), not range(i, len(nums))


# 2018-12-6 52ms 
# two pointer method O(n)

def twoSum(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  
  i = 0
  j = len(nums)-1
  
  nums = [(idx,i) for idx,i in enumerate(nums)] 
  nums = sorted(nums, key = lambda x: x[1])
  
  while i < j:
    if nums[i][1] + nums[j][1] > target:
      j-= 1
    elif nums[i][1] + nums[j][1] < target:
      i+=1
    else:
      return [nums[i][0],nums[j][0]]

# hash map -> dictionary() key: list's value; value: index
def twoSum(self, nums, target):

  complement = 0
  hash_map = dict()
  for count, elem in enumerate(nums, start = 0):
    complement = target - elem
    if complement in hash_map:
      first = hasp_map.get(complement, 0) # ther might be multiple number 
      return first, count
    else:
      hash_map[elem] = count