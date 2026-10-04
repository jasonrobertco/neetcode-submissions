class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs
        #mark as visited
        #make q
        #append to q
        #while q
            #pop left
            #porcess neighbors
            #if notightbor not in visited
                #mark as visied
                #put in q
        rowslen = len(grid)
        colslen = len(grid[0])
        q = deque()
        fresh = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0
        #initial parse
        for r in range(rowslen):
            for c in range(colslen):
                if grid[r][c] == 2: 
                    q.append((r,c)) #append as a tuple
                if grid[r][c] == 1: 
                    fresh += 1 #count fresh for edge case
        #now while q
        while q and fresh > 0:
            #need a way to pop
            for x in range(len(q)): #for tuple in q
                #check neighbors to add to q
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr>=0 and nc>=0 and nr<rowslen and nc<colslen and grid[nr][nc] == 1:
                        #mark as visited
                        grid[nr][nc] = 2
                        fresh -= 1
                        #append to q
                        q.append((nr,nc)) #append as tuple
            #time for every layer
            time += 1
        if fresh == 0:
            return time
        else:
            return -1


        
                