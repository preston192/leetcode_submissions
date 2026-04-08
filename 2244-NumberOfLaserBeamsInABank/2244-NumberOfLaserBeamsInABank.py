# Last updated: 4/8/2026, 5:08:32 PM
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        prev = 0

        for row in bank:
            count = row.count("1")
            if count == 0:
                continue
            lasers += count * prev
            prev = count
    
        return lasers