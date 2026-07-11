class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_w = nums[:k]
        res = max(curr_w) - min(curr_w)

        for i in range(k, len(nums)):
            curr_w.append(nums[i])
            curr_w.pop(0)
            res = min(res, max(curr_w) - min(curr_w))
        
        return res
