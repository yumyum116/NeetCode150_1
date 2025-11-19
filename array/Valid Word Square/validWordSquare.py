# Approach    : Hash Map
# Results     : runtime -> 0.865 sec, memory -> 52 MB
# Strength    : easy to debug and high scalability
# Limitation  : additional memory required O(N^2)

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        column_words = [[0]]
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j < len(column_words) and j == column_words[j][0]:
                    column_words[j].append(words[i][j])
                else:
                    column_words.append([j, words[i][j]])
        for i in range(len(words)):
            if len(words[i]) != len(column_words[i]) - 1:
                return False
            for j in range(len(words[i])):
                if words[i][j] != column_words[i][j + 1]:
                    return False
        else:
            return True
