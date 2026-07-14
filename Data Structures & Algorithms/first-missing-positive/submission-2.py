class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if all(nums[i] <= 0 for i in range(len(nums))):
        #     return 1
        k = 1
        for i in range(len(nums)):
            if k not in nums:
                return k
            k += 1
        
        return k
        


