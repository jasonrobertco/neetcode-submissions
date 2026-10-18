class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visit = set()

        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visit):
                return 0 # do nothing
            visit.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r +dr,c + dc)
            return area
        
        best = 0
        for r in range(rows):
            for c in range(cols):
                best = max(best, dfs(r,c))
        return best
        