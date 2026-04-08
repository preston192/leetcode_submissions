# Last updated: 4/8/2026, 5:13:22 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (row + 1) for row in range(numRows)]
        
        for i in range(2,numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
                
        return pascal