// dp: 1 dimension dp 

// dp[i] = dp[i-1] + dp[i-2]

class Solution {
public:
    int climbStairs(int n) {
        if (n == 0) return 1;
        if (n == 1) return 1;
        vector<int> dp = {1,2};
        
        for (int i = 2; i < n; ++i){
            dp.push_back(dp[i-1] + dp[i-2]);
        }
        
        return dp.back();
    }
};