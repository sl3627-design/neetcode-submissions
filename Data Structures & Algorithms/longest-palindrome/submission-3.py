class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for ss in s:
            if ss not in d:
                d[ss] = 1
            else:
                d[ss] += 1
        
        l = 0
        b = False
        for key, value in d.items():
            if value % 2 == 0:
                l += value
            else:
                l += (value // 2)*2
                b = True
        if b:
            l += 1
        return(l)