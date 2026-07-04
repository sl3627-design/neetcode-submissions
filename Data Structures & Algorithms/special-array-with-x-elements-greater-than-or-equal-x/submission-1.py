class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            x = n - i  # number of elements >= nums[i] after sort
            # x is valid iff nums[i] >= x and (i == 0 or nums[i-1] < x)
            if nums[i] >= x and (i == 0 or nums[i-1] < x):
                return x
        return -1