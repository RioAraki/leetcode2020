class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int frontProduct = 1;
        int backProduct = 1;
        int ans = INT_MIN;
        for (int i = 0; i < nums.size(); ++i){
            frontProduct *= nums[i]; // multiply front to back
            backProduct *= nums[nums.size() - i - 1]; // multiply back to front
            ans = max(ans, max(frontProduct, backProduct));
            frontProduct = frontProduct == 0 ? 1 : frontProduct;
            backProduct = backProduct == 0 ? 1 : backProduct;
        }
        return ans;
    }
};