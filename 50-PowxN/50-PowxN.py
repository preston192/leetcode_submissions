# Last updated: 4/8/2026, 5:13:36 PM
class Solution:
    def binaryExp(self, x, n):
        if n == 0: 
            return 1
        if n < 0: 
            return 1 / self.binaryExp(x, -n)

        if n % 2 == 0: 
            return self.binaryExp(x*x, n / 2)
        else: 
            return x * self.binaryExp(x*x, (n-1) / 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
        
