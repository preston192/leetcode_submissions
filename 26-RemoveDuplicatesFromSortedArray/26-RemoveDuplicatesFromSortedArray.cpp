// Last updated: 4/8/2026, 5:13:44 PM
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[k - 1] != nums[i]) {
                nums[k] = nums[i];
                k+=1;
            }
        }
        return k;
    }
};