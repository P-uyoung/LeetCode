from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for n in nums:
            prefix.append(prefix[-1]*n)
            
        postfix = deque([1])
        for n in nums[::-1]:
            postfix.appendleft(postfix[0]*n)

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i+1])
        return ans