class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def binary(n: int) -> int:
            count = 0
            while n > 0:
                if n%2 == 1:
                    count += 1
                n = n // 2
            return count 
        
        res = []

        for i in range(n+1):
            res.append(binary(i))
        
        return res