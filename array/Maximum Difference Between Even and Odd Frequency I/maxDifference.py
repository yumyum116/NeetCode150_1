# Approach   : Brute-force
# Results    : runtime -> 4 ms, memory -> 17.93 MB
# Strength   : versatility, easy to debug, and fast enough with small data
# Limitation : time and space consuming

class Solution:
    def maxDifference(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1
        values = char_count.values()
        
        odd_freq = [value for value in values if value % 2 == 1]
        even_freq = [value for value in values if value % 2 == 0]
        
        if not odd_freq or not even_freq:
            return 0
        
        max_diff = max(odd - even for odd in odd_freq for even in even_freq)
        return max_diff
