# Last updated: 4/8/2026, 5:11:56 PM
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        
        scores = collections.defaultdict(list)
        for student_id, score in items:
            if len(scores[student_id]) < 5:
                scores[student_id].append(score)
            else:
                continue

        result = []
        for student_id in sorted(scores.keys()):
            avg = sum(scores[student_id]) // 5
            result.append([student_id, avg])
        
        return result
