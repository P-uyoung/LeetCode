class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1 
        if n == 1:
            return 1
        
        # shortest = [[10001]*n for _ in range(n)]  # BFS 먼저 도착한 게 최단거리임. shortest 필요 없음.
        dx = [0,0,1,-1,1,1,-1,-1]
        dy = [1,-1,0,0,1,-1,1,-1]
        q = deque()
        grid[0][0] = 1                              # 방문 처리
        q.append((0,0,1))
        
        while q:
            x, y, dist = q.popleft()
            for i in range(8):                      # 방문 예약
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                    continue
                if grid[next_y][next_x] == 1:
                    continue
                if next_x == n-1 and next_y == n-1:
                    return dist + 1
                else:
                    grid[next_y][next_x] = 1
                    q.append((next_x, next_y, dist+1))
        
        return -1
        