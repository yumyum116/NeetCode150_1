# Approach    : Iteration
# Results     : runtime -> 0 ms, memory -> 17.94 MB
# Strength    : the fastest approach among all the other solutions
# Limitation  : the worst approach in space complexity and redundant code

class Solution:
    def scoreOfString(self, s: str) -> int:
        num = list(s)
        sum = 0
        for i in range(len(num) - 1):
            sum += abs(ord(num[i]) - ord(num[i + 1]))
        return sum
