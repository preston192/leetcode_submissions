# Last updated: 4/8/2026, 5:08:27 PM
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_list = list(str(num))
        min_num = ""
        max_num = ""
        min_replace, max_replace = num_list[0], ""

        for d in num_list:
            if d != "9":
                max_replace = d
                break
        
        for i in range(len(num_list)):
            if num_list[i] == max_replace:
                max_num += "9"
            else:
                max_num += num_list[i]
            if num_list[i] == min_replace:
                min_num += "0"
            else:
                min_num += num_list[i]
        
        return int(max_num) - int(min_num)
        