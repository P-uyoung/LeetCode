# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
            # print(mid, ans)
                
        return ans