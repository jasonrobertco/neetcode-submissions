class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #function
        def bfs(r, c):
            q = deque()
            #mark as visited
            grid[r][c] = "0"
            #put start in q
            q.append((r,c))

            #while q not empty
            while q:
            #take node from front
                row, col = q.popleft()
            #process
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    #mark visited
                    grid[nr][nc] = "0"
                    #ad to q
                    q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands