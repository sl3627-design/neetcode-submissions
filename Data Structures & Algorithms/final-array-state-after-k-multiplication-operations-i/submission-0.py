class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            for i in range(len(nums)):
                if nums[i] == min(nums):
                    nums[i] *= multiplier
                    break
            k -= 1
        
        return nums