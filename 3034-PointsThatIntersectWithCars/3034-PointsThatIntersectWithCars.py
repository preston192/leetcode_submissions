# Last updated: 4/8/2026, 5:08:23 PM
class Solution(object):
    def numberOfPoints(self, nums):
        # Step 1: Sort the intervals by their starting points.
        nums.sort(key=lambda x: x[0])
        
        # Step 2: Merge the intervals.
        merged = []
        for interval in nums:
            if not merged or merged[-1][1] < interval[0]:
                # No overlap, so just add the interval.
                merged.append(interval)
            else:
                # Overlap exists: update the end of the last interval.
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        # Step 3: Count the number of integer points covered.
        total_points = 0
        for start, end in merged:
            total_points += (end - start + 1)
        
        return total_points