class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = 1; suffix = 1
        # prefixes = [1]; suffixes = [1]
        # for i in range (len(nums) - 1):
        #     prefix *= nums[i]
        #     prefixes.append(prefix)
        #     suffix *= nums[len(nums) - 1 - i]
        #     suffixes.append(suffix)
        
        # result = []
        # for i in range(len(prefixes)):
        #     result.append(prefixes[i]*suffixes[len(nums) - 1 - i])
    
        # return result

        res = [1] * len(nums)
        prefix = 1
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res



