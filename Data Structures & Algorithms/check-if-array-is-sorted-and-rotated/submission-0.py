class Solution:
    def check(self, nums: List[int]) -> bool:
        extended = nums + nums
        sorted_arr = sorted(nums)
        i = 0; j = len(nums) - 1
        while j < len(extended):
            if extended[i:j+1] == sorted_arr:
                return True
            i += 1
            j += 1
        return False