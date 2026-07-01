class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        result = True
        if nums[0] <= nums[1]:
            for i in range(1, len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        elif nums[1] <= nums[0]:
            for i in range(1, len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False

        return result 
            
        