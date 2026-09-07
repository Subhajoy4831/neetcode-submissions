class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        sell = 0
        for i,num in enumerate(prices):
            buy = min(buy,prices[i])
            sell = max(sell,prices[i]-buy)
        if sell<0:
            return 0
        return sell