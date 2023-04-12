from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) 
        n = len(grid[0])
        count = 0 

        for x in range(n):
            for y in range(m):
                if grid[y][x] == '1':
                    count += 1
                    grid[y][x] = '0'
                    q = deque()
                    q.append((x,y))
                    while q:
                        cur_x, cur_y = q.popleft()
                        dx = [0,0,1,-1]
                        dy = [1,-1,0,0]
                       
                        for i in range(4):
                            nxt_x = cur_x + dx[i]
                            nxt_y = cur_y + dy[i]
                            
                            if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= m:
                                continue
                            if grid[nxt_y][nxt_x] =='1':
                                grid[nxt_y][nxt_x] = '0'
                                q.append((nxt_x, nxt_y))
        return count
