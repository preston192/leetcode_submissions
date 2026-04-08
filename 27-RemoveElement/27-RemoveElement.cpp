// Last updated: 4/8/2026, 5:13:45 PM
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = 0; //counter for unique elements
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[n] = nums[i];
                n++;
            }
        }
        return n;
    }
};