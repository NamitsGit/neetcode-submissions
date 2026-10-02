class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for day_price in prices:
            if day_price < buy:
                buy = day_price
            profit = day_price - buy
            if profit > 0:
                max_profit = max(max_profit, profit)
        return max_profit
