class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = 0
        count = 0
        while i < n and j < m:
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                count += 1
            
        
        return count