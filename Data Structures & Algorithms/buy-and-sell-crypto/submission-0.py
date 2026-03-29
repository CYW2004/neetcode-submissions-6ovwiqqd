class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_price = prices[len(prices) - 1]

        i = len(prices) - 2
        while i >= 0:
            max_price = max(max_price, prices[i])
            profit = max_price - prices[i]
            max_profit = max(max_profit, profit)
            i -= 1
        
        return max_profit