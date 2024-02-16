class Solution:
    def maxSubArray(self, nums):
        memo = {}
        
        def solve(i, must_pick):
            # memoization
            if (i, must_pick) in memo:
                return memo[(i, must_pick)]

            # right 인덱스를 결정함.
            if i >= len(nums):
                return 0 if must_pick else float('-inf')  # [1] 일 때, 1이 출력되어야함
            
            # if must_pick == True인 경우는, 마지막부터 0까지 누적합 한 번 구한것임.
            # if must_pick == Flase인 경우,
            # i 인덱스를 넣으려면, i+1 인덱스부터의 누적합이여야하고,
            # 넣지 않은 값과 비교한다.
            
            pick = nums[i] + solve(i+1, True)
            not_pick = 0 if must_pick else solve(i+1, False)
            
            memo[(i, must_pick)] = max(pick, not_pick)
            return memo[(i, must_pick)]

        return solve(0, False)