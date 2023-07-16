class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_pur = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_pur)
            min_pur = min(min_pur, prices[i])
        return max_profit
