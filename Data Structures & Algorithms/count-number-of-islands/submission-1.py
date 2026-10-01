class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #grid
        Rows = len(grid) #height
        Cols = len(grid[0]) #length
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def bfs(R, C):
            q = deque()
            grid[R][C] = "0"
            q.append((R,C))
            #nesw
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        #grid[R][C]
        #parse
        for R in range(Rows):
            for C in range(Cols):
                if grid[R][C] == "1":
                    bfs(R, C)
                    islands += 1

        return islands
        
        
                
                    
                

        