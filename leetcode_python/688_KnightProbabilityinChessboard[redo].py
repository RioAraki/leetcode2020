# TLE
# 只用了 2d dp，但过程中依然有很多重复部分，可以用三维dp，格式为 {(x,y,turn): probability}


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        
        # eg: {(2,3):[(1,2), (2,3)]} means 2 out of 8 possible moves which are (1,2) and (2,3) from point (2,3) are in the board
        self.score = 0
        def recur(dp, N, K, cur, prob):
            if K == 0:
                self.score += prob
            
            else:
                # get all coordinates possible for the next move
                if cur not in dp:
                    nxt = self.helper(N, cur)
                    dp[cur] = nxt
                else:
                    nxt = dp[cur]

                for i in nxt:
                    recur(dp, N, K-1, i, prob/8)
            
        dp = dict()
        cur = (c,r)
        prob = 1
        
        recur(dp, N, K ,cur, prob)
        return self.score
            

    def helper(self, N, coor):
        moveSet =[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        res = []
        for move in moveSet:
            cur = (coor[0] + move[0], coor[1] + move[1])
            if not (cur[0] < 0 or cur[0] > N-1 or cur[1] < 0 or cur[1] > N-1):
                res.append(cur)
        return res


# 3d dp
def is_valid(r,c,N):
    return 0<=r<N and 0<=c<N

def next_pos(r,c):
    return [ (r+2,c+1),(r+2,c-1),(r-2,c+1),(r-2,c-1),(r+1,c-2),(r+1,c+2),(r-1,c-2),(r-1,c+2) ]    


class Solution:
    def solve(self, N, K, r, c):
        pos = next_pos(r,c)
        prob = 0
        for p in pos:
            if not is_valid(p[0], p[1], N):
                continue
                
            # final round (base case), since it is valid it would have prob 1
            if K-1 == 0:
                self.m[(p[0],p[1],0)] = 1
                
            # recursively move to the next round until hit base case
            if (p[0], p[1], K-1) not in self.m:
                self.solve(N,K-1, p[0],p[1])
                
            # when we reach this line self.m[(p[0], p[1], K-1)] is promised to get a value
            prob += (1/8) * self.m[(p[0], p[1], K-1)]
            
        self.m[(r,c,K)] = prob
            
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        self.m = {}
        self.solve(N,K,r,c)
        return self.m[(r,c,K)]
        
    