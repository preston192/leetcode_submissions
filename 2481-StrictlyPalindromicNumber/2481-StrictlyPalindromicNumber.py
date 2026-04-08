# Last updated: 4/8/2026, 5:08:28 PM
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            temp = n
            digits = ""
            while temp > 0:
                rem = temp % i
                digits = str(rem) + digits
                temp = temp // i
            # checking if palindrome while constructing
            if digits != digits[::-1]:
                return False
        return True