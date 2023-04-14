class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        for y in range(m):
            memo[(0,y)] = 1
        for x in range(n):
            memo[(x,0)] = 1
        
        def pathCount(coordinate):
            if coordinate not in memo:
                x, y = coordinate
                memo[(x,y)] = pathCount((x,y-1)) + pathCount((x-1,y))
            return memo[coordinate]
        
        return pathCount((n-1,m-1))
            