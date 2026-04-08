# Last updated: 4/8/2026, 5:13:07 PM
class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        curr = ""

        for c in s:
            if c.isdigit():
                curr += c
            elif c != " ":
                nums.append(int(curr))
                ops.append(c)
                curr = ""
        if curr:
            nums.append(int(curr))

        i = 0
        while i < len(ops):
            if ops[i] == "*":
                nums[i] *= nums[i+1]
                nums.pop(i+1)
                ops.pop(i)
            elif ops[i] == "/":
                nums[i] = int(nums[i] / nums[i+1])
                nums.pop(i+1)
                ops.pop(i)
            else:
                i += 1

        result = nums[0]
        for i, o in enumerate(ops):
            if o == "+":
                result += nums[i+1]
            else:
                result -= nums[i+1]

        return result
