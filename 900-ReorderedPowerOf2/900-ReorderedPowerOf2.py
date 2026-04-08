# Last updated: 4/8/2026, 5:12:03 PM
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # idea: number must have same # of digits as the power of 2
        digits = len(str(n))
        product = 1
        powers = []
        while len(str(product)) <= digits:
            if len(str(product)) ==  digits:
                powers.append("".join(sorted(str(product))))
            product *= 2
        for power in powers:
            if "".join(sorted(str(n))) == power:
                return True
        return False