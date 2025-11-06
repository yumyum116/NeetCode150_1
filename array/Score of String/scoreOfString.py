# Approach    :
# Strength    :
# Limitation  :

class Solution:
    def scoreOfString(self, s: str) -> int:
        num = list(s)
        sum = 0
        for i in range(len(num) - 1):
            sum += abs(ord(num[i]) - ord(num[i + 1]))
        return sum
