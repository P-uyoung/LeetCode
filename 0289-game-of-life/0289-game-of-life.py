import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        origin = copy.deepcopy(board)
        dx = (0, 1, 0, -1, 1, -1, 1, -1)
        dy = (1, 0, -1, 0, -1, 1, 1, -1)
        for y in range(m):
            for x in range(n):
                neighbors = []
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0<= ny < m:
                        neighbors.append(origin[ny][nx])
                liveN = neighbors.count(1)
                if origin[y][x] == 1:
                    if liveN < 2 :
                        board[y][x] = 0
                    elif liveN <4 :
                        board[y][x] = 1
                    else :
                        board[y][x] = 0
                else:
                    if liveN == 3:
                        board[y][x] = 1
                    
                    
                        
                