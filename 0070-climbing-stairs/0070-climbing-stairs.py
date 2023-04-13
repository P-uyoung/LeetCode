class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(two_count, one_count):
            if two_count == 0 :
                return 1
            result = (math.factorial(two_count + one_count) / (math.factorial(two_count) * math.factorial(one_count)))
            return int(result) + dfs(two_count-1, one_count+2)
        
        return dfs(n//2, n%2)
        