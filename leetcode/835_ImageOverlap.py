# complex: used to represent complex number. In Python, put j after number to make the number imaginary
# Imaginary number is a complex number that can be written as a real number multiplied by the imaginary unit i (i^2 =-1)

# still use brutal force with some decent tricks to decrease codes write
# In short we use complex number system to represent vectors

# My solution with brutal force， TLE

def largestOverlap(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: int
    """

    # brute force and record score

    width = len(A[0])
    height = len(A)
    high_score = 0

    # each slide could be +-(width-1), there are totally 2*(width-1)+1 (when un move)
    for dw in range(2 * width - 1):
        for dh in range(2 * height - 1):
            # if its over the size of width/height, treat as slide negatively
            dw = (width - dw) if (dw > width - 1) else dw
            dh = (height - dh) if (dh > height - 1) else dh
            score = 0
            for w in range(width):
                for h in range(height):
                    # deal with the sliding logic, if after slided the spot is out of grid, do nothing.
                    if not ((w + dw < 0) or (w + dw > width - 1)) and not ((h + dh < 0) or (h + dh > height - 1)):
                        if A[w][h] == B[(w + dw)][(h + dh)] and A[w][h] == 1:
                            score += 1
            high_score = max(score, high_score)

    return high_score


# Other people's solution
# Still use brutal force, but use several tricks
# 1. To create a 2width + 1 sized 2d array representing all possible combinations. Each row
# 2. use multiplication to represent match or mismatch
# class Solution {
# 	    public int largestOverlap(int[][] A, int[][] B) {
# 	        int n = A.length;
# 	        int[][] t = new int[2*n-1][2*n-1];
# 	        for(int i = 0;i < n;i++){
# 	        	for(int j = 0;j < n;j++){
# 	        		for(int k = 0;k < n;k++){
# 	        			for(int l = 0;l < n;l++){
# 	        				t[k-i+n][l-j+n] += A[i][j] * B[k][l];
# 	        			}
# 	        		}
# 	        	}
# 	        }
# 	        int ret = 0;
# 	        for(int[] row : t){
# 	        	for(int v : row){
# 	        		ret = Math.max(ret, v);
# 	        	}
# 	        }
# 	        return ret;
# 	    }
# 	}

def myBetterlargestOverlap(A, B):
    n = len(A)
    t_size = 2*n + 1
    t = [[0 for x in range(t_size)] for y in range(t_size)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    t[k-i+n][l-j+n] += A[i][j]*B[k][l]

    res = 0;
    for c in range(t_size):
        for r in range(t_size):
            res = max(t[c][r], res)
    return res

if __name__ == "__main__":
    A = [[1,1,0],[0,1,0],[0,1,0]]
    B = [[0,0,0],[0,1,1],[0,0,1]]
    print (myBetterlargestOverlap(A, B))
