class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(1,len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            elif nums[l] != 0:
                l += 1
                
                
                    