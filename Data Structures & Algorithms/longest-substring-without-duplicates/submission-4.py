class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        l = 0

        if len(s) == 0:
            return 0

        while j < len(s)-1:
            j += 1
            if len(s[i:j+1]) != len(set(s[i:j+1])):
                i += 1
            l = max(l, j-i+1)
        
        l = max(l, j-i+1)
                
        
        return l

            