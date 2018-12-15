// 2018-12-15 pass 4ms

#include <vector>;
#include <unordered_map>
#include <stdio.h>;
#include <iostream>;

std::vector<int> twoSum(std::vector<int>& nums, int target) {
  std::unordered_map<int, int> hasht;
  int comple;
  for (int i = 0; i < nums.size(); ++i) {
    comple = target - nums[i];
    auto got = hasht.find(comple);
    // not found
    if (got == hasht.end()) {
      hasht.emplace(nums[i], i);
    }
    // found
    else {
      std::vector<int> ret;
      ret.resize(2);
      ret = { got->second, i };
      return ret;
    }
  }
  std::vector<int> wrong;
  wrong.resize(2);
  wrong = { -1, -1 };
  return wrong;
};


int main() {
  std::vector<int> nums;
  nums.resize(4);
  nums = { 2, 7, 11, 15 };
  int target = 9;
  twoSum(nums, target);
  return 0;
}
