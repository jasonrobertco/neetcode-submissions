class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid: return 0

        rows = len(grid) #height
        cols = len(grid[0]) #width (identical)
        visit = set() #map and track what weve visted
        count = 0 #how many islands we've found

        def bfs(r, c): #function
            q = deque([(r,c)]) # queue starts with the starting cell
            visit.add((r, c)) # mark (r,c) visited
            while q: # while queue not empty:
                row, col = q.popleft()#     pop from front set it to current cell
                #     check 4 neighbors (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == "1") and ((nr,nc) not in visit):
                #     if neighbor in bounds, is "1", and not in visit:
                #         add to visit, add to queue
                        visit.add((nr,nc))
                        q.append((nr,nc))
            pass

        # for each row
        #     for each col
        #         if grid[r][c] == "1" and (r,c) not in visit:
            #     bfs(r, c)
            #     count += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    count += 1

        return count