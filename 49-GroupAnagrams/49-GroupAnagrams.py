# Last updated: 4/8/2026, 5:13:37 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            groups[tuple(freq)].append(s)
        
        return list(groups.values())