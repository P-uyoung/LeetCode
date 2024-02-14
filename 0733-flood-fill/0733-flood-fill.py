from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M = len(image)
        N = len(image[0])
        
        before = image[sr][sc]
        
        que = deque()
        que.append((sr,sc))
        visited = [[False]*N for _ in range(M)]
        visited[sr][sc]= True
        image[sr][sc] = color
        
        while que:
            r, c = que.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r+dr, c+dc
                if nr<0 or nr >=M or nc<0 or nc>=N:
                    continue
                
                if not visited[nr][nc] and image[nr][nc] == before:
                    visited[nr][nc] = True
                    image[nr][nc] = color
                    que.append((nr,nc))
        return image
        