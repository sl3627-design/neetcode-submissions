class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        res = 0

        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            r += 1

            res = max(r - l, res)
        
        return res
