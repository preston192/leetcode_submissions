// Last updated: 4/8/2026, 5:08:46 PM
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++) {
            nums[i] += nums[i-1];
        }
        return nums;
    }
};