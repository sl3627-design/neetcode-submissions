class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in nums:
            count = 1
            if num - 1 not in numset:
                while num+count in numset:
                    count += 1
                res = max(res, count)
        
        return res
