class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0; b = len(nums)-1
        while a <= b:
            x = (b+a) // 2
            if nums[x] > target:
                a = a
                b = x-1

            elif nums[x] < target:
                a = x+1
                b = b
            
            else:
                return x 
        return -1
            