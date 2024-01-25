class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n, k = len(nums), 0
        i = 0
        while  i < n-k:
            while nums[i] == val:
                j = n -1 -k
                nums[i] = -1
                nums[i], nums[j] = nums[j], nums[i]
                k += 1
            i += 1
                
        return n-k
                
                
                