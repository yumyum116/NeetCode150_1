# Approach    : Integrating approach of pattern extraction, equivalent class grouping, and O(N^2) grouping
# Results     : runtime -> 1354 ms, memory -> 235.79 MB
# Strength    : easy to follow processes step by step and concise
# Limitation  : time and memory consuming, complext and high possibility of occurring bug

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = []
        t_list = []
        for i in range(len(s)):
            s_list.append(s[i])
        for i in range(len(t)):
            t_list.append(t[i])
        
        s_word_occurrence = [[s_list[0], 0]]
        for i in range(0, len(s_list) - 1):
            for j in range(i + 1, len(s_list)):
                if s_list[j] == s_word_occurrence[i][0]:
                    s_word_occurrence[i].append(j)
                else:
                    s_word_occurrence.append([s_list[j], j])
            if s_word_occurrence[i][-1] == len(s_list) - 1:
                break
            
        t_word_occurrence = [[t_list[0], 0]]
        for i in range(0, len(t_list) - 1):
            for j in range(i + 1, len(t_list)):
                if t_list[j] == t_word_occurrence[i][0]:
                    t_word_occurrence[i].append(j)
                else:
                    t_word_occurrence.append([t_list[j], j])
            if t_word_occurrence[i][-1] == len(t_list) - 1:
                break
            
        if len(s_word_occurrence) != len(t_word_occurrence):
            return False
        
        for i in range(len(s_word_occurrence)):
            if len(s_word_occurrence[i]) != len(t_word_occurrence[i]):
                return False
            for j in range(1, len(s_word_occurrence[i])):
                if s_word_occurrence[i][j] != t_word_occurrence[i][j]:
                    return False
        else:
            return True
