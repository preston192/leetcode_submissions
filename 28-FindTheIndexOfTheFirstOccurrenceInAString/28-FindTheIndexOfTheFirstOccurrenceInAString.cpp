// Last updated: 4/8/2026, 5:13:40 PM
class Solution {
public:
    int strStr(string haystack, string needle) {
        int k = 0;
        for (int i = 0; i < haystack.length(); i++) {
            if(haystack[i] == needle[k]) {
                k += 1;
                if(k == needle.length()) {
                    return i - k + 1;
                }
            } else {
                if(k > 0) {
                    i = i - k;
                }
                k = 0;
            }
        }
        return -1;
    }
};