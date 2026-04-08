# Last updated: 4/8/2026, 5:12:20 PM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for i, num in enumerate(answer):
            if (i + 1) % 3 == 0:
                answer[i] = answer[i] + "Fizz"
            if (i + 1) % 5 == 0:
                answer[i] = answer[i] + "Buzz"
            if answer[i] == "":
                answer[i] = str(i + 1)
        return answer