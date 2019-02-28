// iterator -> set vector<int>::iterator to the begin of a vector, it will iterate through the vector by calling ++
// vector.begin() / vector.end() -> unlike .front() returns a reference, the function returns a random access iterator pointing ot it
// dereference it *X to get the value

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> current;
        sort(candidates.begin(), candidates.end());
        backTracking(candidates.begin(), current, res, candidates, target);
        
        return res
    }
    
    
    void backTracking(vector<int>::iterator n, vector<int>& current, vector<vector<int>>& res, const vector<int>& candidates, int target){
        // base case when target == 0
        if (!target) res.push_back(current);
        
        else if (target > 0) {
            for (; n!=candidates.end() && *n <= target; ++n) {
                current.push_back(*n);
                backTracking(n+1, current, res, candidates, target-*n);
                current.pop_back();
                while(n+1!=candidates.end()&&*(n+1)==*n) ++n; // get rid of duplicate number
            }
            
        }
        
    }
};