class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # even = []
        # odd = []
        # for n in nums:
        #     if n%2 == 0:
        #         even.append(n)
        #     else:
        #         odd.append(n)
        
        # return even + odd

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return nums
