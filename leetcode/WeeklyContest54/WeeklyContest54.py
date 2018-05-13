# Q3： https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
	
	def canPartitionKSubsets(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		
		# if sum cannot divided by k, must be wrong
		
		quotient, remainder = divmod(sum(nums), k)
		if remainder:
			return False
		
		# recursively put num in nums to a group with sum < nums/k, if we finally put all num -> true/ otherwise false
		
		def recsearch(groups):
			if not nums: 
				return True
			v = nums.pop()
			for i, group in enumerate(groups):
				if group + v <= quotient:
					groups[i] += v
					if recsearch(groups): 
						return True
					groups[i] -= v
				if not group: 
					break
			nums.append(v)
			return False
		
		nums.sort()
		if nums[-1] > quotient: 
			return False
		while nums and nums[-1] == quotient:
			nums.pop()
			k -= 1

		return recsearch([0] * k) 