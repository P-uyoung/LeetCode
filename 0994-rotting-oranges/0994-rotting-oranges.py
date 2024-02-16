from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshN = 0
        rotten = []
        # visited = [[False]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r,c, 0))
                    # visited[r][c] = True
                elif grid[r][c] == 1:
                    freshN += 1
        
        
        ans = 0
        que = deque(rotten)
        while que:    
            r, c, level = que.popleft()
            if level > ans:
                ans = level
            for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
                nr, nc = dr+r, dc+c
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc]==1:
                    freshN -= 1
                    grid[nr][nc] = 2
                    que.append((nr,nc,level+1))
        
        if freshN:
            return -1
        else:
            return ans
            
            
            
                   
        
                   


