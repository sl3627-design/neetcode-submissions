class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        d = {}
        res = 0

        for r in range(len(s)):
            if s[r] in d:
                l = max(d[s[r]] + 1, l)
            d[s[r]] = r
            
            res = max(r - l + 1, res)
        
        return res
