class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowslen, colslen = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rowslen):
            for c in range(colslen):
                if grid[r][c] == 0: 
                    q.append((r,c)) #append as a tuple
        while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if(nr>=0 and nr<rowslen and nc>= 0 and nc<colslen) and (grid[nr][nc] == 2147483647):
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))
        return