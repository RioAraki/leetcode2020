#include <iostream> 
#include <vector>
#include <unordered_map>

// leetcode: 2sum


std::vector<int> twoSum(std::vector<int>& nums, int target) {

	std::unordered_map<int, int> mapping;
	std::vector<int> result;

	for (int i=0; i < nums.size(); ++i) {
		mapping[nums[i]] = i;
	}

	for (auto iter = mapping.begin(); iter != mapping.end(); ++iter) {
		std::cout << " " << iter->first << ":" << iter->second << std::endl;
	}

	for (int i = 0; i < nums.size(); ++i) {
		int searched = target - nums[i];
		if (mapping.find(searched) != mapping.end()) {
			result.push_back(i);
			result.push_back(mapping[searched]);
		}
	}
};


int main() {
	std::vector<int> nums;
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(5);
	nums.push_back(9);
	nums.push_back(1);
	twoSum(nums, 6);

	std::cin.get();
}