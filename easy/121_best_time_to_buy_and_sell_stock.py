class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit_max  = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]: profit_max = max(profit_max, prices[r] - prices[l])
            else: l = r
        return profit_max
