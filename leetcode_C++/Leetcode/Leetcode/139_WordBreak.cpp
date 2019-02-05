// dfs

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        if (s.size() == 0) {
            return true;
        }
        
        for (int i = 0; i < wordDict.size(); ++i) {
            if (wordDict[i] == s.substr(0,wordDict[i].size())){
                if (wordBreak(s.substr(wordDict[i].size(), s.size() - wordDict[i].size()), wordDict)){
                    return true;
                }
            }
        }
        return false;
    }
};

// dp

// dfs

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        
        for (int i = 1; i < s.size()+1; ++i){
            for (int j = i-1; j >=0; --j){ 
                if (dp[j]){
                    string word = s.substr(j,i-j);
                    cout << word << endl;
                    int flag = 0;
                    for (int k = 0; k < wordDict.size(); ++k){

                        if (wordDict[k] == word) {
                            cout << wordDict[k] << endl;
                            dp[i]=true;
                            flag = 1;
                            break;
                        } 
                    }
                    if (flag == 1){
                        break;
                    }    
                }     
            }
        }
        return dp[s.size()];
    }
};