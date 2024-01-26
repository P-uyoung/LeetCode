class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[k-1] and cnt < 2:
                cnt += 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif nums[i] != nums[k-1]:
                cnt = 1
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                
        return k