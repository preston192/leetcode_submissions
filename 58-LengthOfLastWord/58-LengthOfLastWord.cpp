// Last updated: 4/8/2026, 5:13:33 PM
class Solution {
public:
    int lengthOfLastWord(string s) {
        int k = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                k += 1;
            } else if (s[i] == ' ' && k != 0) {
                return k;
            }
        }
        return k;
    }
};