# Approach    : Brute-Force
# Results     : FAILURE 4 / 69 PASSED
# Strength    : intensive, fast enough with small data, no extra data structure, high flexibility
# Limitation  : time consuming O(n^2 * m^2), thus low efficiency with large data

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        tmp = words[0]
        start = 0
        end = 0
        in_word = 0
        offset = 0
        for word in words[1:]:
            for i in range(len(tmp)):
                for j in range(offset, len(word)):
                    if word[j] == tmp[i] and start == 0 and in_word == 0:
                        start = i
                        offset = j + 1
                        in_word = 1
                        break
                    if word[j] == tmp[i] and in_word == 1:
                        end = max(end, i)
                        offset = j + 1
                        break
                    if offset != 0 and in_word == 1 and word[j] != tmp[i] and word[j - 1] == tmp[i]:
                        start = i
            if end != 0:
                substrings.append(tmp[start:end + 1])
                start = 0
                end = 0
                offset = 0
                in_word = 0
                continue
            if in_word == 0:
                tmp = word
        return substrings        
