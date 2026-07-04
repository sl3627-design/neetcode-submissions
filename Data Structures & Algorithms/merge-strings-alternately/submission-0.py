class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ""
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                res += word2[j:]
                break
            if j == len(word2):
                res += word1[i:]
                break
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        return res