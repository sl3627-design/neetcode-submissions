class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                for j in range(counter):
                    nums[i - j] = nums[i+1]
                i = i - counter + 1
                counter = 0
            else:
                counter += 1
                i += 1
        
        for _ in range(counter):
            nums.remove(nums[-1])
        return len(nums)
