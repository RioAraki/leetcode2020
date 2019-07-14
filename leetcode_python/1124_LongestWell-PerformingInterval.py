# O(n^2)  TLE

def longestWPI(hours):
	"""
	:type hours: List[int]
	:rtype: int
	"""
	# 2d dp

	interval = 0
	for i in hours:
	    if i > 8:
	        interval = 1
	        break
	if interval == 0:
	    return 0


	n = len(hours)
	dp = [[0 for _ in hours] for _ in hours]

	for i in range(n):
	    dp[i][i] = 1 if hours[i] > 8 else -1
	    
	for i in range(n):
	    for j in range(i):
	        dp[j][i] = dp[j][i-1] + 1 if hours[i] > 8 else dp[j][i-1] - 1
	        if dp[j][i] > 0:
	            interval = max(interval, abs(j-i)+1)

	return interval

