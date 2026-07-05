class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            res = [1,1]
            for i in range(n-1):
                res.append(res[i] + res[i+1])
        
            return res[-1]