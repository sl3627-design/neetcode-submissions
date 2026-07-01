class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Solution 1
        # nums.extend(nums)
        # return nums

        # Solution 2
        # for i in range(len(nums)):
        #     nums.append(nums[i])
        
        # return nums 

        # Solution 3
        return nums + nums