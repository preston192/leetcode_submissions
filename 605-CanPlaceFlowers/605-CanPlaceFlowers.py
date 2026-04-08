# Last updated: 4/8/2026, 5:12:11 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)

        if m == 1:
            if flowerbed[0] == 0:
                count += 1
            return n <= count

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = -1
            count += 1

        if flowerbed[m-1] == 0 and flowerbed[m-2] == 0:
            flowerbed[m-1] = -1
            count += 1

        for i in range(1, len(flowerbed)):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = -1
                count += 1
            if n <= count:
                return True

        return False