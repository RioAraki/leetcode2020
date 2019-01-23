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