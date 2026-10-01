class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        fresh = 0
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        mins = 0

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
        while q and fresh > 0:
            for x in range(len(q)):
                r,c = q.popleft()
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < Rows and 0 <= nc < Cols and grid[nr][nc] == 1):
                        q.append((nr,nc))
                        fresh -= 1
                        grid[nr][nc] = 2
            mins +=1
        return mins if fresh == 0 else -1
