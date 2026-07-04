class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        daily_profit = []
        for i in range(len(prices)-1):
            daily_profit.append(prices[i+1] - prices[i])
        
        daily_profit.sort()
        res = 0
        for p in daily_profit:
            if p > 0:
                res += p
        
        return res