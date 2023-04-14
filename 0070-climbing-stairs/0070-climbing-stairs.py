class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1 : 1, 2 : 2}
        def cs(n):
            if n not in memo:
                memo[n]= cs(n-1) + cs(n-2)
            return memo[n]
        return cs(n)
          