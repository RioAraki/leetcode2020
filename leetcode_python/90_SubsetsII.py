# 2018-12-22 Not my original idea, needs to redo

# logic: loop through the list, in each iteration, add the new element to all things already in the output list, update the "effect region" if current num from the list is the same as the previous one

def subsetWithDup(nums):
	res = [[]]

	for i in range(len(nums)):

		if i == 0 or nums[i] == nums[i-1]:
			cur_res_len = len(res)

		for j in range(len(nums) - cur_res_len, len(nums)):
			res.append(res[j] + [nums[i]])

		return res

		