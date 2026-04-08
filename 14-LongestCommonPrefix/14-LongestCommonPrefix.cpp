// Last updated: 4/8/2026, 5:14:16 PM
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int prefix_length = 0;
        if (strs.size() == 1) {
            return strs[0];
        } 
        else if (strs.size() > 1)
            for (int k = 0; k < strs.size(); k++) {
                if (strs[k] == "") {
                    return "";
                }
            }   
            for (int i = 0; i < 200; i++) {
                for (int j = 0; j < strs.size() - 1; j++) {
                    if (strs[j][i] != strs[j + 1][i] || i == strs[j].length()) {
                        return strs[0].substr(0,prefix_length);
                    }
                }
                prefix_length++;
            } 
        return strs[0];
    }
};