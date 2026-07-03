class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        res = True

        if len(nums) == 1:
            return res
        
        for i in range (len(nums) - 1):
            if nums[i]%2 == nums[i+1]%2:
                return not res
        
        return res