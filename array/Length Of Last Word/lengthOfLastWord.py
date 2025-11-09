# Approach      : Iteration (backward)
# Result        : runtime -> 0.756 sec, memory -> 52.1 MB
# Strength      : low memory usage O(1)
# Limitation    : none

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and count == 0:
                i -= 1
                continue
            if s[i] == ' ':
                break
            count += 1
        return count
