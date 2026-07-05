class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        for i in range(len(num)-2):
            n = num[i:i+3]
            if len(set(n)) == 1:
                res.append(n)
        
        res.sort()
        if not res:
            return ""
        return res[-1]