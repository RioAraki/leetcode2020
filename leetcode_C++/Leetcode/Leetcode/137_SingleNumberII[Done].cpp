// 2019-1-17: Done

// get sum of set and sum of all

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> db;
        int set_sum = 0;
        int two_sum = 0;
            
        for (int i: nums){
            if (db.find(i) == db.end()){
                db[i]=1;
                set_sum += i;
            } else {
                two_sum += i;
            }
        }
        return set_sum - two_sum/2;
    }
};