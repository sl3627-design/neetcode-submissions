class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin = curmax = 1

        for num in nums:
            tmp = curmax*num
            curmax = max(curmax*num, curmin*num, num)
            curmin = min(tmp, curmin*num, num)
            res = max(res, curmax)
        return res
