class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        p = 0
        while r != len(prices):
            if prices[r] > prices[l]:
                p = max(p, prices[r]-prices[l])
            else:
                l=r #new low r is less
            r += 1
        return p