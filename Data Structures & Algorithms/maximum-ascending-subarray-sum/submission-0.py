class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else:
                res = max(cur, res)
                cur = nums[i]
        
        res = max(cur, res)


        return res
        

