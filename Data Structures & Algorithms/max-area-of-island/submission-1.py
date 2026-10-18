from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def bfs(r,c):
            area = 1
        #make queue
            q = deque()
            #add to queue
            q.append((r,c))
            #mark as visited
            grid[r][c] = 0
            #check neighbors
            while q:
                row, col = q.popleft()  
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr>=0 and nr<rows and nc>=0 and nc< cols) and grid[nr][nc] == 1:
                        #add to q
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1
            return area

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  
                    best = max(best, bfs(r,c))
        return best
        