class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mins = 0
        
        q = deque()
        fresh = 0

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for x in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            mins += 1
        
        return mins if fresh == 0 else -1


            


