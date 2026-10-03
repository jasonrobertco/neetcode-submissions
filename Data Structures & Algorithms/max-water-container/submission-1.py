class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        best = 0
        while L <= R:
            H = min(heights[L], heights[R])
            W = R - L
            best = max(best, H*W)
            if heights[R] > heights[L]:
                L += 1
            else:
                R -= 1
        return best