class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = res = 0
        for n in nums:
            counter = counter + 1 if n == 1 else 0
            res = max(res, counter)

        return res