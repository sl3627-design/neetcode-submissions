class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        l = list()

        if len(s) == 0:
            return 0

        while j < len(s):
            j += 1
            if len(s[i:j+1]) != len(set(s[i:j+1])):
                l.append(j-i)
                i += 1
        
        l.append(j-i)
                
        
        return max(l)

            