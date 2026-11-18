from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        high = 0
        def bfs(r, c):
            q = deque([(r,c)])
            grid[r][c] = 0
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                for a, b in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr, nc = r + a, c + b
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr,nc))
            return area
        for n in range(rows):
            for m in range(cols):
                if grid[n][m] == 1:
                    curr = bfs(n,m)
                    high = max(curr,high)
        return high
