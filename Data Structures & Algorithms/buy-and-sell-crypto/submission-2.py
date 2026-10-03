class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        best = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            best = max(best, prices[R]-prices[L])
        return best
        
        