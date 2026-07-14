class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)):
            if k not in set(nums):
                return k
            k += 1
        
        return k
        


