https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_value = 0
        min_value = float('inf')
        for i in range(len(prices)):
            min_value = min(min_value,prices[i])
            max_value = max(max_value,prices[i]-min_value)
        return max_value