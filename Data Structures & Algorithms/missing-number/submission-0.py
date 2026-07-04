class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for idx, n in enumerate(nums):
            if idx not in nums:
                return idx
            elif len(nums) not in nums:
                return len(nums)
                