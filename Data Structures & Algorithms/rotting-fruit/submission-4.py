class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
        
        while q and fresh > 0:
            for n in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if(nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -=1
                        q.append((nr,nc))
            time += 1
            print("minute", time, "fresh left:", fresh)
        
        return time if fresh == 0 else -1
        

        
                    
                