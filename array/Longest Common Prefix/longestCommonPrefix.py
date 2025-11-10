# Approach     : Horizontal Scanning
# Results      : runtime -> 0.815 sec, memory -> 52.3 MB
# Strength     : no extra memory O(1) and relatively fast approach O(n*m)
# Limitation   : redundant code

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            if strs[i] == "":
                return ""
        hash_string = list(enumerate(strs))
        str1 = hash_string[0][1]
        str2 = hash_string[1][1]
        if not str1[0] == str2[0]:
            return ""
        i = 0
        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            prefix.append(str1[i])
            i += 1
        index = len(prefix)
        for j in range(2, len(strs)):
            string = hash_string[j][1]
            k = 0
            while k < min(len(prefix), len(string)) and prefix[k] == string[k]:
                    k += 1
            index = min(k, index)
        return "".join(prefix[:index])
