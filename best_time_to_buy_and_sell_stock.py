from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit