# Approach    : Two-pointer
# Results     : runtime -> 0.889, memory -> 52 MB
# Strength    : 
# Limitation  : 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        index = [0] * len(s)
        hash_s = list(enumerate(s))
        hash_t = list(enumerate(t))
        for i in range(len(s)):
            start = index[i - 1] + 1 if i > 0 else 0
            for j in range(start, len(t)):
                if hash_s[i][1] == hash_t[j][1]:
                    index[i] = (hash_t[j][0])
                    break
            else:
                return False
        if len(index) == len(s):
            for i in range(1, len(index)):
                if index[i - 1] > index[i]:
                    return False
                else:
                    return True
        return False
