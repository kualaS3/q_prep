from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    count += 1
        
        time = 0
        while q:
            for _ in range(len(q)):    
                r, c = q.popleft()
                for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr, nc = r + a, c + b
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count -= 1
                        q.append((nr, nc))
            if q:
                time += 1
        if count != 0:
            return -1
        else:
            return time
