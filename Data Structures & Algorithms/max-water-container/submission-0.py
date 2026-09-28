class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        L = 0
        R = len(heights)-1
        while L < R:
            W = R - L 
            H = min(heights[L], heights[R])
            best = max(W*H, best)
            #increment pointer
            #only the smaller height moves
            if heights[R] > heights[L]:
                L += 1
            else:
                R -= 1
        return best
        