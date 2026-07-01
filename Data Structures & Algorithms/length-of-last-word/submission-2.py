class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        idx = len(s)-1
        while s[idx] == " " and idx >= 0:
            idx -= 1
        
        while s[idx] != " " and idx >= 0:
            count += 1
            idx -= 1
        
        return count