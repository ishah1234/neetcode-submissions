class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # 10, 1, 8, 2, 5, 7
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit