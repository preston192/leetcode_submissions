# Last updated: 4/8/2026, 5:11:18 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = list(str(num))

        for i, d in enumerate(str_num):
            if d == "6":
                str_num[i] = "9"
                break

        return int("".join(str_num))
                
