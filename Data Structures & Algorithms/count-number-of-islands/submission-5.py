class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowslen = len(grid)
        colslen = len(grid[0])
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #dfs
            #process
            #mark node as visited
            
            #for each neighbor
                #if not visited dfs
        def dfs(r,c):
            if r<0 or c<0 or r>=rowslen or c>=colslen or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            

        #bfs
            #mark node as visited
            #append to q
            #while q
                #q.popleft()
                #process
                    #for each neighbor 
                    #mark visited
                    #add to q
        for r in range(rowslen):
            for c in range(colslen):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands


            
