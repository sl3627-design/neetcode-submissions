class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.SquareSum(n)
        
        return True

    def SquareSum(self, n: int) -> int:
        return sum(int(d)**2 for d in str(n))