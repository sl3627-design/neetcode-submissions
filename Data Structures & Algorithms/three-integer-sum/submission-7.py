class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            target = - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    if [nums[l], nums[r], nums[i]] not in res:
                        res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
        
        return res
