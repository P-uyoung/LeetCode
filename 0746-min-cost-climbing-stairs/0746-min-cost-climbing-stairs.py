class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = {0: cost[0], 1: cost[1]}
        for i in range(2,n+1):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
        return dp[n]
        
        