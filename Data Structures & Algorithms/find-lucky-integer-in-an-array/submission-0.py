class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        res = -1
        for key, value in d.items():
            if key == value:
                res = max(res, key)
        
        return res