class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rowslen, colslen = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #dfs
            #mark current node as visited
            #process it
            #look at neighbors criteria
                #call dfs
        def dfs(r,c):
            if r<0 or c<0 or r >= rowslen or c >= colslen or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(dr+r,dc+c)
                
        #bfs
            #mark as visited
            #make a q
            #append to q
            #whileq
                #pop left
                #look at neighbors criteria
                    #mark as visited
                    #append to q
        def bfs(r,c):
            grid[r][c] = "0"
            q = deque()
            q.append((r,c))
            while q:
                row, col = q.popleft() #gives from tuple
                #look at neighbors
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr<0 or nc<0 or nr>=rowslen or nc>=colslen or grid[nr][nc] == "0":
                        continue #continue to next loop
                    grid[nr][nc] = "0"
                    q.append((nr, nc)) #append as tuple


        for r in range(rowslen):
            for c in range(colslen):
                if grid[r][c] == "1":
                    #bfs/dfs
                    #dfs(r,c)
                    bfs(r,c)
                    islands+=1
        return islands

        