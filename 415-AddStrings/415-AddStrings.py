# Last updated: 4/8/2026, 5:12:18 PM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        result = []
        carry = 0
        for place in range(max(n1, n2)):
            if place >= n1:
                add = int(num2[-(1 + place)]) + carry
            elif place >= n2:
                add = int(num1[-(1 + place)]) + carry
            else: 
                add = int(num1[-(1 + place)]) + int(num2[-(1 + place)]) + carry
            carry, digit = divmod(add, 10)
            result.append(str(digit))
        
        if carry:
            result.append(str(carry))

        return "".join(reversed(result))