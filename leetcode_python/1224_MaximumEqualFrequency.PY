# Three situations
# 1. all elements appear once
# 2. all elements except 1 appear k times, one element appears k+1 times
# 3. all elements except 1 appear k times, one element appears once

def maxEqualFreq(nums):
	cnt = collections.defaultdict(int)
	freq = collections.defaultdict(int)
	maxF = 0
	res = 0

	for i, num in enumerate(nums):
		cnt[num] += 1
		# freqency only records how many times number with certain frequency appeared. It does not care which number has that freq
		freq[cnt[num]-1] -= 1
		freq[cnt[num]] += 1
		# 
		maxF = max(maxF, cnt[num])

		# case 1: in each loop there are actually i+1 items, if the max frequency * times of number with max frequency = i, it matches 3
		# case 2: if maxF is 1, matches 1
		# case 3: there are freq[maxF-1] items appears maxF-1 times, once appears maxF times, so add them all together would be i+1
		if maxF * freq[maxF] == i or maxF == 1 or (maxF - 1) * (freq[maxF - 1]) + maxF == i+1:
			res = i + 1
		return res