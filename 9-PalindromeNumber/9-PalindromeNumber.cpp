// Last updated: 4/8/2026, 5:14:21 PM
class Solution {
public:
    bool isPalindrome(int x) {
        std::string y = std::to_string(x);
        for (int i = 0; i < y.length() / 2; i++) {
            if (y[i] != y[y.length() - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}; 