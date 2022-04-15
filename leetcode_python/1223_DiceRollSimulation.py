# dp question
# dp[i][j][k] i -> the ith turn ; j,k -> end with j continuous number of k
# eg: dp[5][3][4] : now in 5th turn, there are 3 continuous numbers end with 4

def dieSimulator(n, rollMax):
	# rollmax is 15

	# i -> in the range of n, j -> in the range of 0-15 as ther could only be 15max, k -> in the range of 6, 6 faces die
	dp = [[[0]*6 for _ in range(16)] for _ in range(n)]

	# initialization of the first rolling
	for k in range(6):
		dp[0][1][k] = 1

	for i in range(1,n):
		# this turn of rolling ending with k
		for k in range(6):
			# last turn of rolling ending with prev
			# we want to see if this turn's number k is the same as last turn's number prev
			for prev in range(6):
				# for last turn ending with continous j number of prev
				for j in range(1,min(rollMax[prev],i+1)+1):
          if prev == k:
              dp[i][j][k]+=dp[i-1][j-1][k]
              dp[i][j][k]%=mod
          else:
              dp[i][1][k]+=dp[i-1][j][prev]
              dp[i][1][k]%=mod

  return sum(dp[n-1][j][k] for k in range(6) for j in range(1,min(n,rollMax[k])+1))%mod
