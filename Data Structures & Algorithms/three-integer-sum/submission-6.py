class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range (n - 2):
            if nums[i] > 0: # positive anchor -> no zero-sum triplet possible
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicate anchor

            target = -nums[i]
            j = i + 1; k = n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: # skip dup j
                        j += 1
                    while j < k and nums[k] == nums[k+1]: # skip dup k
                        k -= 1
                        
        return result
