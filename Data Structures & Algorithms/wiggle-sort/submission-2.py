class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
  
        if len(nums) == 2:
            if nums[1] < nums[0]:
                nums[0], nums[1] = nums[1], nums[0]

        for i in range(1, len(nums) - 1):
            if i&1 and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if i&1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            if i&0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if i&0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    