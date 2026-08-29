class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        profit = 0

        while l < len(prices) - 1 and r < len(prices) - 1:
            r += 1
            if prices[l] >= prices[r]:
                l = r
            profit = max(profit, prices[r] - prices[l])
        
        return profit