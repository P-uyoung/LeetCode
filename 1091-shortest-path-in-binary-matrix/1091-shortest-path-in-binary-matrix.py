class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1 
        if n == 1:
            return 1
        
        visited = [[False]*n for _ in range(n)]     # [[False]*n]*n 으로 하면 안됨. 이렇게 하면 2차원 배열의 각 행이 같은 메모리를 가리키게 됨.
        shortest = [[10001]*n for _ in range(n)]                      # 마찬가지!
        dx = [0,0,1,-1,1,1,-1,-1]
        dy = [1,-1,0,0,1,-1,1,-1]
        q = deque()
        visited[0][0] = True
        q.append((0,0,1))
        
        while q:
            x, y, dist = q.popleft()
            for i in range(8):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                    continue
                if visited[next_y][next_x] == True or grid[next_y][next_x] == 1:
                    continue
                if shortest[next_y][next_x] > dist + 1:
                    shortest[next_y][next_x] = dist + 1
                    visited[next_y][next_x] = True
                    q.append((next_x, next_y, dist+1))
        
        if shortest[n-1][n-1] == 10001:
            return -1
        else:
            return shortest[n-1][n-1]
        