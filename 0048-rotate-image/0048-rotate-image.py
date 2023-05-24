from collections import deque
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        length = N
        for i in range(N//2):
            idx = [(i, i+j) for j in range(length)]
            idx +=  [(i+j, i+length-1) for j in range(1, length)]
            idx += [(i+length-1, i+length-1-j) for j in range(1, length)]
            idx += [(i+length-1-j, i) for j in range(1, length-1)]
            
            # print(idx)
            arr =  deque([matrix[y][x] for y, x in idx])
            idx = idx[length-1:] + idx[:length-1]
            # print(len(arr), len(idx))
            for y, x in idx:
                matrix[y][x] = arr.popleft()
            length -= 2