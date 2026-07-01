class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = set()
        area = 0 
        left = 0; right = len(heights) - 1


        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            areas.add(area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                right -= 1

        ans = max(areas)
        return ans
                