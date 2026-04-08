# Last updated: 4/8/2026, 5:12:04 PM
class Solution:
    def triangle_area(self, p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
        return area

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        best = 0
        n = len(points)
        for i in range(n-2):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    best = max(best, self.triangle_area(points[i], points[j], points[k]))
        return best

