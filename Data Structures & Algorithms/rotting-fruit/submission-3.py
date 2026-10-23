class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        #iterate thru row sand cols
        #if == 2 rotten fruit
        #we add it to q
        q = deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        #whle q exists everyhting is q is rotten and seraching for neihbors
        while q and fresh>0:
            for x in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if(nr>=0 and nc>= 0 and nr<rows and nc<cols and grid[nr][nc] == 1):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            time +=1
        
        if fresh == 0:
            return time
        return -1

