class Solution:
    def maxSubArray(self, nums):
        memo = {}  # 결과를 저장할 사전
        
        def solve(i, must_pick):
            # 메모이제이션: 이미 계산된 결과가 있는지 확인
            if (i, must_pick) in memo:
                return memo[(i, must_pick)]

            if i >= len(nums):
                return 0 if must_pick else float('-inf')
            
            # 현재 위치의 숫자를 선택하는 경우
            pick = nums[i] + solve(i+1, True)
            # 선택하지 않는 경우
            not_pick = solve(i+1, False) if not must_pick else 0
            
            # 최대값을 선택하여 메모에 저장
            memo[(i, must_pick)] = max(pick, not_pick)
            # print(i, must_pick, memo[(i, must_pick)] )
            # print(memo)
            return memo[(i, must_pick)]

        return solve(0, False)