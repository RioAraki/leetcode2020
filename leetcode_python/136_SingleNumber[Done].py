# 2019-01-16: Done

# hashmap
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> mySet;
        for(int i = 0;i < nums.size();++i){
            if(mySet.find(nums[i]) == mySet.end()) mySet.insert(nums[i]);
            else mySet.erase(nums[i]);
        }
        auto it = mySet.begin();
        return *it;
    }
};

# 