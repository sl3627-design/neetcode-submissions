class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 0
        while x <= len(nums):
            if x == sum([x <= n for n in nums]):
                return x
            x += 1
        
        return -1