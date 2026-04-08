# Last updated: 4/8/2026, 5:13:31 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a,2)
        b_int = int(b,2)
        while b_int!= 0:
            carry = a_int & b_int
            a_int = a_int ^ b_int
            b_int = carry << 1
        return str(bin(a_int)[2:])
